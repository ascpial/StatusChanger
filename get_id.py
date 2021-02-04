from tkinter import *
import webbrowser
from util import application_path
from traduction import Traduction
import os
from tkinter.messagebox import showerror
import sys

class GetId(Tk):
    def __init__(self, config):
        self.config = config
        Tk.__init__(self)
        self.iconbitmap(os.path.join(application_path(), "StatusChanger.ico"))
        self.title("StatusChanger")
        self.geometry("300x400")
        self.trad = Traduction()
        self.load_id_page()
    def mainloop(self):
        self.protocol("WM_DELETE_WINDOW", self.close_application)
        Tk.mainloop(self)
        self.config["values"]["application_id"] = self.id.get()
        self.config["values"]["pipe"]           = self.spinbox_value.get()
        self.config["values"]["langue"]         = self.trad.langue
        return self.id.get(), self.spinbox_value.get(), self.trad
    def load_id_page(self):
        try:
            self.trad.load_id_page(self, self.config["values"]["langue"])
        except KeyError:
            self.trad.load_id_page(self, "en")
        label = Label(self, textvariable=self.trad["application_here"])
        label.pack()
        self.id = StringVar()
        try:
            self.id.set(self.config["values"]["application_id"])
        except KeyError: pass
        text = Entry(self, textvariable=self.id)
        text.pack()
        bouton = Button(self, textvariable=self.trad["continue"], command=self.check, width=20)
        bouton.pack()
        self.spinbox_value = StringVar()
        try:
            self.spinbox_value.set(self.config["values"]["pipe"])
        except KeyError: pass
        spinbox = Spinbox(self, from_=0, to=9,increment=1, textvariable=self.spinbox_value)
        spinbox.pack()
        Button(self, textvariable=self.trad["get_id"], command=self.open_id_page).pack(side=BOTTOM)
        langue_frame = Frame(self)
        fr = PhotoImage(file=os.path.join(application_path(), "flag_fr.png"))
        self.fr = fr.subsample(11, 11)
        bouton = Button(langue_frame, image=self.fr, command=self.set_fr)
        bouton.pack(side="right")
        gb = PhotoImage(file=os.path.join(application_path(), "flag_gb.png"))
        self.gb = gb.subsample(11, 11)
        Button(langue_frame, image=self.gb, command=self.set_en).pack(side="right")
        langue_frame.pack(side=BOTTOM)
    def open_id_page(self):
        webbrowser.open("https://discord.com/developers/applications")
    def close_application(self):
        sys.exit(0)
    def check(self):
        if self.id.get().isdigit():
            self.destroy()
        else:
            showerror(self.trad["invalide_id_title"].get(), self.trad["invalide_id_content"].get())
    def set_en(self):
        self.trad.set_id_page("en")
    def set_fr(self):
        self.trad.set_id_page("fr")