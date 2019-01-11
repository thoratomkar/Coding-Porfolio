# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:45:21 2018

@author: omkar
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import timeit
import base64
import os
#Our Encryption Function
def encrypt_blob(blob, public_key):
    #Import the Public Key and use for encryption using PKCS1_OAEP
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #compress the data first
    #blob = zlib.compress(blob)

    #In determining the chunk size, determine the private key length used in bytes
    #and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted
    #in chunks
    chunk_size = 256
    offset = 0
    end_loop = False
    encrypted = b""

    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]

        #If the data chunk is less then the chunk size, then we need to add
        #padding with " ". This indicates the we reached the end of the file
        #so we end loop here
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b" " * (chunk_size - len(chunk))

        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #Base 64 encode the encrypted file
    return base64.b64encode(encrypted)

#Use the public key for encryption
fd = open("public_key.pem", "rb")
public_key = fd.read()
fd.close()

#Our candidate file to be encrypted
fd = open("sample.txt", "rb")
unencrypted_blob = fd.read()
fd.close()
start = timeit.default_timer()
encrypted_blob = encrypt_blob(unencrypted_blob, public_key)
stop = timeit.default_timer()
print('Time: ', stop - start)
#Write the encrypted contents to a file

fd = open("encrypted_sample.txt", "wb")
fd.write(encrypted_blob)
fd.close()
p='F:\\Study\\MS\\SEM 1\\Comp Sec\\HomeWork\\encrypted_sample2.txt'
b=os.path.getsize(p)
time_per_byte=(stop - start)/b
print(f"Time to encrypted per byte is: {time_per_byte}")