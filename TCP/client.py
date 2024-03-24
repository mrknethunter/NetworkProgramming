from dotenv import load_dotenv
import os
from socket import *

if __name__ == '__main__':
    load_dotenv()
    PORT = int(os.getenv('PORT'))
    HOST = os.getenv('HOST')

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((HOST, PORT))
    print('Connected to server')
    print('Type "stop" to close connection', end='\n\n')

    while True:
        data = input('Please insert a message to send: ')

        if data == 'stop':
            break

        client.send(data.encode())
        res = client.recv(1024).decode('utf-8')
        print(f'Response from server: {res}')

    conn.close()

