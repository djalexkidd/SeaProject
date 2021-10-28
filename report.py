import csv
from tkinter import *
import vlc # python-vlc est nécéssaire pour lire la musique
import re
import json
import urllib.request

# Permet d'obtenir la géolocalisation
url = 'http://ipinfo.io/json'
response = urllib.request.urlopen(url)
data = json.load(response)

# IP=data['ip']
# org=data['org']
# city = data['city']
# country=data['country']
# region=data['region']
latitude=data['loc']

# print("Your IP detail\n")
# print("IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}\nLat : {5}".format(org,region,country,city,IP,latitude))

sea = Tk()
sea.geometry("800x600+100+100") # Taille de la fenêtre
sea.title("Oil Alert") # Titre de la fenêtre
img = PhotoImage(file="imgs/favicon.png") # Charge l'image de l'icone
sea.tk.call("wm", "iconphoto", sea._w, img) # Place l'icone dans la barre de fenêtre
bg = PhotoImage(file="imgs/background.png") # Charge l'image de l'arrière-plan
photo = Label(sea, image=bg)
photo.place(x=0, y=0) # Place l'image en arrière-plan
p = vlc.MediaPlayer("sounds/music.mp3") # Charge la musique
p.play() # Lire la musique

# Fonction pour écrire le formulaire dans un fichier CSV
def write_csv(meteo, vent, latitude):
    with open("report.csv", "a", newline='', encoding='utf-8') as file: # Écrit dans le fichier report.csv
        write = csv.writer(file, quoting = csv.QUOTE_ALL)
        write.writerow([meteo.get()] + [] + [vent.get()] + [] + [latitude]) # Écrit le formulaire dans le fichier

    # Fenêtre du bouton OK
    newWindow = Toplevel(sea)
    newWindow.geometry("600x90+100+100") # Taille de la fenêtre
    newWindow.title("Merci")
    img = PhotoImage(file="imgs/favicon.png")
    newWindow.tk.call("wm", "iconphoto", newWindow._w, img)

    # Fait apparaitre la fenêtre
    Label(newWindow, text ="Merci d'avoir signalé la marée noire !\nLe programme récupère la géolocalisation automatiquement.", font=("Ubuntu", 14)).pack()

    def click_ok():
        label_ok = Label(sea, text ="OK")
        sea.destroy() # Quitte le programme

    button_ok = Button(newWindow, text="OK", command = click_ok, padx = 25, pady = 10)
    button_ok.pack()

# Fonction pour vérifier que le champ météo est bon
def checkError():
    if bool(re.search(r"\b^c(alme)?$\b|\b^a(gité)?$\b", str(meteo.get()), re.IGNORECASE)) and bool(re.search(r"\b^l(ent)?$\b|\b^r(apide)?$\b", str(vent.get()), re.IGNORECASE)) == True:
        write_csv(meteo, vent, latitude)
    else:
        error()

#Fonction pour notifier qu'une donnée de l'utilisateur n'est pas valide
def error():
    errorWindow = Toplevel(sea)
    errorWindow.geometry("300x80+100+100") # Taille de la fenêtre
    errorWindow.title("Erreur")
    img = PhotoImage(file="imgs/favicon.png")
    errorWindow.tk.call("wm", "iconphoto", errorWindow._w, img)

    Label(errorWindow, text ="Données non conforme !", font=("Ubuntu", 14)).pack()

    button_ok = Button(errorWindow, text="OK", command = errorWindow.destroy, padx = 25, pady = 10)
    button_ok.pack()

def mute():
    if p.is_playing():
        p.stop()
    else:
        p.play()

# Label à placer à gauche du champ de texte pour la météo
meteo_info = Label(sea, text="Quel est la météo ? (calme ou agité)", font=("Ubuntu", 20))
meteo_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
meteo_info.place(relx=0.5, rely=0.1, anchor=N)

# Label à placer à gauche du champ de texte pour la vitesse du vent
vent_info = Label(sea, text="Quel est la vitesse du vent ? (lent ou rapide)", font=("Ubuntu", 20))
vent_info.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)
vent_info.place(relx=0.5, rely=0.3, anchor=N)

# Champ de texte à placer pour la météo
meteo = Entry(sea, width = 50, borderwidth = 5, font=("Ubuntu", 18))
meteo.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

# Champ de texte à placer pour la vitesse du vent
vent = Entry(sea, width = 50, borderwidth = 5, font=("Ubuntu", 18))
vent.grid(row = 3, column = 0, columnspan = 3, padx = 10, pady = 10)

button_1 = Button(sea, text="Send", padx = 30, pady = 15, fg = "#00ff00", command = checkError, font=("Ubuntu", 25)) # Bouton envoyer (lambda envoie les quatre valeurs)
button_2 = Button(sea, text="Exit", padx = 40, pady = 15, fg = "#ff0000", command = sea.destroy, font=("Ubuntu", 25)) # Bouton quitter
button_3 = Button(sea, text="Mute Music", fg = "#ff0000", command = mute, font=("Ubuntu", 12)) # Bouton mute

button_1.grid(row = 8, column = 0)
button_2.grid(row = 8, column = 1)
button_3.grid(row = 3, column = 2)

# Mise en page des boutons
button_1.place(relx=0.35, rely=0.6, anchor=CENTER)
button_2.place(relx=0.65, rely=0.6, anchor=CENTER)
button_3.place(relx=0, rely=0, anchor=NW)
meteo.place(relx=0.5, rely=0.2, anchor=N)
vent.place(relx=0.5, rely=0.4, anchor=N)

sea.resizable(False, False) # Désactive le redimensionnement de la fenêtre

sea.mainloop()
