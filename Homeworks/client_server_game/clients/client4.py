# Truly random client
import socket
import threading
import random
import time

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DIS"
num = "0"
guess = 0

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def access(guess, num):
    while guess != -1 and num!= 2:
        msg = "Available?"
        message = msg.encode(FORMAT)
 
        client.send(message)
        status = client.recv(2048).decode(FORMAT)
        print(status)

        if status == "y":
            num = send(guess, num)
            guess = truerand(guess, num)

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

# This just completely guesses at random. There is a 1 in 2147483647 chance it will
# get the right number on a guess (assuming it hasn't already guessed that number.)
# It will probably never win, but it's fun to watch and useful for debugging.
def truerand(guess, num):

    # In the odd event the number does match, be sure to end the while loop.
    if num == 0:
        guess = -1
    
    else:
        guess = random.randint(1, 2147483647)

    return guess

access(guess, num)
