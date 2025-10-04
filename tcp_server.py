import socket  # Import the socket module for working with network connections

def server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind it to an address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Start listening for incoming connections (maximum 5 in queue)
    server_socket.listen(5)
    print("Server started and waiting for connections...")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print(f"Message received: {data}")

        # Send a response to the client
        response = f"Server received: {data}"
        client_socket.send(response.encode())

        # Close the connection with the client
        client_socket.close()

if __name__ == '__main__':
    server()