# Cameron Holbrook
# UCA ID: B01257833

import socket
import threading

class Server:
    # -------------------------- SERVER-SIDE SETUP --------------------------
    def __init__(self):

        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())  # Will get the IP Address of this computer. If a VPN is used, will use that IP address instead.
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "DISCONNECT"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        # print("[STARTING] server is starting...")
        # start_server()



    # -------------------------- SERVER-SIDE --------------------------

    # def setup_server(self):



    def handle_client(self, connection, address):
        print(f"[SERVER] NEW CONNECTION: {address} CONNECTED.")

        connected = True
        while connected:
            message_length = connection.recv(self.HEADER).decode(self.FORMAT)
            if message_length:
                message_length = int(message_length)
                msg = connection.recv(message_length).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:       # If the server receives the disconnect message, disconnect the client.
                    connected = False

                print(f"[{address}] {msg}")         # Debugging
                connection.send("Message received.".encode(self.FORMAT))

        connection.close()


    # -------------------------- SERVER SETUP --------------------------

    def start_server(self):
        self.server.listen()
        print(f"[LISTENING] SERVER IS LISTENING ON: {self.SERVER}")

        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
