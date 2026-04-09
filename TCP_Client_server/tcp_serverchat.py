import socket

HOST = 'localhost'   # Symbolic name meaning all available interfaces
PORT = 8080  # Arbitrary non-privileged port
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))
# Listen for incoming connections (max backlog of 5)
server_socket.listen(5)
print('Server listening on {}:{}'.format(HOST, PORT))
# Wait for a connection
client_socket, client_address = server_socket.accept()
print('Accepted connection from {}:{}'.format(client_address[0],
                                              client_address[1]))
# Receive and send messages from/to the client
while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print('Received message: {}'.format(data))
        # Send a response to the client
    response = input('Enter a response: ')
    client_socket.sendall(response.encode())
# Close the connection
print('Closing connection')
client_socket.close()
