# Cameron Holbrook
# UCA ID: B01257833

import socket
import threading

# -------------------------- SERVER-SIDE --------------------------

def handle_client(connection, address):
    print(f"[SERVER] NEW CONNECTION: {address} CONNECTED.")

    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            msg = connection.recv(message_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:       # If the server receives the disconnect message, disconnect the client.
                connected = False

            print(f"[{address}] {msg}")         # Debugging
            connection.send("Message received.".encode(FORMAT))

    connection.close()


# -------------------------- SERVER SETUP --------------------------

def start_server():
    server.listen()
    print(f"[LISTENING] SERVER IS LISTENING ON: {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")




if __name__ == '__main__':

    # -------------------------- SERVER-SIDE SETUP --------------------------

    HEADER = 64
    PORT = 5050
    SERVER = socket.gethostbyname(
        socket.gethostname())  # Will get the IP Address of this computer. If a VPN is used, will use that IP address instead.
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "DISCONNECT"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    print("[STARTING] server is starting...")
    start_server()
