import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.0.112', 6666))
print("Aguardando conexões...\n")
server.listen(2)

connection, address = server.accept()


name_file = connection.recv(1024).decode()
print(name_file)

with open(name_file, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print("Arquivo enviado")