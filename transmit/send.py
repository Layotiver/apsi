import socket
import pickle
import base64


class Sender:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_msg(self, data_list):
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = socket.socket()
        s.connect((self.host, self.port))
        data_bytes = pickle.dumps(data_list)

        # print(len(data_bytes))
        s.sendall(data_bytes)

        data_bytes = b""
        while True:
            packet = s.recv(1024)
            if packet is not None:
                data_bytes += packet
            if packet is None or len(packet) < 1024:
                break

        # data_bytes = s.recv(1024)
        # print(len(data_bytes))
        data_list = pickle.loads(data_bytes)
        # print("接收到的数据:", data_list)

        s.close()
        return data_list
