from Logic import Client
from tkinter import *
import random


class ClientWindow:
    clientWindows = []

    def __init__(self, client, server):
        self.server = server
        self.client = client
        self.window = Tk()
        self.window.title(client.name)
        Label(self.window, text="chat", ).grid(row=0, column=0)
        self.chat_box = Text(self.window, bd="3")
        self.chat_box.grid(row=1, column=0)
        Label(self.window, text="send message", ).grid(row=2, column=0)
        self.client_message = Entry(self.window, width=200, bd="3")
        self.client_message.grid(row=3, column=0)
        Button(self.window, text="Submit", command=self.send_massage).grid(row=3, column=1)
        self.window.protocol('WM_DELETE_WINDOW', self.close_client)
        Label(self.window, text=self.client.client_lag_to_server(), ).grid(row=0, column=1)

    def send_massage(self):
        new_massage = self.client_message.get()
        self.server.receive_message(self.client, new_massage)
        ClientWindow.update_all_clients()

    def update_text(self):
        self.chat_box.delete(0.0, END)
        self.chat_box.insert(0.0, self.client.chat)

    def close_client(self):
        ClientWindow.clientWindows.remove(self)
        self.server.remove_client(self.client)
        ClientWindow.update_all_clients()
        self.window.destroy()

    @staticmethod
    def update_all_clients():
        for client in ClientWindow.clientWindows:
            client.update_text()
