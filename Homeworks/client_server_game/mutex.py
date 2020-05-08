# This is a really simple version of dealing with a critical 
# section. The server and only the server will create an object
# of this class. The server will then look at the condition of the
# key boolean in this object and allow a client to guess if it is
# true. The value will then be changed to false to prevent other
# clients from guessing until the current client is finished.
class mutex():
    def __init__(self):
        self.key = True
        self.winner = False

    def getkey(self):
        return self.key

    def falsekey(self):
        self.key = False

    def returnkey(self):
        self.key = True

# This class will be used to stop the other clients once a winner
# has been found.
class win():
    def __init__(self):
        self.winner = False
        self.client = ""

    def winnerfound(self, name):
        self.winner = True
        self.client = name
