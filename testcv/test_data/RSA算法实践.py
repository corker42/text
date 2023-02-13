import math
import random
from Crypto.Util import number
def mach_e(fn):
    while True:
        e = random.randint(0, fn)
        if math.gcd(e, fn) == 1:
            return e
def mach_d(e, fn):
    d = 0
    while True:
        if (e * d) % fn == 1:
            return d
        d += 1
def create_keys(p,q):
   n = p * q
   fn = (p-1) * (q-1)
   e = mach_e(fn)
   d = mach_d(e, fn)
   return n, e, d

def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
def decrypt(ciphertexts, d, n):
    print("RSA解密")
    print("----------------------------")
    dec_texts = []
    for ciphertext in ciphertexts:
        dec_text = pow(ciphertext, d, n)
        dec_texts.append(dec_text)
    print("明文数字")
    for dec_text in dec_texts:
        print(dec_text, end="")
    print("\n----------------------------")
    dec_texts = [str(i) for i in dec_texts]
    print("明文数字分组")
    print("----------------------------")
    groups = []
    for dec_text in dec_texts:
        for i in range(0, len(dec_text), 3):
            group = dec_text[i:i+3]
            groups.append(group)
    for i, group in enumerate(groups):
        print(group, end=" ")
        if (i + 1) % 2 == 0:
            print("\n", end="")
    print("----------------------------")
    return groups

def encrypt(b_text, e, n):
    dec_text = []
    print("明文数字分组")
    print("----------------------------")
    for i, char in enumerate(b_text):
        char = int(char, 2)
        dec_text.append(char)
        print(char, end=" ")
        if (i+1) % 2 == 0:
            print("\n", end="")
    print("----------------------------")
    print("RSA加密")
    print("----------------------------")
    for i, dec in enumerate(dec_text):
        if len(str(dec)) < 3:
            dec = "0" + str(dec)
        dec_text[i] = str(dec)
    groups = []
    for group in zip(dec_text[::2], dec_text[1::2]):
        group = ''.join(group)
        groups.append(group)
    ciphertexts = []
    for group in groups:
        ciphertext = pow(int(group), e, n)
        ciphertexts.append(ciphertext)
    return ciphertexts

if __name__ == '__main__':
    print("生成两个素数")
    print("----------------------------")
    n_length = 14
    primeNum1 = number.getPrime(n_length)
    primeNum2 = number.getPrime(n_length)
    print("q =", primeNum1, " p =", primeNum2)
    print("----------------------------")
    print("生成公钥和私钥")
    print("----------------------------")
    n, e, d = create_keys(primeNum1,primeNum2)
    # n = 138579431
    # e = 4228085
    # d = 94050149
    print("公钥:(", n, e, ")")
    print("私钥:(", n, d, ")")
    print("----------------------------")
    text = "hello world!"
    print("文本")
    print("----------------------------")
    print(text)
    print("----------------------------")
    text = encode(text)
    b_text = text.split(' ')
    print("二进制")
    print("----------------------------")
    for i, char in enumerate(b_text):
        print(char, end=" ")
        if (i+1) % 2 == 0:
            print("\n", end="")
    print("----------------------------")
    ciphertexts = encrypt(b_text, e, n)
    print("密文如下：")
    print("----------------------------")
    s = [str(i) for i in ciphertexts]
    print(''.join(s))
    print("----------------------------")
    dec_text = decrypt(ciphertexts, d, n)
    dec_text = [int(i) for i in dec_text]
    dec_text = [str(i) for i in dec_text]
    print("二进制")
    print("----------------------------")
    for i,x in enumerate(dec_text):
        dec_text[i] = bin(int(x))[2:]
    for i, char in enumerate(dec_text):
        print(char, end=" ")
        if (i + 1) % 2 == 0:
            print("\n", end="")
    dec_text = " ".join(dec_text)
    dec_text = decode(dec_text)
    print("----------------------------")
    print("文本")
    print("----------------------------")
    print((dec_text))





