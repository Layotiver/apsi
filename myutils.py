import Crypto.Util.number as cun
import Crypto.Hash.SHA256 as sha256


# 扩展欧几里得算法
def exgcd(a, b):
    if a < b:
        x, y = exgcd(b, a)
        return y, x

    if b == 0:
        return 1, 0

    x_, y_ = exgcd(b, a % b)
    x = y_
    y = x_ - y_ * (a // b)
    return x, y


# 求最大公因数
def gcd(a, b):
    x, y = exgcd(a, b)
    return a * x + b * y


# 求a的乘法逆元
def reverse(a, n):
    x, y = exgcd(a, n)
    if a * x + n * y != 1:
        raise ValueError("fuck! gcd(a,n)!=1")
    x %= n
    return x


# 快速幂，模n
def encrypt(a, b, n):
    ret = 1
    a = a % n
    while b:
        if b & 1:
            ret *= a
            ret %= n
        b = b // 2
        a = a * a
        a = a % n
    return ret


def RSA(bit_len=256, e_len=32):
    p = cun.getPrime(bit_len)
    q = cun.getPrime(bit_len)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = cun.getRandomNBitInteger(e_len)
    while 1:
        if gcd(e, phi_n) == 1:
            break
        e = cun.getRandomNBitInteger(e_len)

    d = reverse(e, phi_n)

    return p, q, n, e, d


def hash(string, salt=""):
    if not isinstance(string, str):
        string = str(string)
    h = sha256.new(salt.encode())
    h.update(string.encode())
    return int(h.hexdigest(), base=16)


# 读取集合 { i }，返回 { H(i) }
def read_set(file_name):
    with open(file_name) as f:
        h = sha256.new()
        set_list = f.read().split("\n")
        set_hash = [hash(i) for i in set_list]
    return set_hash


if __name__ == "__main__":
    p, q, n, e, d = RSA()
    # print(p, q, n, e, d, sep="\n\n")

    x = cun.getRandomNBitInteger(1024)
    en_x = encrypt(x, e, n)
    print(en_x)
