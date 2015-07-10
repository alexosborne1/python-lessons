# Jake Malley
# 05/02/15
# Tested for Python 2.7

"""
Message server
"""

# Import the socket module.
import socket

# Create the socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Define the host and the port.
host = '127.0.0.1'
port = 8005

# Bind to that host/port.
sock.bind((host,port))

try:
    # Listen
    sock.listen(5) # Queue of 5 clients.

    while True:
        # Forever do:
        print("Waiting for new connection... (Ctrl-c to exit)")
        client, address = sock.accept()

        # Once someone has connected.
        print('Someone has connected from %s port %s' %(address[0],address[1]))

        while True:
            # We are waiting for the client to send a message.
            print('\nWaiting for a message from %s' %(address[0]))

            # Wait for the client to send us a message.
            incoming_message = client.recv(1024)

            # Print out the message.
            print("Message = %s" %(incoming_message))

            # Send them a reply.
            print("Enter your reply or type 'END' to close the connection.")
            outgoing_message = raw_input(">")
            client.send(outgoing_message)

            if outgoing_message.upper() == "END":
                print("Disconnected...")
                # Close the connection.
                client.close() 
                break


# If someone pressed ctrl-c    
except KeyboardInterrupt:
    print('Closing...')

except socket.error:
    print("The server encountered an error.")

finally:
    # Close everything.
    client.close()
    sock.close()


    



