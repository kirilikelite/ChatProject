from Logic import Server
import random


class Client:
    def __init__(self, server: Server, name):
        self.server = server
        self.chat = ""
        self.name = name
        self.lag = random.randrange(1, 9)

    def update_chat(self, message):
        self.chat += message

    def send_message(self, message):
        self.server.receive_message(self, message)

    def client_lag_to_server(self):
        lag_message = "client lag to the server is {} seconds"
        return lag_message.format(self.lag)
