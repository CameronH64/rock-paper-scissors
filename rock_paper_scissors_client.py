# Cameron Holbrook
# UCA ID: B01257833

from tkinter import *
from PIL import Image, ImageTk
import socket
import threading


# -------------------------- CLIENT-SIDE --------------------------

# Send a message to the server.
def send(message, client):

    message = message.encode('utf-8')                   # Encode the string in utf-8 format.
    client.send(message)                                # Send to the server the actual message.


# For when the server sends the client a message.
def handle_message_from_server(address, PORT):
    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = (address, PORT)
    sock.connect(server_address)

    # Receive data from the server. In a try-catch because it could fail.
    data = sock.recv(1024)              # Blocks the code.
    try:
        return data.decode('utf-8')
    finally:
        # close the socket
        sock.close()



# ------------------------- SETUP CLIENT STUFF --------------------------

# Is run for the client to connect to the server.
def setup_client(ip_address, port_number):

    # A global client variable so that it can be accessed anywhere.
    global client

    connection_information = (ip_address, port_number)              # Create a tuple that has the IP address and port number to connect to the server.

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Create the client socket.
    client.connect(connection_information)                          # Connect this socket with the information above.

    return client

# Start the thread. Run whenever the connect button on the client is pressed.
def start_client_setup_thread(server_address_textfield, connection_status):

    # Get the text (the IP address) out of the textarea.
    ip_address = server_address_textfield.get("1.0", 'end-1c')      # Get the text (IP address) out of the textfield.

    # Setup the client using the ip address of the server and port number.
    client = setup_client(ip_address, 5050)
    connection_status.config(text='Connected!')


# ------------------------ CREATE CLIENT GUI STUFF ------------------------

# Instantiate a basic Tkinter window.
root = Tk()
root.geometry('500x800')

# Instantiate GUI components
server_address_label = Label(root, text='Server Address')
server_address_textfield = Text(root, height=1, width=20)
connection_status = Label(root, text='Disconnected')
connect_button = Button(root, text='Connect', command=lambda: start_client_setup_thread(server_address_textfield, connection_status))
client_win_lose = Label(root, text='Win/lose: pending')
client_quit_button = Button(root, text="Quit", command=root.destroy)

# Rock setup
rock_image = Image.open('assets/rock.png')
rock_image_tk = ImageTk.PhotoImage(rock_image)
rock_button = Button(root, image=rock_image_tk, command=lambda: send('rock', client))

# Paper setup
paper_image = Image.open('assets/paper.png')
paper_image_tk = ImageTk.PhotoImage(paper_image)
paper_button = Button(root, image=paper_image_tk, command=lambda: send('paper', client))

# Scissors setup
scissors_image = Image.open('assets/scissors.png')
scissors_image_tk = ImageTk.PhotoImage(scissors_image)
scissors_button = Button(root, image=scissors_image_tk, command=lambda: send('scissors', client))

# Add components to the GUI
server_address_label.grid(row=0, column=0)
server_address_textfield.grid(row=0, column=1)
connect_button.grid(row=1, column=0)
connection_status.grid(row=2, column=0)
client_win_lose.grid(row=3, column=0)
rock_button.grid(row=4, column=0)
paper_button.grid(row=5, column=0)
scissors_button.grid(row=6, column=0)
client_quit_button.grid(row=7, column=0)

# Show the GUI
root.mainloop()
