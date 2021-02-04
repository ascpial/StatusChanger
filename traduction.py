from tkinter import StringVar

class Traduction(dict):
    def __init__(self):
        dict.__init__(self)
    def load_id_page(self, root, langue):
        self.langue = langue
        if langue=="fr":
            self["application_here"]=StringVar(root)
            self["invalide_id_title"]=StringVar(root)
            self["application_id_content"] = StringVar(root)
            self["continue"] = StringVar(root)
            self["get_id"] = StringVar(root)
            self.set_id_page("fr")
        elif langue=="en":
            self["application_here"]=StringVar(root)
            self["invalide_id_title"]=StringVar(root, "Invalide ID")
            self["application_id_content"] = StringVar(root)
            self["continue"] = StringVar(root)
            self["get_id"] = StringVar(root)
            self.set_id_page("en")
    def set_id_page(self, langue=None):
        if langue:
            self.langue = langue
        if self.langue == "fr":
            self["application_here"].set("Votre ID d'application :")
            self["invalide_id_title"].set("ID invalide")
            self["application_id_content"].set("L'ID d'application doit être un nombre")
            self["continue"].set("Continuer")
            self["get_id"].set("Récupérez votre ID d'application")
        elif langue=="en":
            self["application_here"].set("Your application ID :")
            self["invalide_id_title"].set("Invalide ID")
            self["application_id_content"].set("the application ID must be a number")
            self["continue"].set("Continue")
            self["get_id"].set("Get application ID")
    def load_page(self, root, langue=None):
        if langue:
            self.langue = langue
        self["send"]=StringVar(root)
        self["clear"]=StringVar(root)
        self["save"]=StringVar(root)
        self.set_page()
    def set_page(self, langue=None):
        if langue:
            self.langue = langue
        if self.langue=="fr":
            self["send"].set("Envoyer")
            self["clear"].set("Effacer")
            self["save"].set("Sauvegarder")
        elif self.langue=="en":
            self["send"].set("Send")
            self["clear"].set("Clear")
            self["save"].set("Save")