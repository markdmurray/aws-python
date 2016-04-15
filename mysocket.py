#socket test

import socket
import time

port = 80
host = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
done = False
while not done:
    try:
        s.connect((host, port))
        s.shutdown(2)
        print("Success connecting to ")
        print(host," on port: ",str(port))
        done = True
    except socket.error as e:
        time.sleep(5)
        print("." end="")
