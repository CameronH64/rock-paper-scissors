# Cameron Holbrook
# UCA ID: B01257833
import tkinter
from tkinter import *
import socket
import threading


# -------------------------- CLIENT-SIDE --------------------------

def setup_client(ip_address, port_number):
    connection_information = (ip_address, port_number)              # Create a tuple that has the IP address and port number to connect to the server.

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Create the client socket.
    client.connect(connection_information)                          # Connect this socket with the information above.

    return client

# Send a message to the server.
def send(message, client):

    message = message.encode('utf-8')                        # Encode the string in utf-8 format.
    client.send(message)                                # Send to the server the actual message.



def handle_message_from_server(address, PORT):
    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = (address, PORT)
    sock.connect(server_address)

    try:
        # Receive data from the server.
        data = sock.recv(1024)              # Blocks the code.
        return data.decode('utf-8')
    finally:
        # close the socket
        sock.close()


def start_client_setup_thread(server_address_textfield):

    ip_address = server_address_textfield.get("1.0", 'end-1c')

    client = setup_client(ip_address, 5050)
    # send('message', client)



threading.Thread(target=setup_client, args=())



# ------------------------ CREATE CLIENT GUI STUFF ------------------------

root = Tk()

server_address_label = Label(root, text='Server Address')
server_address_textfield = Text(root, height=1, width=20)
connect_button = Button(root, text='Connect', command=lambda: start_client_setup_thread(server_address_textfield))
connection_status = Label(root, text='Disconnected')

# rock_photo = tkinter.PhotoImage(file='assets/rock.jpg')
# rock_label = Label(root, image=rock_photo)

server_address_label.grid(row=0, column=0)
server_address_textfield.grid(row=0, column=1)
connect_button.grid(row=1, column=0)
connection_status.grid(row=2, column=0)

# rock_label.grid(row=3, column=0)

root.mainloop()
