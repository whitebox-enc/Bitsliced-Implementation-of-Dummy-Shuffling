#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
import os

n = 64
block_size = 16
plaintexts = []

for i in range(n):
    plaintext = os.urandom(block_size)
    plaintexts.append(plaintext)

with open("test_plaintext", "wb") as plaintext_file:
    for pt in plaintexts:
        plaintext_file.write(pt)

print(f"{n} groups of plaintext written to test_plaintext.")

k = b"samplekey1234567"

with open("test_plaintext", "rb") as plaintext_file:
    pt = plaintext_file.read()

print(len(pt))
if len(pt) % AES.block_size != 0:
    pt = pt[:len(pt) - (len(pt) % AES.block_size)]

cipher = AES.new(k, AES.MODE_ECB)
ct = cipher.encrypt(pt)

with open("test_ciphertext", "wb") as ciphertext_file:
    ciphertext_file.write(ct)

print("key:       ", binascii.hexlify(k).decode())
print("plaintext: ", binascii.hexlify(pt).decode())
print("ciphertext:", binascii.hexlify(ct).decode())

# with open("test_plaintext", "rb") as plaintext_file:
#     pt = plaintext_file.read()

# # pt_padded = pad(pt, AES.block_size)
# print(len(pt))
# if len(pt) % AES.block_size != 0:
#     pt = pt[:len(pt) - (len(pt) % AES.block_size)]

# # ECB
# cipher = AES.new(k, AES.MODE_ECB)
# ct = cipher.encrypt(pt)

# with open("test_ciphertext", "wb") as ciphertext_file:
#     ciphertext_file.write(ct)

# print("key:       ", binascii.hexlify(k).decode())
# print("plaintext: ", binascii.hexlify(pt).decode())
# print("ciphertext:", binascii.hexlify(ct).decode())

# #!/usr/bin/env python2
# #-*- coding:utf-8 -*-

# from Crypto.Cipher import AES

# k = open("key").read()[:16]

# pt = open("test_plaintext").read()
# ct = AES.new(k).encrypt(pt)
# open("test_ciphertext", "w").write(ct)

# # print "key:       ", k.encode("hex"), `k`
# # print "plaintext: ", pt.encode("hex"), `pt`
# # print "ciphertext:", ct.encode("hex"), `ct`