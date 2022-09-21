import requests
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
proxy = {'http': 'localhost:54357'}

r = requests.get('https://www.coolmathgames.com/', proxies=proxy, verify=False)
with open('main.html', 'w') as f:
    f.write(r.text)

print(r.text)