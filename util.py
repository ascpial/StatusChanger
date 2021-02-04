import sys

def application_path():
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path="."
    return application_path