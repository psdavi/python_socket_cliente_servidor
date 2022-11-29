import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "192.168.0.112"
# the port, let's use 5001
port = 6666

print('Conectado ao Servidor\n')

opcao = int(input("Digite a opção: (1)Enviar - (2)Receber>"))

if opcao == 1:
    # the name of file we want to send, make sure it exists
    filename = str(input("Arquivo>"))
    # get the file size
    filesize = os.path.getsize(filename)

    # create the client socket
    s = socket.socket()

    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
elif opcao == 2:
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
    # print('recebido\n')
