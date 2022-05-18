from Logic import Client


class Server:

    def __init__(self):
        self.clients = []
        self.chat_string = ""

    def add_client(self, client):
        self.clients.append(client)
        self.notify_about_new_client(client)

    def notify_about_new_client(self, client):
        notification = " \n {} joins the server"
        self.chat_string += notification.format(client.name)
        self.update_clients(notification.format(client.name))

    def receive_message(self, client: Client, message):
        new_message = "\n {} : {}"
        self.chat_string += new_message.format(client.name, message)
        self.update_clients(new_message.format(client.name, message))

    def update_clients(self, message):
        for client in self.clients:
            client.update_chat(message)

    def remove_client(self, client):
        self.clients.remove(client)
        notification = " \n {} disconnects from the server"
        self.chat_string += notification.format(client.name)
        self.update_clients(notification.format(client.name))




