import json
import os
from tkinter import StringVar, IntVar

class Settings(dict):
    def __init__(self, filename, root):
        self.root = root
        dict.__init__(self)
        self.filename = filename
        try:
            if not os.path.exists(os.path.dirname(self.filename)):
                os.mkdir(os.path.dirname(self.filename))
            if not os.path.exists(self.filename):
                with open(self.filename, 'w') as file:
                    file.write(json.dumps(self, indent=4))
            with open(self.filename, 'r') as file:
                self.input = json.load(file)
            for key, value in self.input.items():
                if type(value) == int:
                    self[key] = IntVar(root)
                    self[key].set(value)
                elif type(value) == str:
                    self[key] = StringVar(root)
                    self[key].set(value)
            self.can_write = True
        except ImportError:
            self.values = {}
            self.can_write = False
    def save(self):
        if self.can_write:
            output = {}
            for key, value in self.items():
                output[key] = value.get()
            with open(self.filename, 'w') as file:
                file.write(json.dumps(output, indent=4))
    