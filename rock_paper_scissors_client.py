# Cameron Holbrook
# UCA ID: B01257833

import socket

class Client:


    # -------------------------- CLIENT-SIDE SETUP --------------------------

    def __init__(self):

        # Set basic variables.
        self.HEADER = 64                             # Header size
        self.PORT = 5050                             # Port number to use the socket on.
        self.FORMAT = 'utf-8'                        # Format to encode data in.
        self.DISCONNECT_MESSAGE = "DISCONNECT"                           # The message needed to disconnect from the server.

        # self.SERVER = input('Enter the server\'s IP address: ')          # Empty for now because I'm not  for now. Needs to contain the IP Address of the server.
        self.ADDR = None
        self.client = None

    # -------------------------- CLIENT-SIDE --------------------------

    def setup_client(self, ip_address):
        self.ADDR = (ip_address, self.PORT)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    # Send a message to the server.
    def send(self, message):
        message = message.encode(self.FORMAT)                        # Encode the string in utf-8 format.
        msg_length = len(message)                           # Get the message length
        send_length = str(msg_length).encode(self.FORMAT)        # Make the send length using the msg length and the encode format.
        send_length += b' ' * (self.HEADER - len(send_length))   # Then, add a buffer to the rest of the send length.

        self.client.send(send_length)                            # Send to the server the send_length.
        self.client.send(message)                                # Send to the server the actual message.

        print(self.client.recv(2048).decode(self.FORMAT))

