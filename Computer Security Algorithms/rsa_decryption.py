# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:55:53 2018

@author: omkar
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os
import timeit
#Our Decryption Function
def decrypt_blob(encrypted_blob, private_key):

    #Import the Private Key and use for decryption using PKCS1_OAEP
    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    #Base 64 decode the data
    encrypted_blob = base64.b64decode(encrypted_blob)

    #In determining the chunk size, determine the private key length used in bytes.
    #The data will be in decrypted in chunks
    chunk_size = 384
    offset = 0
    decrypted = b""

    #keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        #The chunk
        chunk = encrypted_blob[offset: offset + chunk_size]

        #Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #return the decompressed decrypted data
    return decrypted

#Use the private key for decryption
fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()

#Our candidate file to be decrypted
fd = open("encrypted_sample2.txt", "rb")
encrypted_blob = fd.read()
fd.close()

#Write the decrypted contents to a file

fd = open("decrypted_sample2.txt", "wb")
start = timeit.default_timer()
fd.write(decrypt_blob(encrypted_blob, private_key))
fd.close()
stop = timeit.default_timer()
print('Time: ', stop - start)
p='F:\\Study\\MS\\SEM 1\\Comp Sec\\HomeWork\\decrypted_sample2.txt'
b=os.path.getsize(p)
time_per_byte=(stop - start)/b
print(f"Time to decrypted per byte is: {time_per_byte}")