from tkinter import *
from tkinter.messagebox import *
from pypresence import Client, exceptions
import os
import sys
import pathlib
import settings
import webbrowser
from traduction import Traduction
from get_id import get_id
from util import application_path

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
        self.start = SaisieInt(self, "Start : ", "start_state", "start_value", self.config)
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
    def update(self):
        buttons = []
        for bouton in (self.bouton1, self.bouton2):
            if bouton.get() != None:
                buttons.append({"label":bouton.get()[0],"url":bouton.get()[1]})
        if len(buttons) == 0:
            buttons = None
        party_size = [self.number_players.get(), self.party_size.get()]
        if party_size == [None, None]:
            party_size=None
        self.RPC.set_activity(pid=os.getpid(), state=self.state.get(), details=self.details.get(),
                        large_image=self.large_image_key.get(), large_text = self.large_image_text.get(),
                        small_image = self.small_image_key.get(), small_text=self.small_image_text.get(),
                        start=self.start.get(), end=self.end.get(),
                        buttons=buttons, party_size=party_size,
                        party_id=self.party_id.get(),join=self.join.get())
        self.save()
    def clear(self):
        self.RPC.clear_activity(os.getpid())
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
    id, pipe, trad = get_id(config = configuration)
    if not id == 0:
        try:
            RPC = Client(id, pipe=pipe)
            RPC.start()
        except exceptions.InvalidPipe:
            pass
        rpc_tk = RPC_tk(RPC, id, configuration, trad, pipe)