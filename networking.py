import socket
import time
import random

HOST = '192.168.241.38'
PORT = 50007  # The same port as used by the server
thislist = ["Bacon", "Eggs", "Grits"]
print("About to connect...")

for i in range(5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(random.choice(thislist).encode("utf-8"))
        print("Message sent.")
        time.sleep(1)
