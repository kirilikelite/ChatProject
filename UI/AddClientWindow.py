from tkinter import *
from Logic import Client
from UI import ClientWindow


class AddClientWindow:
    isAlreadyOpen = False

    def __init__(self, server):
        AddClientWindow.isAlreadyOpen = True
        self.server = server
        self.window = Tk()
        self.window.title("AddClient")
        Label(self.window, text="addClient", ).grid(row=0, column=0)
        self.client_name = Entry(self.window, width=20, bd="3")
        self.client_name.grid(row=1, column=0)
        Button(self.window, text="add client", command=self.add_client).grid(row=1, column=1)
        self.window.protocol('WM_DELETE_WINDOW', self.close_window)

    def add_client(self):
        client_name = self.client_name.get()
        new_client = Client.Client(self.server, client_name)
        self.server.add_client(new_client)
        new_client_window = ClientWindow.ClientWindow(new_client, self.server)
        ClientWindow.ClientWindow.clientWindows.append(new_client_window)
        self.window.destroy()
        AddClientWindow.isAlreadyOpen = False
        ClientWindow.ClientWindow.update_all_clients()

    def close_window(self):
        AddClientWindow.isAlreadyOpen = False
        self.window.destroy()
