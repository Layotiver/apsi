from transmit.send import Sender
from psi.client import Client

client=Client()
client.off_line()
send=Sender("localhost",12121)

y_hats, ts=send.send_msg(client.send_to_server())
print(client.on_line(y_hats,ts))