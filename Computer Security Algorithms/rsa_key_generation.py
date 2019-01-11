# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:42:09 2018

@author: omkar
"""

from Crypto.PublicKey import RSA
import timeit
#Generate a public/ private key pair using 3072 bits key length (256 bytes)
start = timeit.default_timer()
new_key = RSA.generate(2048, e=65537)
stop = timeit.default_timer()
print('Time: ', stop - start)

#The private key in PEM format
private_key = new_key.exportKey("PEM")

#The public key in PEM Format
public_key = new_key.publickey().exportKey("PEM")

print(private_key)
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print(public_key)
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()