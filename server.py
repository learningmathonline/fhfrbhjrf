import socket
import threading
import time
import json

host = 'localhost'
port = 62389

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

newprox = []

def recive():
    while True:
        client, address = server.accept()
        print('New Prox Incoming')
        print(newprox)
        prox = client.recv(1024).decode('utf-8')
        print('prox came')
        ok = client.recv(1024).decode('utf-8')
        print('prox came')
        ok = int(ok)
        print('recd ok')
        time.sleep(3)
        client.send(b'Thanks For Adding It Always Helps')
        print('New Prox Recieved')
        prox = prox.replace("'", '"')
        prox = json.loads(prox)
        prox = dict(prox)
        if ok == 1:
            if prox in newprox:
                pass
            else:
                print(prox)
                newprox.append(prox)
        else:
            client.close()
        print(newprox)

recive()
    