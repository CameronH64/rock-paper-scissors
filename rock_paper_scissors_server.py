# Cameron Holbrook
# UCA ID: B01257833

import socket
import threading
from tkinter import *

# -------------------------- SERVER SETUP --------------------------

# Starts the server, taking in the
def start_server(server_ip, port_number):

    # Server variable setup.
    server_running = True
    client_list = []

    # Instantiate the server.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port_number))

    server.listen()
    print(f"[LISTENING] SERVER IS LISTENING ON: {server_ip}")

    while server_running:
        client_connection, addr = server.accept()                                            # Accept any and all new client socket connections.

        client_list.append(client_connection)

        thread = threading.Thread(target=handle_client, args=(client_connection, addr))      # Pass the handle_client function to a thread so that the thread the can do it.
        thread.start()                                                                       # Start that thread.

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")           # Server-side debugging for printing the number of active socket connections.



def handle_client(client_connection, address):
    print(f"[SERVER] NEW CONNECTION: {address} CONNECTED.")

    server_running = True
    action_counter = 0

    while server_running:

        message = client_connection.recv(64).decode('utf-8')

        if message:

            # If statement that will deal with input data
            if message == 'exit':       # If the server receives the disconnect message, disconnect the client.
                server_running = False
            elif message == 'rock':
                print('[SERVER] RECEIVED ROCK')
                action_counter += 1
            elif message == 'paper':
                print('[SERVER] RECEIVED PAPER')
                action_counter += 1
            elif message == 'scissors':
                print('[SERVER] RECEIVED SCISSORS')
                action_counter += 1

            # After client information is received, check if enough data to make a game judgment.
            if action_counter == 1:
                print('ROUND 1')
            if action_counter == 3:
                print('ROUND 2')
            if action_counter == 5:
                print('ROUND 3')

            # Debugging
            print(f"[{address}] {message}")
            client_connection.send(f"Message received: {message}".encode('utf-8'))
    #
    # client_connection.close_everything()



# ------------------- RUNNING CODE -----------------------

# Start the server thread. Is run whenever the "Start Server" button is pressed.
def start_start_server_thread(server_textarea):

    # Variable setup for the server.
    PORT = 5050
    server_ip = socket.gethostbyname(socket.gethostname())             # Will get the IP Address of this computer. If a VPN is used, will use that IP address instead.

    # Run the server_thread method
    threading.Thread(target=start_server, args=(server_ip, PORT)).start()

    # Run the handle_client method.
    threading.Thread(target=handle_client, args=())

    # Show that the server is started on the GUI.
    server_textarea.insert(INSERT, 'Server started.\n')



# ------------------------ CREATE SERVER GUI STUFF ------------------------

def close_everything():
    root.destroy()


# Create the server GUI

root = Tk()
root.title('Server GUI')
# root.geometry('200x400')

# Instantiate components
server_log_label = Label(root, text='Server Log')
server_textarea = Text(root, height=20, width=40)
start_server_button = Button(root, text='Start Server', command=lambda: start_start_server_thread(server_textarea))
exit_program_button = Button(root, text='Exit', command=close_everything)

# Place components on window
server_log_label.grid(row=0, column=0)
server_textarea.grid(row=1, column=0)
start_server_button.grid(row=2, column=0)
exit_program_button.grid(row=3, column=0)

# Show the GUI
root.mainloop()



