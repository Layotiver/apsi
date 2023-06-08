import Crypto.Util.number as cun
import Crypto.Hash.SHA256 as sha256
from apsi.certificate import CertificateAuthority
import myutils

e1 = 4262248169
n1 = 4328236848640591846497999293204589862716945565888978129460830415472113271195442568964628200884085986388732361852540794421691114582987043680480463787953929

e2 = 3514693195
n2 = 11276099792544615335474267978320347122491668738105209654508057091536149776995561950721678078303251254520853321114489335466491055018545188183197038616790609

N = n1 * n2

FILE_NAME = "client_set.txt"
SALT = "salt"


class Client:
    def __init__(self) -> None:
        self.hcRe1 = []
        self.hcRe2 = []
        self.hcRe1e2 = []
        self.R = []

    def off_line(self, ca: CertificateAuthority):
        self.hc = myutils.read_set(FILE_NAME)

        for i in self.hc:
            Ri = cun.getRandomNBitInteger(32)
            Re1 = myutils.encrypt(Ri, e1, N)
            Re2 = myutils.encrypt(Ri, e2, N)
            Re1e2 = myutils.encrypt(Re1, e2, N)

            self.R.append(Ri)
            self.hcRe1.append(i * Re1 % N)
            self.hcRe2.append(i * Re2 % N)
            self.hcRe1e2.append(i * Re1e2 % N)

        if ca:
            self.hcRe1_d1, self.hcRe2_d1, self.hcRe1e2_d1 = ca.sign(self.hcRe1, self.hcRe2, self.hcRe1e2)
        else:
            self.hcRe1_d1, self.hcRe2_d1, self.hcRe1e2_d1 = (
                [0 for i in self.hcRe1],
                [0 for i in self.hcRe1],
                [0 for i in self.hcRe1],
            )

    def send_to_server(self):
        return [self.hcRe2, self.hcRe2_d1, self.hcRe1e2, self.hcRe1e2_d1]

    def on_line(self, hcRe2_d2, hcRe1e2_d1d2, ts):
        ret = []
        for idx, (i, j, k) in enumerate(zip(self.hcRe1_d1, hcRe2_d2, hcRe1e2_d1d2)):
            x = k * myutils.reverse(i, N) * myutils.reverse(j, N) * self.R[idx] % N
            x %= n1
            x = myutils.encrypt(x, e1, n1)
            x = x * self.hc[idx] % n1
            t = myutils.hash(x, SALT)

            if t in ts:
                ret.append(idx)
        return ret
