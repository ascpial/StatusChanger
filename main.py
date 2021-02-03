from tkinter import *
from tkinter.messagebox import *
from pypresence import Client
import os
import sys
import pathlib
import settings
import webbrowser

class RPC_tk(Tk):
    def __init__(self, RPC, id, pipe):
        self.RPC = RPC
        Tk.__init__(self)
        color = "#36393f"
        self.config = settings.Settings(get_config_file(), self)
        self.iconbitmap(os.path.join(application_path, "StatusChanger.ico"))
        self.title(f"StatusChanger (pipe {pipe})")
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
        self.send = Button(self, text="Envoyer", command=self.update)
        self.send.pack()
        self.clear = Button(self, text="Clear", command=self.clear)
        self.clear.pack()
        #self.after(1000, self.update_timer)
        self.mainloop()
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
        self.config.save()
    def clear(self):
        self.RPC.clear_activity(os.getpid())
    """
    def update_timer(self):
        self.RPC.register_event("ACTIVITY_JOIN", self.join_party)
        self.after(1000, self.update_timer)
    def join_party(self, values):
        print(values)
        secret = values["secret"]
        showinfo("Rejoindre une partie", f"Vous avez rejoint la partie {secret}")"""
def get_config_file():
    home = pathlib.Path.home()
    if sys.platform == "win32":
        return home / "AppData/Roaming/.StatusChanger.json"
    elif sys.platform == "linux":
        return home / ".local/share/.StatusChanger.json"
    elif sys.platform == "darwin":
        return home / "Library/Application Support/.StatusChanger.json"
def get_id():
    def open_doc():
        webbrowser.open("https://discord.com/developers/applications")
    saving = os.path.join(os.path.expanduser('~'), ".presencechanger.json")
    with open(saving, 'w') as file:
        file.write("Helloworld!")
    root = Tk()
    root.iconbitmap(os.path.join(application_path, "StatusChanger.ico"))
    root.title("StatusChanger")
    root.geometry("300x400")
    label = Label(root, text="ID de votre application :")
    label.pack()
    id = StringVar()
    text = Entry(root, textvariable=id)
    text.pack()
    def check():
        if id.get().isdigit():
            root.destroy()
        else:
            showerror("ID invalide", "L'ID d'application doit être un nombre")
    bouton = Button(root, text="Continuer", command=check, width=20)
    bouton.pack()
    spinbox_value = StringVar()
    spinbox = Spinbox(root, from_=0, to=9,increment=1, textvariable=spinbox_value)
    spinbox.pack()
    Button(root, text="Get your ID", command=open_doc).pack()
    lang_frame = Frame(root)
    lang_frame.pack(side=BOTTOM)
    root.mainloop()
    return id.get(), spinbox_value.get()
class Saisie:
    def __init__(self, root, name, state_name, value_name, config):
        self.config = config
        if not (state_name in config and value_name in config):
            config[state_name] = IntVar()
            config[value_name] = StringVar()
        self.state = config[state_name]
        self.value = config[value_name]
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
        if not (state_name in config and value2_name in config and value2_name in config):
            config[state_name] = IntVar()
            config[value1_name] = StringVar()
            config[value2_name] = StringVar()
        self.state = config[state_name]
        self.value1 = config[value1_name]
        self.value2 = config[value2_name]
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
        if not (state_name in config and value_name in config):
            config[state_name] = IntVar()
            config[value_name] = IntVar()
        self.state = config[state_name]
        self.value = config[value_name]
        self.name = name
        self.root = root
        self.state = IntVar()
        self.state.set(0)
        self.frame = Frame(root)
        Checkbutton(self.frame, text=self.name, variable=self.state).grid(row=0,column=0)
        self.value = StringVar()
        Entry(self.frame, textvariable=self.value).grid(row=0,column=1)
        self.frame.pack()
    def get(self):
        if self.state.get() == 1:
            try:
                if self.value.get() == "":
                    self.state.set(0)
                    return None
                else:
                    return int(self.value.get())
            except ValueError:
                self.state.set(0)
                return None
        else:
            return None

if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path="."
    id, pipe = get_id()
    if not id == 0:
        RPC = Client(id, pipe=pipe)
        RPC.start()
        rpc_tk = RPC_tk(RPC, id, pipe)