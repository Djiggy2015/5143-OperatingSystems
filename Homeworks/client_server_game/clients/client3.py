import socket
import time
import sys

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DIS"

# Initial Variables
guess = 1
tens = 1000000000
num = "0"

# Load up the necessary data to connect to the server.
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def access(guess_ten, num):
    while guess_ten[0] != -1:
        msg = "Available?"
        message = msg.encode(FORMAT)
 
        client.send(message)
        status = client.recv(2048).decode(FORMAT)
        print(status)

        # If the server is available, take a guess!
        if status == "y":
            num = send(guess_ten[0], num)
            searchbytens(guess_ten, num)

        # Otherwise, do nothing.
        else:
            print("Waiting...")

# Send the server what you think the number is.
def send(guess, num):
    msg = str(guess)
    message = msg.encode(FORMAT)
    client.send(message)

    num = client.recv(2048).decode(FORMAT)

    return num

# Beginning with the number 1, start by adding 1000000000 until the number
# is too high, then bring it back down. This will tell you the 1^n place
# of the server's number. Continue this process until the number has been 
# found.
def searchbytens(guess_ten, num):
    # If the number is greater, then lower it back down
    # and reduce the power of tens by 1.
    if num == "1":
        guess_ten[0] -= guess_ten[1]
        guess_ten[1] = guess_ten[1] // 10
        print(guess_ten[0])

    # If smaller, just keep increasing the current tens place
    # by one. 
    elif num == "-1":
        guess_ten[0] += guess_ten[1]
        print(guess_ten[0])

    else:
        print("The number is: ", guess)
        guess_ten[0] = -1


guess_ten = [guess, tens]

access(guess_ten, num)
