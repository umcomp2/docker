#!/usr/bin/python3
import socket
import multiprocessing
import signal
import time
import datetime
import os
from urllib.parse import urlparse


def service(s2,addr):
    data = s2.recv(1024).decode()
    print(addr,data)
    p = urlparse(data)
    request = p.path.split("/")[1]
    #print (request)
    if request == "loadtest":
        x = 0
        while x < 100000000:
            y = x*x
            x = x + 1
        s2.send("HTTP/1.1 200 OK\nServer: sockerserver/0.1\nContent-Type: text/html\n\nusing cpu ....\n".encode())
        exit()
    else:
        try:
           loops = int(request)
        except ValueError:
           s2.send("HTTP/1.1 200 OK\nServer: sockerserver/0.1\nContent-Type: text/html\n\nTry: Any_Number as fist URL path value to produce a delay\n".encode())
           exit()
#< HTTP/1.1 200 OK
#< Server: nginx/1.18.0 (Ubuntu)
#< Date: Sat, 08 Oct 2022 02:43:57 GMT
#< Content-Type: text/html
#< Content-Length: 162
#< Connection: keep-alive
    response = "HTTP/1.1 200 OK\nServer: sockerserver/0.1\nContent-Type: text/html\n"
    response = response + "Date: " + time.ctime() + "\n"
    response = response + "Content-Length: " + str(40 * loops) + "\nConnection: close\n\n"
    cuanto1 = s2.send(response.encode())
    for line in range(loops):
       cuanto2 = s2.send("23456789qwertyuiopasdfghjklzxcvbnm12345\n".encode())
       time.sleep(0.5)
    s2.close()

# no zombiessss
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# .... address already in use 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    port = int(os.environ['port'])
except ValueError:
    print ("use a number for port ! ... using default -> 4000")
    port = 4000
s.bind(("0.0.0.0",port))
s.listen(1)
print ("listening in port", port)
while True:
    s2,addr = s.accept()
    hijo = multiprocessing.Process(target=service, args = (s2,addr,))
    hijo.start()
    hijo.join()
    # open file descriptors
    #sudo lsof  -p 163748
    s2.close()
