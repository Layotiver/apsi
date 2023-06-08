import Crypto.Util.number as cun
import Crypto.Hash.SHA256 as sha256
import myutils

FILE_NAME = "client_set.txt"
E_key = 4190490217
N_mod = 6928823295358917993255461531469953051209715272966577456185381343835636191581719319555351295990764226700085325138946089255532788097571404495029128837453339
SALT = "salt"


class Client:
    def __init__(self):
        self.ys = []
        self.Rs = []
        self.R_reverses = []

    def off_line(self):
        set_hash = myutils.read_set(FILE_NAME)

        for i in set_hash:
            R_i = cun.getRandomNBitInteger(32)
            y_i = myutils.encrypt(R_i, E_key, N_mod)
            y_i *= i
            y_i %= N_mod
            R_i_rev = myutils.reverse(R_i, N_mod)

            self.ys.append(y_i)
            self.Rs.append(R_i)
            self.R_reverses.append(R_i_rev)

    def send_to_server(self):
        return self.ys

    def on_line(self, y_hats, ts):
        psi = []
        for i, y_hat in enumerate(y_hats):
            y_hat = y_hat * self.R_reverses[i] % N_mod
            t_hat = myutils.hash(y_hat, SALT)
            if t_hat in ts:
                psi.append(i)
        return psi


if __name__ == "__main__":
    pass
