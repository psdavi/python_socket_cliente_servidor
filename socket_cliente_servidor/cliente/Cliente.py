import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.0.112', 6666))
print('Conectado\n')

name_file = str(input("Arquivo>"))

client.send(name_file.encode())

with open(name_file, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{name_file} recebido\n')
#print('recebido\n')

