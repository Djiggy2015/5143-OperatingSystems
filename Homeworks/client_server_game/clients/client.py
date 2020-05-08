# Binary Search Client
import socket
import time
import sys

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'

num = "0"

# Numbers that will be used in binary search. Since the range picked
# by server is unknown, we will have to assume the worst case scenario
# 0 to maxint.
high = 2147483647
low = 0
count = 0

# Load up the necessary data to connect to the server.
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Talk to the server and find out if the key is currently available.
# If the server says yes, then try to guess the number. If it is not,
# then just keep trying and print "waiting" to the screen.
def access(data, num):
    while data[0] != -1 and data[0] != 2:
        msg = "Available?"
        message = msg.encode(FORMAT)

        client.send(message)
        status = client.recv(2048).decode(FORMAT)

        if status == "y":
            num = send(data[0], num)
            data = change(data[0], num, data[1], data[2])
        
        else:
            print("Waiting...")

    finalmess = client.recv(64).decode(FORMAT)

    # If this client wins, print out a win message.
    if data[0] == -1:
        print("YOU WIN!")

    # Else print out the winner's address. (Not a good idea online but this is a local network.)
    else:
        print("YOU LOSE!")
        print("The winner was address: ", finalmess)

# Send to the server what you think the number is. This function will
# return either -1, 0, or 1. This value will be used to determine how
# to change your guess during binary search.
def send(guess, num):
    msg = str(guess)
    message = msg.encode(FORMAT)

    client.send(message)
    num = client.recv(2048).decode(FORMAT)

    return num

# This client uses the binary search method to try and find the 
# server's number. It is incredibly fast even with the wide range.
def change(guess, num, high, low):
    # If guess is too high
    if num == "1":
        high = guess - 1
        guess = ((low + high) // 2)
        print(guess)

    # If guess is too low
    elif num == "-1":
        low = guess + 1
        guess = ((low + high) // 2)
        print(guess)
    
    else:
        print("Number was found!")
        print("It was ", guess)
        guess = -1

    return [guess, high, low]

# The first guess will be smack dab in the middle of our range
guess =  2147483647 // 2

# A list has to be used here because python handles assignment 
# differently. If you try to change integers inside a function,
# they will not be changed outside the function, because python
# makes a new variable during assignment. Lists can be changed 
# without affecting a variables assignment.
data = [guess, high, low]

access(data, num)
