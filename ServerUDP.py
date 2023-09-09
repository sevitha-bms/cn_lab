from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))

print("The server is ready to receive")

while True:
    sentence, clientAddress = serverSocket.recvfrom(2048)
    sentence = sentence.decode("utf-8")

    try:
        with open(sentence, "r") as file:
            file_contents = file.read(2048)
            serverSocket.sendto(bytes(file_contents, "utf-8"), clientAddress)
            print('\nSent contents of', sentence)
    except FileNotFoundError:
        error_message = f"File '{sentence}' not found."
        serverSocket.sendto(bytes(error_message, "utf-8"), clientAddress)
        print(error_message)

    file.close()
