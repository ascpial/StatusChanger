import json
import os
from tkinter import StringVar, IntVar

class Settings(dict):
    can_write = False
    def __init__(self, filename, root=None):
        self.root = root
        dict.__init__(self)
        self.filename = filename
        try:
            if not os.path.exists(os.path.dirname(self.filename)):
                os.mkdir(os.path.dirname(self.filename))
            if not os.path.exists(self.filename):
                self["values"] = {}
                self["tk"]     = {}
                with open(self.filename, 'w') as file:
                    file.write(json.dumps(self, indent=4))
            with open(self.filename, 'r') as file:
                self.input = json.load(file)
            self["values"] = self.input["values"]
            self["tk"] = {}
        except ImportError:
            self.values = {"values":{}, "tk":{}}
    def get_tk(self, root=None):
        if root:
            self.root = root
        for key, value in self.input["tk"].items():
            if type(value) == int:
                self["tk"][key] = IntVar(root)
                self["tk"][key].set(value)
            elif type(value) == str:
                self["tk"][key] = StringVar(root)
                self["tk"][key].set(value)
        self.can_write = True
    def save(self):
        if self.can_write:
            output = {"values":self["values"],
                      "tk":{}}
            for key, value in self["tk"].items():
                output["tk"][key] = value.get()
            with open(self.filename, 'w') as file:
                file.write(json.dumps(output, indent=4))
    