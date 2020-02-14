import base64
import socket
import threading
import os
import time


class Client:
    def __init__(self):
        # self.host = '47.111.139.74'
        self.host = '127.0.0.1'
        # self.port = 6379
        self.port = 631
        self.handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handle.connect((self.host, self.port))
        self.handle.setblocking(False)

    def send(self,payload):
        try:
            self.handle.send(payload)
        except:
            self.__init__()

    def recv(self):
        try:
            time.sleep(0.1)
            return self.handle.recv(65535)
        except:
            return None

class ListenSocketServer:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 65000
        self.handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handle.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client = None

    def listen(self):
        self.handle.bind((self.host,self.port))
        self.handle.listen(5)
        self.client = Client()
        while True:
            tmp_handle, addr = self.handle.accept()
            self.event_handler(tmp_handle)

    def event_handler(self, client):
        time.sleep(0.1)
        data = client.recv(65535)
        print(data)
        if data == b'XCVF':
            ret = self.client.recv()
            print(ret)
            if ret: client.send(ret)
        else:
            self.client.send(data)
            ret = self.client.recv()
            print(ret)
            if ret: client.send(ret)
        client.close()
        return


if __name__ == '__main__':
    listen_socket = ListenSocketServer()
    listen_socket.listen()
