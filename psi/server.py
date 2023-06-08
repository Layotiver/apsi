import Crypto.Util.number as cun
import Crypto.Hash.SHA256 as sha256
import myutils

FILE_NAME = "server_set.txt"
P_PRIME = 81763263289070360957195134095243904247377362381620100731869525982045277993803
Q_PRIME = 84742499462899041652732484273576460992829916440855421891158394771536172531313
E_key = 4190490217
D_key = 4287665434702991884139911976391141520010843870076401039268065505684567334651000340013953682013121899466439573002327068651622030560296543002581735105635321
N_mod = 6928823295358917993255461531469953051209715272966577456185381343835636191581719319555351295990764226700085325138946089255532788097571404495029128837453339
SALT = "salt"


class Server:
    def __init__(self) -> None:
        self.ts = []

    def off_line(self):
        self.ts.clear()
        set_hash = myutils.read_set(FILE_NAME)
        for i in set_hash:
            K = myutils.encrypt(i, D_key, N_mod)
            t = myutils.hash(K, SALT)
            self.ts.append(t)

    def on_line(self, ys):
        y_hats = [myutils.encrypt(i, D_key, N_mod) for i in ys]
        return y_hats, self.ts


if __name__ == "__main__":
    pass
