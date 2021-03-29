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
        self["change"]=StringVar(root)
        self["error"]=StringVar(root)
        self.set_page()
    def set_page(self, langue=None):
        if langue:
            self.langue = langue
        if self.langue=="fr":
            self["send"].set("Appliquer")
            self["clear"].set("Effacer")
            self["save"].set("Sauvegarder")
            self["change"].set("Changer")
            self["error"].set("Erreur")
        elif self.langue=="en":
            self["send"].set("Apply")
            self["clear"].set("Clear")
            self["save"].set("Save")
            self["change"].set("Change")
            self["error"].set("Error")
    def load_date_input(self, root, langue=None):
        if langue:
            self.langue = langue
        self["date"]=StringVar(root)
        self["hour"]=StringVar(root)
        self["day_n"]=int
        self["month_n"]=int
        self["set"]=StringVar(root)
        self["cancel"]=StringVar(root)
        self["invalide date"]=StringVar(root)
    def set_date_input(self, langue=None):
        if langue:
            self.langue = langue
        if self.langue=="fr":
            self["date"].set("Date")
            self["hour"].set("Heure")
            self["day_n"]   = 0
            self["month_n"] = 2
            self["set"].set("Changer")
            self["cancel"].set("Annuler")
            self["invalide date"].set("La date saisie est invalide")
        elif self.langue=="en":
            self["date"].set("Date")
            self["hour"].set("Hour")
            self["day_n"]   = 2
            self["month_n"] = 0
            self["set"].set("Set")
            self["cancel"].set("Cancel")
            self["invalide date"].set("The date is invalide")