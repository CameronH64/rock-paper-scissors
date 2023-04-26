# Cameron Holbrook
# UCA ID: B01257833

import socket
import threading

# -------------------------- SERVER-SIDE SETUP --------------------------
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Will get the IP Address of this computer. If a VPN is used, will use that IP address instead.
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "exit"

client_list = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



# -------------------------- SERVER-SIDE --------------------------

def handle_client(connection, address):
    print(f"[SERVER] NEW CONNECTION: {address} CONNECTED.")

    server_running = True

    action_counter = 0

    while server_running:

        message_length = connection.recv(HEADER).decode(FORMAT)

        if connection not in client_list:
            client_list.append(connection)

        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)



            # If statement that will deal with input data
            if message == DISCONNECT_MESSAGE:       # If the server receives the disconnect message, disconnect the client.
                server_running = False
            elif message == 'rock':
                print('[SERVER] RECEIVED ROCK')
                connection.send(f"Message received: {message}".encode(FORMAT))
                action_counter += 1
            elif message == 'paper':
                print('[SERVER] RECEIVED PAPER')
                connection.send(f"Message received: {message}".encode(FORMAT))
                action_counter += 1
            elif message == 'scissors':
                print('[SERVER] RECEIVED SCISSORS')
                connection.send(f"Message received: {message}".encode(FORMAT))
                action_counter += 1


            # After client information is received, check if enough data to make a game judgment.
            if action_counter % 2 == 0:
                print('Do rps comparison')
            elif action_counter % 2 == 1:
                print('Do NOT do rps comparison')


            print(f"[{address}] {message}")         # Debugging
            connection.send(f"Message received: {message}".encode(FORMAT))

    connection.close()


# -------------------------- SERVER SETUP --------------------------

def start_server():
    server.listen()
    print(f"[LISTENING] SERVER IS LISTENING ON: {SERVER}")

    while True:
        conn, addr = server.accept()                                            # Accept any and all new client socket connections.
        thread = threading.Thread(target=handle_client, args=(conn, addr))      # Instantiate a new thread for the new client.

        thread.start()                                                          # Start that thread.
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")           # Debugging for printing the number of active socket connections.



# ------------------- RUNNING CODE -----------------------

start_server()
