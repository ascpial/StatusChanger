from tkinter import *
from tkinter.messagebox import *
from pypresence import Client, exceptions
import os
import sys
import pathlib
import settings
import webbrowser
from traduction import Traduction
from get_id import GetId
from util import application_path
from datetime import datetime

class RPC_tk(Tk):
    def __init__(self, RPC, id, config, trad, pipe=0):
        self.RPC = RPC
        self.config = config
        Tk.__init__(self)
        self.config.get_tk(self)
        self.iconbitmap(os.path.join(application_path(), "StatusChanger.ico"))
        self.title(f"StatusChanger (pipe {pipe})")
        self.trad = trad
        self.trad.load_page(self)
        Label(self, text="StatusChanger :").pack()
        self.state = Saisie(self, "State : ", "state_state", "state_value", self.config)
        self.details = Saisie(self, "Details : ", "details_state", "details_value", self.config)
        self.start = SaisieDate(self, "Start : ", "start_state", "start_value", self.config)
        self.end = SaisieInt(self, "End : ", "end_state", "end_value", self.config)
        self.large_image_key = Saisie(self, "Large Image Key : ", "large_key_state", "large_key_value", self.config)
        self.large_image_text = Saisie(self, "Large Image Text : ", "large_text_state", "large_text_value", self.config)
        self.small_image_key = Saisie(self, "Small Image Key : ", "small_key_state", "small_key_value", self.config)
        self.small_image_text = Saisie(self, "Small Image Text : ", "small_text_state", "small_text_value", self.config)
        self.party_size = SaisieInt(self, "Party Size : ", "party_state", "party_value", self.config)
        self.number_players = SaisieInt(self, "Players : ", "number_state", "number_value", self.config)
        self.party_id  = Saisie(self, "Party Id : ", "party_id_state", "party_id_value", self.config)
        self.join = Saisie(self, "Join hash : ", "join_state", "join_value", self.config)
        self.frame = LabelFrame(self, text="Buttons", relief=GROOVE)
        self.bouton1 = DoubleSaisie(self.frame, "Button1 Text :", "Url : ", "bouton1_state", "bouton1_name", "bouton1_url", self.config)
        self.bouton2 = DoubleSaisie(self.frame, "Button2 Text :", "Url : ", "bouton2_state", "bouton2_name", "bouton2_url", self.config)
        self.frame.pack()
        self.buttons = Frame(self)
        self.send = Button(self.buttons, textvariable=self.trad["send"], command=self.update)
        self.send.pack(side=LEFT)
        self.bind("<Return>", self.update)
        self.save_button = Button(self.buttons, textvariable=self.trad["save"], command=self.save)
        self.save_button.pack(side=RIGHT)
        self.clear = Button(self.buttons, textvariable=self.trad["clear"], command=self.clear)
        self.clear.pack(side=BOTTOM)
        self.buttons.pack()
        self.mainloop()
    def save(self):
        self.start.check()
        self.end.check()
        self.party_size.check()
        self.number_players.check()
        self.config.save()
    def update(self, event=None):
        buttons = []
        for bouton in (self.bouton1, self.bouton2):
            if bouton.get() != None:
                buttons.append({"label":bouton.get()[0],"url":bouton.get()[1]})
        if len(buttons) == 0:
            buttons = None
        party_size = [self.number_players.get(), self.party_size.get()]
        if party_size == [None, None]:
            party_size=None
        self.RPC.set_activity(state=self.state.get(), details=self.details.get(),
                        large_image=self.large_image_key.get(), large_text = self.large_image_text.get(),
                        small_image = self.small_image_key.get(), small_text=self.small_image_text.get(),
                        start=self.start.get(), end=self.end.get(),
                        buttons=buttons, party_size=party_size,
                        party_id=self.party_id.get(),join=self.join.get())
        self.save()
    def clear(self):
        self.RPC.clear_activity()
class Saisie:
    def __init__(self, root, name, state_name, value_name, config):
        self.config = config
        if not (state_name in config["tk"] and value_name in config["tk"]):
            config["tk"][state_name] = IntVar()
            config["tk"][value_name] = StringVar()
        self.state = config["tk"][state_name]
        self.value = config["tk"][value_name]
        self.name = name
        self.root = root
        self.frame = Frame(root)
        Checkbutton(self.frame, text=self.name, variable=self.state).grid(row=0,column=0)
        Entry(self.frame, textvariable=self.value).grid(row=0,column=1)
        self.frame.pack()
    def get(self):
        if self.state.get() == 1:
            if self.value.get() == "":
                self.state.set(0)
                return None
            else:
                return self.value.get()
        else:
            return None
class DoubleSaisie:
    def __init__(self, root, text1, text2, state_name, value1_name, value2_name, config):
        self.config = config
        if not (state_name in config["tk"] and value2_name in config["tk"] and value2_name in config["tk"]):
            config["tk"][state_name] = IntVar()
            config["tk"][value1_name] = StringVar()
            config["tk"][value2_name] = StringVar()
        self.state = config["tk"][state_name]
        self.value1 = config["tk"][value1_name]
        self.value2 = config["tk"][value2_name]
        self.root = root
        self.text1 = text1
        self.text2 = text2
        self.frame = Frame(root)
        Checkbutton(self.frame, text=self.text1, variable=self.state).grid(row=0, column=0)
        Entry(self.frame, textvariable=self.value1).grid(row=0,column=1)
        Label(self.frame, text=text2).grid(row=0, column=2)
        Entry(self.frame, textvariable=self.value2).grid(row=0,column=3)
        self.frame.pack()
    def get(self):
        if self.state.get() == 1:
            if self.value1.get()=="" or self.value2.get() == "":
                self.state.set(0)
                return None
            else:
                return (self.value1.get(), self.value2.get())
        else:
            return None
