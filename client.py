import socket
import time

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 62389))

client.send("{'localhost': 54357}".encode('utf-8'))
time.sleep(3)
client.send('1'.encode('utf-8'))
time.sleep(3)
mess = client.recv(1024)
print(mess)
client.close()

proxy.bind(('localhost', 54357))
while True:
    try:
        pass
    except:
        pass