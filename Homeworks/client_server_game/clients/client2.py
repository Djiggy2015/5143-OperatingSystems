# Random add/sub client
import socket
import threading
import random
import time

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'

num = "0"
guess = 0

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def access(guess, num):
    while guess != -1 and num != 2:
        msg = "Available?"
        message = msg.encode(FORMAT)
 
        client.send(message)
        status = client.recv(2048).decode(FORMAT)
        print(status)

        if status == "y":
            num = send(guess, num)
            guess = randguess(guess, num)

        # In case the server sends 2 to this variable
        if status == "2":
            break
        
        else:
            print("Waiting...")

    finalmess = client.recv(64).decode(FORMAT)

    # If this client wins, print out a win message.
    if guess == -1:
        print("YOU WIN!")

    # Else print out the winner's address. (Not a good idea online but this is a local network.)
    else:
        print("YOU LOSE!")
        print(finalmess)


def send(guess, num):
    msg = str(guess)
    message = msg.encode(FORMAT)
    client.send(message)

    num = client.recv(2048).decode(FORMAT)

    return num

# Try to find the number through random addition or subtraction. 
# It's definitely not the most efficient method, but who knows? Maybe
# it will get lucky.
def randguess(guess, num):
    if num == "1":
       guess -= random.randint(1, 1000)
       print(guess)
    elif num == "-1":
        guess += random.randint(1, 1000)
        print(guess)
    elif num == 0:
        print("Number was found!")
        print("It was", guess)
        guess = -1

    return guess

access(guess, num)
