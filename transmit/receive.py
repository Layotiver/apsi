import socket
import pickle


class Receiver:
    def __init__(self, host, port):
        self.host = host
        self.port = port


    def rec_msg(self, func):
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = socket.socket()
        s.bind((self.host, self.port))
        s.listen(1)
        print("等待连接...")
        while 1:
            conn, addr = s.accept()
            print("已连接:", addr)
            data_bytes = b""
            while True:
                packet = conn.recv(1024)
                if packet is not None:
                    data_bytes += packet
                if packet is None or len(packet) < 1024:
                    break
            # data_bytes = conn.recv(1048576)
            # print(len(data_bytes))
            data_list = pickle.loads(data_bytes)

            # print("接收到的数据:", data_list)

            #conn.close()

            data_bytes = pickle.dumps(func(data_list))
            print(len(data_bytes))
            
            conn.sendall(data_bytes)
            conn.close()