class SaisieInt:
    def __init__(self, root, name, state_name, value_name, config):
        self.config = config
        if not (state_name in config["tk"] and value_name in config["tk"]):
            config["tk"][state_name] = IntVar()
            config["tk"][value_name] = StringVar()
        self.state = config["tk"][state_name]
        self.value = config["tk"][value_name]
        self.name = name
        self.root = Radiobutton
        self.frame = Frame(root)
        Checkbutton(self.frame, text=self.name, variable=self.state).grid(row=0,column=0)
        Entry(self.frame, textvariable=self.value).grid(row=0,column=1)
        self.frame.pack()
    def get(self):
        self.check()
        if self.state.get() == 1:
            return int(self.value.get())
        else:
            return None
    def check(self):
        if not self.value.get().isdigit():
            self.state.set(0)
            self.value.set(0)
class SaisieDate:
    def __init__(self, root, name, state_name, value_name, config):
        self.config = config
        if not (state_name in config["tk"] and value_name in config["tk"]):
            config["tk"][state_name] = IntVar()
            config["tk"][value_name] = StringVar()
        self.state = config["tk"][state_name]
        self.value = config["tk"][value_name]
        self.name = name
        self.root = root
        self.frame = Frame(root)
        Checkbutton(self.frame, text=self.name, variable=self.state).grid(row=0,column=0)
        Entry(self.frame, textvariable=self.value).grid(row=0,column=1)
        Button(self.frame, textvariable=self.root.trad["change"], command=self.update).grid(row=0, column=2)
        self.frame.pack()
    def get(self):
        self.check()
        if self.state.get() == 1:
            return int(self.value.get())
        else:
            return None
    def check(self):
        if not self.value.get().isdigit():
            self.state.set(0)
            self.value.set(0)
    def update(self):
        date = InputDate(self.root, self.value)
class InputDate:
    def __init__(self, root, end_value):
        self.root = root
        self.root.trad.load_date_input(self.root)
        self.root.trad.set_date_input()
        self.top = Toplevel(self.root)
        self.top.grab_set()
        self.year   = IntVar()
        self.month  = IntVar()
        self.day    = IntVar()
        self.hour   = IntVar()
        self.minute = IntVar()
        self.second = IntVar()
        self.end_value = end_value
        if self.end_value.get():
            try:
                self.set(int(self.end_value.get()))
            except ImportError:
                self.set(31532399.0)
        else:
            self.set(31532399.0)
        Label(self.top, textvariable=self.root.trad["date"]).pack()
        self.date = Frame(self.top)
        Spinbox(self.date, from_=1, to=31, width=2, textvariable=self.day).grid(row=0, column=self.root.trad["day_n"])
        Label(self.date, text="/").grid(row=0, column=1)
        Spinbox(self.date, from_=1, to=12, width=2, textvariable=self.month).grid(row=0, column=self.root.trad["month_n"])
        Label(self.date, text="/").grid(row=0, column=3)
        Spinbox(self.date, from_=1970, to=2038, width=4, textvariable=self.year).grid(row=0, column=4)
        self.date.pack()
        Label(self.top, textvariable=self.root.trad["hour"]).pack()
        self.time = Frame(self.top)
        Spinbox(self.time, from_=0, to=23, width=2, textvariable=self.hour).grid(row=0, column=0)
        Label(self.time, text=":").grid(row=0, column=1)
        Spinbox(self.time, from_=0, to=59, width=2, textvariable=self.minute).grid(row=0, column=2)
        Label(self.time, text=":").grid(row=0, column=3)
        Spinbox(self.time, from_=0, to=59, width=2, textvariable=self.second).grid(row=0, column=4)
        self.time.pack()
        Button(self.top, textvariable=self.root.trad["set"], command=self.done).pack()
        Button(self.top, textvariable=self.root.trad["cancel"], command=self.cancel).pack()
    def cancel(self):
        self.top.destroy()
    def done(self):
        if self.get():
            self.end_value.set(self.get())
        else:
            showerror(self.root.trad["error"].get(), self.root.trad["invalide date"].get())
        self.top.destroy()
    def get(self):
        try:
            return int(datetime(year=self.year.get(), month=self.month.get(), day=self.day.get(),
                hour=self.hour.get(), minute=self.minute.get(), second=self.second.get()).timestamp())
        except:
            return None
    def set(self, value):
        time = datetime.fromtimestamp(value)
        self.year.set(time.year)
        self.month.set(time.month)
        self.day.set(time.day)
        self.hour.set(time.hour)
        self.minute.set(time.minute)
        self.second.set(time.second)
        self.value = value

def get_config_file():
    home = pathlib.Path.home()
    if sys.platform == "win32":
        return home / "AppData/Roaming/StatusChanger/.StatusChanger.json"
    elif sys.platform == "linux":
        return home / ".local/share/StatusChanger/.StatusChanger.json"
    elif sys.platform == "darwin":
        return home / "Library/Application Support/StatusChanger/.StatusChanger.json"

if __name__ == "__main__":
    configuration = settings.Settings(get_config_file())
    get_id = GetId(configuration)
    id, pipe, trad = get_id.mainloop()
    if not id == 0:
        try:
            RPC = Client(id, pipe=pipe)
            RPC.start()
        except exceptions.InvalidPipe:
            pass
        rpc_tk = RPC_tk(RPC, id, configuration, trad, pipe)