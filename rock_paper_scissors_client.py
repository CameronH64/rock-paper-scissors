# Cameron Holbrook
# UCA ID: B01257833

import socket

# -------------------------- CLIENT-SIDE SETUP --------------------------

HEADER = 64                             # Header size
PORT = 5050                             # Port number to use the socket on.
FORMAT = 'utf-8'                        # Format to encode data in.
DISCONNECT_MESSAGE = "DISCONNECT"                           # The message needed to disconnect from the server.
SERVER = input('Enter the server\'s IP address: ')          # Empty for now because I'm not  for now. Needs to contain the IP Address of the server.
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# -------------------------- CLIENT-SIDE --------------------------

# Send a message to the server.
def send(message):
    message = message.encode(FORMAT)                        # Encode the string in utf-8 format.
    msg_length = len(message)                           # Get the message length
    send_length = str(msg_length).encode(FORMAT)        # Make the send length using the msg length and the encode format.
    send_length += b' ' * (HEADER - len(send_length))   # Then, add a buffer to the rest of the send length.

    client.send(send_length)                            # Send to the server the send_length.
    client.send(message)                                # Send to the server the actual message.

    print(client.recv(2048).decode(FORMAT))





send("Hello World!")
input()
send("Hey, listen!")

send(DISCONNECT_MESSAGE)
