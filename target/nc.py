#! /usr/bin/python
import socket
import sys
import base64
import traceback
import time

try:
    payload = sys.argv[3]

    payload = base64.b64decode(payload)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((str(sys.argv[1]), int(sys.argv[2])))
    # sock.setblocking(False)
    sock.send(payload)
    time.sleep(0.2)
    p = sock.recv(65535)
    print(base64.b64encode(p))


except:
    # traceback.print_exc()
    pass
