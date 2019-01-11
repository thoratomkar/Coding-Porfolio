# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:11:38 2018

@author: swats
"""

from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
#import hashlib
import timeit

#filename = "sample.txt"
start = timeit.default_timer()
key = DSA.generate(2048)
stop = timeit.default_timer()
print('Time for key generation: ', stop - start)

def hash_file(filename,h):
   
   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
   # return the hex representation of digest
   return h.hexdigest()

h = SHA256.new()
x = str(input("Enter name of file to hash: "))

message = hash_file(x,h)
print(f"The hash of the file is:\n{message}")


start = timeit.default_timer()
signer = DSS.new(key, 'fips-186-3')
stop = timeit.default_timer()
print('Time for producing sign: ', stop - start)
signature = signer.sign(message)

verifier = DSS.new(key, 'fips-186-3')
try:
     start = timeit.default_timer()
     verifier.verify(message, signature)
     print("The message is authentic.")
     stop = timeit.default_timer()
     print('Time for verifying sign: ', stop - start)
except ValueError:
     print ("The message is not authentic.")