from UI import AddClientWindow
from tkinter import *


class ServerWindow:
    def __init__(self, server):
        self.server = server
        self.window = Tk()
        self.window.title("Server")
        Button(self.window, text="add client", command=self.add_client).grid(row=1, column=1)

    def add_client(self):
        if not AddClientWindow.AddClientWindow.isAlreadyOpen:
            AddClientWindow.AddClientWindow(self.server)
        AddClientWindow.isAlreadyOpen = True

