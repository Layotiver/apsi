from transmit.receive import Receiver
from apsi.server import Server

rec=Receiver("localhost",12122)
server=Server()
server.off_line()

def func(data):
    try:
        ret=server.on_line(*data)
        return ret
    except Exception as e:
        print(e)
        return "SOMETHING ERROR!"
    
rec.rec_msg(func)