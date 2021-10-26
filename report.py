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
p = vlc.MediaPlayer("imgs/music.m4a") # Charge la musique
p.play() # Lire la musique

# Fonction pour écrire le formulaire dans un fichier CSV
def write_csv(who, when, where):
    with open("report.csv", "a", newline='', encoding='utf-8') as file: # Écrit dans le fichier report.csv
        write = csv.writer(file, quoting = csv.QUOTE_ALL)
        write.writerow([who.get()] + [] + [where.get()] + [] + [when.get()]) # Écrit le formulaire dans le fichier

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

# Label à placer à gauche du champ de texte pour Who
who_info = Label(sea, text="Who are you ?")
who_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
who_info.place(relx=0.15, rely=0.11, anchor=N)

# Label à placer à gauche du champ de texte pour Where
where_info = Label(sea, text="Where is it ?")
where_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
where_info.place(relx=0.15, rely=0.21, anchor=N)

# Label à placer à gauche du champ de texte pour When
when_info = Label(sea, text="When is it ?")
when_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
when_info.place(relx=0.15, rely=0.31, anchor=N)

# Champ de texte à placer pour Who
who = Entry(sea, width = 50, borderwidth = 5)
who.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# Champ de texte à placer pour Where
where = Entry(sea, width = 50, borderwidth = 5)
where.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

# Champ de texte à placer pour When
when = Entry(sea, width = 50, borderwidth = 5)
when.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)

button_1 = Button(sea, text="Send", padx = 50, pady = 15, fg = "#00ff00", command = lambda: write_csv(who, when, where)) # Bouton envoyer (lambda envoie les trois valeurs)
button_2 = Button(sea, text="Exit", padx = 50, pady = 15, fg = "#ff0000", command = sea.destroy) # Bouton quitter

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)

# Mise en page des boutons
button_1.place(relx=0.4, rely=0.5, anchor=N)
button_2.place(relx=0.6, rely=0.5, anchor=N)
who.place(relx=0.5, rely=0.1, anchor=N)
where.place(relx=0.5, rely=0.2, anchor=N)
when.place(relx=0.5, rely=0.3, anchor=N)

sea.resizable(False, False) # Désactive le redimensionnement de la fenêtre

sea.mainloop()