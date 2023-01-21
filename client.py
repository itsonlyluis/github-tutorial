import socket
import threading

# Where to open this socket
_HOST = "127.0.0.1"
_PORT = 4000

# Try to connect to the server
server = socket.socket()
x = server.connect((_HOST, _PORT))
print("Connected to socket server")



# Function which will continually listen for any inputs from the user, and forward them to the server
# This will be run in a separate thread in the background, so it doesn't block the listener below
def inputThread():
    global server
    while True:
        msg = input()
        server.send(msg.encode())

# Create and start a thread for that function
# Marks the thread as a daemon so it exits with the main program, just for this tutorial
# There's good reasons why this isn't always the best solution. If you're going to be using threads, Google why this is the case
_listenThread = threading.Thread(target = inputThread, daemon = True)
_listenThread.start()



# Continually listen for any messages from the server
while True:
    data = server.recv(1024).decode()

    # If the connection is lost, close the socket, and exit the program
    if(len(data) == 0):
        print("Connection lost...")
        server.close()
        exit()

    # Print out anything we receive from the server
    print("> {}".format(data))