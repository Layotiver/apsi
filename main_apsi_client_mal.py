# 恶意客户端
# 提供的元素没有证书

from transmit.send import Sender
from apsi.client import Client

client = Client()
client.off_line(None)

send = Sender("localhost", 12122)

print(send.send_msg(client.send_to_server()))
