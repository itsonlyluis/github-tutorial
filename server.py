import socket
from datetime import datetime

# Where to open this socket
_HOST = "127.0.0.1"
_PORT = 3000

# Bind the socket
server = socket.socket()
server.bind((_HOST, _PORT))

# Allow 1 client to connect to the socket, printing to console once a connection has been made
while True:
    server.listen(1)
    print("Awaiting connection...")
    client, address = server.accept()
    print("Client connected " + str(address))

    # Continually listen for messages
    while True:
        data = client.recv(1024).decode()

        # If the connection has lost, close the socket, and break out of the loop so something else can (re)connect
        if not data:
            client.close()
            break
        
        # Decode the message we've received, and print it out on the server console so we can see what's happening
        msg = str(data)
        print(msg)

        # If the client asked for the date, send them it
        if(msg == "date"):
            client.send(datetime.now().isoformat().encode())

        # For test pings, echo back whatever was sent
        elif(msg.startswith("ping ")):
            client.send(msg.replace("ping ", "").encode())
        
        # Close the connection with them if they ask for that
        elif(msg == "exit"):
            client.close()
            break