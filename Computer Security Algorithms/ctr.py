# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:04:49 2018

@author: omkar
"""
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
import timeit

class Encryptor:
    def __init__(self,key):
        self.key = key
        
    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key):
        message = self.pad(message)
        #iv = Random.new().read(AES.block_size)
        secret = (Random.get_random_bytes(16))
        cipher = AES.new(key, AES.MODE_CTR, counter = lambda:secret)
        return secret + cipher.encrypt(message)
    
    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext,self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)
        f=file_name + ".enc"
        return f
        
    def decrypt(self, ciphertext, key):
        secret = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CTR, counter = lambda:secret)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")
    
    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext,self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)
        return file_name[:-4]
    
choice1 = int(input(
        "1. Press '1' to encrypt using 128bit key.\n2. Press '2' to encrypt using 256bit key.\n"))
if choice1 == 1:
      start = timeit.default_timer()
      key = (Random.get_random_bytes(16))
      stop = timeit.default_timer()
      print('Time: ', stop - start)
      print(key)
      print(len(key))   
    
elif choice1 == 2:
      start = timeit.default_timer()
      key = (Random.get_random_bytes(32))
      stop = timeit.default_timer()
      print('Time: ', stop - start)
      print(key)
      print(len(key))

enc = Encryptor(key)
clear = lambda: os.system('cls')
def filecheck():
    if os.path.isfile('data.txt.enc'):
        while True:
            password = str(input("Enter password: "))
            enc.decrypt_file("data.txt.enc")
            p = ''
            with open("data.txt", "r") as f:
                p = f.readlines()
            if p[0] == password:
                enc.encrypt_file("data.txt")
                break
    
        while True:
            clear()
            choice = int(input(
                "1. Press '1' to encrypt 1KB file.\n2. Press '2' to encrypt 1MB file.\n3. Press '3' to decrypt file.\n4. Press '4' to exit.\n"))
            clear()
            if choice == 1 or choice == 2:
                x = str(input("Enter name of file to encrypt: "))
                start = timeit.default_timer()
                f=enc.encrypt_file(x)
                stop = timeit.default_timer()
                print('File Encrypted')
                print('Time: ', stop - start)
                p='F:\\Study\\MS\\SEM 1\\Comp Sec\\HomeWork\\'+f
                b=os.path.getsize(p)                
                time_per_byte=(stop - start)/b
                print(f'Encryption time per byte is:\n{time_per_byte}')
                
            elif choice == 3:
                x = str(input("Enter name of file to decrypt: "))
                start1 = timeit.default_timer()
                f=enc.decrypt_file(x)
                stop1 = timeit.default_timer()
                print('File Decrypted')
                print('Time: ', stop1 - start1)
                p='F:\\Study\\MS\\SEM 1\\Comp Sec\\HomeWork\\'+f
                b=os.path.getsize(p)
                time_per_byte=(stop - start)/b
                print(f'Decryption time per byte is:\n{time_per_byte}')
                
            elif choice == 4:
                os.remove('data.txt.enc')
                break
            else:
                print("Please select a valid option!")
    
    else:
        while True:
            clear()
            password = str(input("Setting up stuff. Enter a password that will be used for encryption: "))
            repassword = str(input("Confirm password: "))
            if password == repassword:
                break
            else:
                print("Passwords Mismatched!")
        f = open("data.txt", "w+")
        f.write(password)
        f.close()
        enc.encrypt_file("data.txt")
        filecheck()
        
filecheck()