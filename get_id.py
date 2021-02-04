from tkinter import *
import webbrowser
from util import application_path
from traduction import Traduction
import os
from tkinter.messagebox import showerror

def get_id(config):
    def open_doc():
        webbrowser.open("https://discord.com/developers/applications")
    root = Tk()
    root.iconbitmap(os.path.join(application_path(), "StatusChanger.ico"))
    root.title("StatusChanger")
    root.geometry("300x400")
    trad = Traduction()
    try:
        trad.load_id_page(root, config["values"]["langue"])
    except KeyError:
        trad.load_id_page(root, "en")
    label = Label(root, textvariable=trad["application_here"])
    label.pack()
    id = StringVar()
    try:
        id.set(config["values"]["application_id"])
    except KeyError: pass
    text = Entry(root, textvariable=id)
    text.pack()
    def check():
        if id.get().isdigit():
            root.destroy()
        else:
            showerror(trad["invalide_id_title"].get(), trad["invalide_id_content"].get())
    def close():
        sys.exit(0)
    bouton = Button(root, textvariable=trad["continue"], command=check, width=20)
    bouton.pack()
    spinbox_value = StringVar()
    try:
        spinbox_value.set(config["values"]["pipe"])
    except KeyError: pass
    spinbox = Spinbox(root, from_=0, to=9,increment=1, textvariable=spinbox_value)
    spinbox.pack()
    Button(root, textvariable=trad["get_id"], command=open_doc).pack(side=BOTTOM)
    lang_frame = Frame(root)
    def set_fr():
        trad.set_id_page("fr")
    fr = PhotoImage(file="flag_fr.png")
    fr = fr.subsample(11, 11) 
    Button(lang_frame, image=fr, command=set_fr).pack(side="right")
    def set_en():
        trad.set_id_page("en")
    gb = PhotoImage(file="flag_gb.png")
    gb = gb.subsample(11, 11)
    Button(lang_frame, image=gb, command=set_en).pack(side="right")
    lang_frame.pack(side=BOTTOM)
    root.protocol("WM_DELETE_WINDOW", close)
    root.mainloop()
    config["values"]["application_id"] = id.get()
    config["values"]["pipe"]           = spinbox_value.get()
    config["values"]["langue"]         = trad.langue
    return id.get(), spinbox_value.get(), trad