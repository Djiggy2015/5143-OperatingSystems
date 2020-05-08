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
    while guess != -1 and guess != 2:
        msg = "lock"
        message = msg.encode(FORMAT)
 
        client.send(message)
        status = client.recv(2048).decode(FORMAT)

        if status == "y":
            num = send(guess, num)
            guess = randguess(guess, num)
        
        else:
            print("Waiting...")


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
