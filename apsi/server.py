import myutils

e1 = 4262248169
n1 = 4328236848640591846497999293204589862716945565888978129460830415472113271195442568964628200884085986388732361852540794421691114582987043680480463787953929

p2 = 99292401535669340584420400316386735456546488037889516317584113881202385827653
q2 = 113564579143489058260704784828269061754698257618987030615638975871987882225053
n2 = 11276099792544615335474267978320347122491668738105209654508057091536149776995561950721678078303251254520853321114489335466491055018545188183197038616790609
e2 = 3514693195
d2 = 7187373602997877884975206858292584106334849194169139487129156229120804144722409918745235450378860919224465772364674907434851351996167247872881690593550819

N = n1 * n2

FILE_NAME = "server_set.txt"
SALT = "salt"


class Server:
    def __init__(self) -> None:
        self.ts = []

    def off_line(self):
        self.ts.clear()
        hs = myutils.read_set(FILE_NAME)
        for i in hs:
            k = myutils.encrypt(i, d2, n1) * myutils.reverse(myutils.encrypt(i, e1 * d2, n1),n1) % n1
            t = myutils.hash(k, SALT)
            self.ts.append(t)

    def on_line(self, hcRe2, hcRe2_d1, hcRe1e2, hcRe1e2_d1):
        hcRe1e2_d1d2 = []
        hcRe2_d2 = []
        for i, j, k, l in zip(hcRe2, hcRe2_d1, hcRe1e2, hcRe1e2_d1):
            if myutils.encrypt(j, e1, n1) != i%n1:
                print("error1")
                return -1
            if myutils.encrypt(l, e1, n1) != k%n1:
                print("error2")
                return -1
            hcRe1e2_d1d2.append(myutils.encrypt(l, d2, N))
            hcRe2_d2.append(myutils.encrypt(i, d2, N))

        return self.ts, hcRe2_d2, hcRe1e2_d1d2
