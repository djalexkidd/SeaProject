import csv
from tkinter import *

sea = Tk()
sea.geometry("800x600+100+100")
sea.title("Report oil leaking")
img = PhotoImage(file="imgs/favicon.png")
sea.tk.call("wm", "iconphoto", sea._w, img)
bg = PhotoImage(file="imgs/background.png")
photo = Label(sea, image=bg)
photo.place(x=0, y=0)

def write_csv(who, when, where):
    with open("report.csv", "a", newline='', encoding='utf-8') as file:
        write = csv.writer(file, quoting = csv.QUOTE_ALL)
        write.writerow([info1.get()] + [] + [info2.get()] + [] + [info3.get()])
    newWindow = Toplevel(sea)
    Label(newWindow, text ="Thanks for report the oil leaking !").pack()
    label = Label(sea, text ="Thanks for report the oil leaking !")
    label.pack

    def click_ok():
        label_ok = Label(sea, text ="Ok")
        sea.destroy()

    button_ok = Button(newWindow, text="Ok", command = click_ok, padx = 25, pady = 10)
    button_ok.pack()

info1 = StringVar()
who = Entry(sea, width = 50, borderwidth = 5, textvariable=info1)
who.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
who.insert(0, "Who are you ?")

info2 = StringVar()
where = Entry(sea, width = 50, borderwidth = 5, textvariable=info2)
where.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)
where.insert(0, "Where is it ?")

info3 = StringVar()
when = Entry(sea, width = 50, borderwidth = 5, textvariable=info3)
when.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)
when.insert(0, "When is it ?")

button_1 = Button(sea, text="Send", padx = 50, pady = 15, fg = "#00ff00", command = lambda: write_csv(who, when, where))
button_2 = Button(sea, text="Exit", padx = 50, pady = 15, fg = "#ff0000", command = sea.destroy)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)

sea.resizable(False, False)

sea.mainloop()
