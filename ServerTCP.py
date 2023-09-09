from socket import *

serverName = "127.0.0.1"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()

    try:
        with open(sentence, "r") as file:
            filecontents = file.read(1024)
            connectionSocket.send(filecontents.encode())
            print(f"Sent contents of {sentence}")
    except FileNotFoundError:
        error_message = f"File '{sentence}' not found."
        connectionSocket.send(error_message.encode())
        print(error_message)

    connectionSocket.close()
