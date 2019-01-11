# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:07:07 2018

@author: omkar
"""

import hashlib
import os
import timeit

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

clear = lambda: os.system('cls')

while True:
             clear()
             choice = int(input(
                    "1. Press '1' to hash using SHA256.\n2. Press '2' to encrypt using SHA512.\n3. Press '3' to encrypt using SHA3_256.\n4. Exit.\n"))
             if choice == 1:
                h = hashlib.sha256()
                x = str(input("Enter name of file to hash: "))
                start = timeit.default_timer()
                message = hash_file(x,h)                
                print(f"The hash of the file is:\n{message}")
                stop = timeit.default_timer()
                print('Time: ', stop - start)
                p='F:\\Study\\MS\\SEM 1\\Comp Sec\\HomeWork\\'+x
                b=os.path.getsize(p)
                time_per_byte=(stop - start)/b
                print(f"Time to hash per byte is: {time_per_byte}")
                
             elif choice == 2:
                  h = hashlib.sha512()
                  x = str(input("Enter name of file to hash: "))
                  start = timeit.default_timer()
                  message = hash_file(x,h)
                  print(f"The hash of the file is:\n{message}")
                  stop = timeit.default_timer()
                  print('Time: ', stop - start)
                  p='F:\\Study\\MS\\SEM 1\\Comp Sec\\HomeWork\\'+x
                  b=os.path.getsize(p)
                  time_per_byte=(stop - start)/b
                  print(f"Time to hash per byte is: {time_per_byte}")
            
             elif choice == 3:
                  h = hashlib.sha3_256()
                  x = str(input("Enter name of file to hash: "))
                  start = timeit.default_timer()
                  message = hash_file(x,h)
                  print(f"The hash of the file is:\n{message}")
                  stop = timeit.default_timer()
                  print('Time: ', stop - start)
                  p='F:\\Study\\MS\\SEM 1\\Comp Sec\\HomeWork\\'+x
                  b=os.path.getsize(p)
                  time_per_byte=(stop - start)/b
                  print(f"Time to hash per byte is: {time_per_byte}")
                  
             elif choice == 4:
                  break
             else:
                  print("Please select a valid option!")