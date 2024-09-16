import re
from os import urandom
from secret import key,nonce
from Crypto.Util import Counter
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import *



def encrypt(m):
    return AES.new(key, mode=AES.MODE_CTR, nonce=nonce).encrypt(m)

def save_file(path,path1):
    with open(path,"r") as f:
        with open(path1, "wb") as g:
            for line in f:
                words=line.split()
                for word in words:
                    m=re.match("[a-zA-Z0-9{}:]+",word).group() #正则匹配单词然后进行加密操作
                    m=m.encode()
                    g.write(encrypt(m)+b" ")




# save_file("./cipher.txt","enc1.txt")