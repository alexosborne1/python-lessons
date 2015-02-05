# Jake Malley
# 05/02/15
# Tested for Python 2.7

"""
Message client
"""

# Import the socket module.
import socket

# Create the socket object
sock = socket.socket()

# Define the host and the port.
host = '127.0.0.1'
port = 8005

# Connect to the server.
sock.connect((host, port))
print("Connected to the server:")

while True:
    print("Enter a message to send to the server.")
    outgoing_message = raw_input("> ")
    # Send the message to the server.
    sock.send(outgoing_message)

    print("Waiting for a reply from the server.")
    # Wait for the server's reply.
    incoming_message = sock.recv(1024)
    # Print out the message.
    print("Message = %s" %(incoming_message))

    # If the server ended the connection
    if incoming_message.upper()=='END':
        print("Server disconnected.")
        break

# Close the connection.
sock.close() 