from dotenv import load_dotenv
import os
from socket import *

if __name__ == '__main__':
    load_dotenv()
    PORT = int(os.getenv('PORT'))

    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('', PORT))
    server.listen(1)
    print(f'The server is listening on port {PORT}')

    while True:
        conn, client = server.accept()

        while True:
            print(f'Detected connection from: {client}')
            data = conn.recv(1024).decode('utf-8')
            print(f'Received data: {data}')
            res = 'Received "{}", status ok'.format(data)
            conn.send(res.encode())

        conn.close()
