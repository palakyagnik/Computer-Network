import socket

HOST = 'localhost' # The server's hostname or IP address
PORT = 8080       # The port used by the server
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#You can see that family=socket.AF_INET defines the address family that this 
#socket can accept – only IPv4 addresses.
#And type=socket.SOCK_STREAM defines that the socket accepts only TCP 
#(Transmission Control Protocol) connections.

# Connect to the server
client_socket.connect((HOST, PORT))
print('Connected to {}:{}'.format(HOST, PORT))

# Send and receive messages from the server
while True:
    # Send a message to the server
    message = input('Enter a message: ')
    client_socket.sendall(message.encode())
        # Receive a response from the server
    data = client_socket.recv(1024).decode()
    print('Received response: {}'.format(data))
# Close the connection
print('Closing connection')
client_socket.close()