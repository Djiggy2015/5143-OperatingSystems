import socket
import threading
import random
import sys
from key import mutex, win

random.random() # Seed the random num generator

# This function will randomly create an upper and low bound for a 
# range of numbers. It will then create a random number within these
# bounds. This will lead to a wildly different number to guess every
# time server is ran.
def createrand():
    # Get the low and high bounds
    low = random.randint(0, 2147483646)
    high = random.randint(low + 1, 2147483647)

    return random.randint(low, high)

# This is an external object that will deal with
# the key
m = mutex()
w = win()

# There are no real members in this class. It is mainly used
# to organize the network information
class network:  
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "D"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try binding the host and port to the socket server
try:
    network.server.bind(network.ADDR)
except socket.error as e:
    print(str(e))

# When a client appears, recieve their message and inform them
# whether the key is available or not.
def handle_client(conn, addr, value):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(64).decode(network.FORMAT)
        if msg == network.DISCONNECT_MESSAGE or w.winner == True:
            connected = False
            conn.send("2".encode(network.FORMAT))
        print(f"[{addr}] {msg}")

        if m.getkey() == True and w.winner == False:
            m.falsekey()
            conn.send("y".encode(network.FORMAT))

            msg = conn.recv(64).decode(network.FORMAT)

            if msg == network.DISCONNECT_MESSAGE or w.winner == True:
                connected = False
                conn.send("2".encode(network.FORMAT))
            print(f"[{addr}] {msg}")

            if int(msg) > value:
                conn.send("1".encode(network.FORMAT))
        
            elif int(msg) < value:
                conn.send("-1".encode(network.FORMAT))
        
            else:
                conn.send("0".encode(network.FORMAT))
                print("A winner has been found!")
                connected = False
                w.winnerfound(addr)

            m.returnkey()



        else:
            conn.send("n".encode(network.FORMAT))
            if w.winner == True:
                conn.send("2".encode(network.FORMAT))

    finalmess = "The winner is " + str(w.client)
    conn.send(finalmess.encode(network.FORMAT))
    conn.close()

# Start up the server and get ready to listen for available
# clients. 
def start(value):
    network.server.listen()
    print(f"[LISTENING] server is listening on {network.SERVER}")
    while True:
        conn, addr = network.server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr, value))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("Server is starting...")
value = createrand()
start(value)
