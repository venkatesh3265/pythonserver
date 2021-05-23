# Python3.7+
import socket

HOST, PORT = '', 8887

listen_socket = socket.socket()
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port',PORT)
print('Access http://localhost:',PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    print('connected with',client_address)
    request_data = client_connection.recv(1024).decode('utf-8')
    string_list = request_data.split(' ')
    print(string_list)
    method = string_list[0] # First string is a method
    print(method)
    requesting_file = string_list[1] #Second string is request file

    print('client request',requesting_file)
   
    myfile = requesting_file
    print('myfile:',myfile)
    myfile = myfile.lstrip('/')
    if(myfile == ''):
        myfile = 'index.html'

    try:
        file = open(myfile,'rb')
        response = file.read()
        file.close()
        header = 'HTTP/1.1 200 OK\n Content-Type:text/html\n\n'
       
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
    
    final_response = header.encode('utf-8')
    final_response += response
    print("Final response:",final_response)
    client_connection.sendall(final_response)
    
    client_connection.close()
  
