from transmit.send import Sender
from apsi.client import Client
from apsi.certificate import CertificateAuthority

ca=CertificateAuthority()

client = Client()
client.off_line(ca)
send = Sender("localhost", 12122)

ts, hcRe2_d2, hcRe1e2_d1d2 = send.send_msg(client.send_to_server())
print(client.on_line(hcRe2_d2, hcRe1e2_d1d2, ts))
