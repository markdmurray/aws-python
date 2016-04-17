#socket test

import socket
import time

port = 22
host = '54.206.78.92'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
done = False
print("Waiting for port %s to open" % port)
while not done:
    try:
        s.connect((host, port))
        s.shutdown(2)
        print("")
        print("Success connecting to %s on port %d" % (host, port))
        done = True
    except socket.error as e:
        time.sleep(2)
        print(".",end="",flush=True)
