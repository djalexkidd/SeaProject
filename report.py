import csv
from tkinter import *
import vlc # python-vlc est nécéssaire pour lire la musique

sea = Tk()
sea.geometry("800x600+100+100") # Taille de la fenêtre
sea.title("Report oil leaking") # Titre de la fenêtre
img = PhotoImage(file="imgs/favicon.png") # Charge l'image de l'icone
sea.tk.call("wm", "iconphoto", sea._w, img) # Place l'icone dans la barre de fenêtre
bg = PhotoImage(file="imgs/background.png") # Charge l'image de l'arrière-plan
photo = Label(sea, image=bg)
photo.place(x=0, y=0) # Place l'image en arrière-plan
p = vlc.MediaPlayer("sounds/music.mp3") # Charge la musique
p.play() # Lire la musique

# Fonction pour écrire le formulaire dans un fichier CSV
def write_csv(meteo, vent, longitude, latitude):
    with open("report.csv", "a", newline='', encoding='utf-8') as file: # Écrit dans le fichier report.csv
        write = csv.writer(file, quoting = csv.QUOTE_ALL)
        write.writerow([meteo.get()] + [] + [vent.get()] + [] + [longitude.get()] + [] + [latitude.get()]) # Écrit le formulaire dans le fichier

    # Fenêtre du bouton OK
    newWindow = Toplevel(sea)
    newWindow.geometry("300x50+100+100") # Taille de la fenêtre
    newWindow.title("Thanks")
    img = PhotoImage(file="imgs/favicon.png")
    newWindow.tk.call("wm", "iconphoto", newWindow._w, img)

    # Fait apparaitre la fenêtre
    Label(newWindow, text ="Thanks for report the oil leaking !").pack()
    label = Label(sea, text ="Thanks for report the oil leaking !")
    label.pack

    def click_ok():
        label_ok = Label(sea, text ="Ok")
        sea.destroy() # Quitte le programme

    button_ok = Button(newWindow, text="Ok", command = click_ok, padx = 25, pady = 10)
    button_ok.pack()

def mute():
    if p.is_playing():
        p.stop()
    else:
        p.play()

# Label à placer à gauche du champ de texte pour la météo
meteo_info = Label(sea, text="Quel est la météo ? (calme ou agité)")
meteo_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
meteo_info.place(relx=0.5, rely=0.1, anchor=N)

# Label à placer à gauche du champ de texte pour la vitesse du vent
vent_info = Label(sea, text="Quel est la vitesse du vent ? (lent ou rapide)")
vent_info.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)
vent_info.place(relx=0.5, rely=0.3, anchor=N)

# Label à placer à gauche du champ de texte pour la longitude
longitude_info = Label(sea, text="Quel est votre longitude ?")
longitude_info.grid(row = 4, column = 0, columnspan = 3, padx = 10, pady = 10)
longitude_info.place(relx=0.5, rely=0.5, anchor=N)

# Label à placer à gauche du champ de texte pour la latitude
latitude_info = Label(sea, text="Quel est votre latitude ?")
latitude_info.grid(row = 6, column = 0, columnspan = 3, padx = 10, pady = 10)
latitude_info.place(relx=0.5, rely=0.7, anchor=N)

# Champ de texte à placer pour la météo
meteo = Entry(sea, width = 50, borderwidth = 5)
meteo.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

# Champ de texte à placer pour la vitesse du vent
vent = Entry(sea, width = 50, borderwidth = 5)
vent.grid(row = 3, column = 0, columnspan = 3, padx = 10, pady = 10)

# Champ de texte à placer pour la longitude
longitude = Entry(sea, width = 50, borderwidth = 5)
longitude.grid(row = 5, column = 0, columnspan = 3, padx = 10, pady = 10)

# Champ de texte à placer pour la latitude
latitude = Entry(sea, width = 50, borderwidth = 5)
latitude.grid(row = 7, column = 0, columnspan = 3, padx = 10, pady = 10)

button_1 = Button(sea, text="Send", padx = 50, pady = 15, fg = "#00ff00", command = lambda: write_csv(meteo, vent, longitude, latitude)) # Bouton envoyer (lambda envoie les quatre valeurs)
button_2 = Button(sea, text="Exit", padx = 50, pady = 15, fg = "#ff0000", command = sea.destroy) # Bouton quitter
button_3 = Button(sea, text="Mute Music", fg = "#ff0000", command = mute) # Bouton mute

button_1.grid(row = 8, column = 0)
button_2.grid(row = 8, column = 1)
button_3.grid(row = 3, column = 2)

# Mise en page des boutons
button_1.place(relx=0.4, rely=0.9, anchor=N)
button_2.place(relx=0.6, rely=0.9, anchor=N)
button_3.place(relx=0, rely=0, anchor=NW)
meteo.place(relx=0.5, rely=0.2, anchor=N)
vent.place(relx=0.5, rely=0.4, anchor=N)
longitude.place(relx=0.5, rely=0.6, anchor=N)
latitude.place(relx=0.5, rely=0.8, anchor=N)

sea.resizable(False, False) # Désactive le redimensionnement de la fenêtre

sea.mainloop()
