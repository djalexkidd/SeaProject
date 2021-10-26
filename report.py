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
        write.writerow([who.get()] + [] + [where.get()] + [] + [when.get()])

    newWindow = Toplevel(sea)
    newWindow.geometry("300x50+100+100")
    newWindow.title("Thanks")
    img = PhotoImage(file="imgs/favicon.png")
    newWindow.tk.call("wm", "iconphoto", newWindow._w, img)

    Label(newWindow, text ="Thanks for report the oil leaking !").pack()
    label = Label(sea, text ="Thanks for report the oil leaking !")
    label.pack

    def click_ok():
        label_ok = Label(sea, text ="Ok")
        sea.destroy()

    button_ok = Button(newWindow, text="Ok", command = click_ok, padx = 25, pady = 10)
    button_ok.pack()

who_info = Label(sea, text="Who are you ?")
who_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
who_info.place(relx=0.15, rely=0.11, anchor=N)

where_info = Label(sea, text="Where is it ?")
where_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
where_info.place(relx=0.15, rely=0.21, anchor=N)

when_info = Label(sea, text="When is it ?")
when_info.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
when_info.place(relx=0.15, rely=0.31, anchor=N)

who = Entry(sea, width = 50, borderwidth = 5)
who.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

where = Entry(sea, width = 50, borderwidth = 5)
where.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

when = Entry(sea, width = 50, borderwidth = 5)
when.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)

button_1 = Button(sea, text="Send", padx = 50, pady = 15, fg = "#00ff00", command = lambda: write_csv(who, when, where))
button_2 = Button(sea, text="Exit", padx = 50, pady = 15, fg = "#ff0000", command = sea.destroy)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)

button_1.place(relx=0.4, rely=0.5, anchor=N)
button_2.place(relx=0.6, rely=0.5, anchor=N)
who.place(relx=0.5, rely=0.1, anchor=N)
where.place(relx=0.5, rely=0.2, anchor=N)
when.place(relx=0.5, rely=0.3, anchor=N)

sea.resizable(False, False)

sea.mainloop()