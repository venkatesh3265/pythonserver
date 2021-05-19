# Python web server
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket( )
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')
print('Access http://localhost:8888')
while True:
    client_connection, client_address = listen_socket.accept()
    print('connected with',client_address)
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))


    http_response = 'HTTP/1.0 200 OK\n\n<h1 style="color:red;">Hello World<h1> \n<h1> our server is working </h1>'
    client_connection.sendall(http_response.encode())
    
    client_connection.close()
  
