# Python3.7+
import socket
#socket.AF_INET, socket.SOCK_STREAM

HOST, PORT = '', 8888

listen_socket = socket.socket( )
# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')
print('Access http://localhost:8888')
while True:
    client_connection, client_address = listen_socket.accept()
    print('connected with',client_address)
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

<h1 style="color:red;text-align: center;">Hello, World!<h1>
<h3> Our server is working <h3>
"""
    client_connection.sendall(http_response)
    
    client_connection.close()
  
