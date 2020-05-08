Client server game with Critical section implementation

Author: Matt Stanley<br><br>
Date: 5/8/2020<br><br>
How to run: To run this game, first start up the server in a python compiler or the command line. If command line is used,
type python server.py. Once the server is running, you may run the client programs through a different command line window by the 
command: python clientname (No parameters are necessary). If you would like to run multiple clients at once, then open multiple
command line windows and run a different client on each. The client's code will automatically finish once a winner has been found.
However, the server will continue to run and must be stopped manually. <br><br>
Development Platform: This program was developed on a Windows 10 Operating system using Python and the Visual Studio Code 
source code editor with Python support. <br><br>
Known Issues: <br>
1.) The server code will not stop running until manually stopped (closing the terminal). Ideally I should be able to stop it 
through the command line.<br>
2.) The binary search client outclasses all of the other clients in finding the number. The other clients barely have time to run
before it wins. It should be nerfed.<br>
3.) While using a lock variable does create a critical section, it is definitely not the best way to implement one. If a client never
leaves the critical section, or the server does not set the lock variable back to true, then the whole program will 
crash. <br>
