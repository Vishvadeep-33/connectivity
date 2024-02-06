import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
server_address = ('localhost',12345)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    print("Waiting for connection")
    connection, client_address = server_socket.accept()
    try:
        print('connection for client' , client_address)
        data = connection.recv(1024)
        print('recived ',data.decode())
        connection.sendall(b'hello world')
        
    finally:
        connection.close()