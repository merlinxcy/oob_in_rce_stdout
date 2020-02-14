import base64
import socket
import threading
import os
import time
import subprocess
os.system("rm /tmp/traffic")


def rceFunction(traffic_paylaod):
    if traffic_paylaod:
        b64_traffic = base64.b64encode(traffic_paylaod)
        print(b64_traffic)
        # t = os.popen("echo %s |base64 -d | nc 127.0.0.1 65000" % b64_traffic)
        t = subprocess.Popen("nc.py 127.0.0.1 65000 %s" % str(b64_traffic)[2:-1],
                         shell=True,
                         stdout=subprocess.PIPE)
        result = t.stdout.read()
        print(result)
    else:
        t = subprocess.Popen("nc.py 127.0.0.1 65000 %s" % str(base64.b64encode(b"XCVF"))[2:-1],
                             shell=True,
                             stdout=subprocess.PIPE)
        result = t.stdout.read()
        print(result)
    if result:
        result = base64.b64decode(result)
    return result


class ListenSocketServer:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 63777
        self.handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handle.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def listen(self):
        self.handle.bind((self.host,self.port))
        self.handle.listen(5)
        tmp_handle, addr = self.handle.accept()
        self.event_handler(tmp_handle)
        # while True:
        #     tmp_handle,addr = self.handle.accept()
        #     client_handle = threading.Thread(target=self.event_handler, args=(tmp_handle,))
        #     client_handle.start()

    def event_handler(self, client):
        result = rceFunction(None)
        time.sleep(0.2)
        if result:
            client.send(result)
        while True:
            print(111)
            try:
                data = client.recv(65535)
                print("asd")
            except:
                data = None
            result = rceFunction(data)
            client.send(result)
            print(333)

if __name__ == '__main__':
    listen_socket = ListenSocketServer()
    listen_socket.listen()
