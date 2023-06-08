from transmit.receive import Receiver
from psi.server import Server

rec=Receiver("localhost",12121)
server=Server()
server.off_line()

def func(data):
    try:
        ret=server.on_line(data)
        return ret
    except Exception:
        print("something error")
        return "SOMETHING ERROR!"
    
rec.rec_msg(func)