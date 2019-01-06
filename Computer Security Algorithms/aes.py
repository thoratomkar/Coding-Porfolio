from Crypto.Cipher import AES
import base64
import os
import random,string
import timeit



def encryption(message):
	BLOCK_SIZE=16
	PADDING='{'
	pad=lambda s: s+ (BLOCK_SIZE - len(s) % BLOCK_SIZE)*PADDING
	EncodeAES=lambda c,s: base64.b64encode(c.encrypt(pad(s)))
	key=os.urandom(BLOCK_SIZE)
	print(f'Encryption Key: {key}')
	print(f'The message is: {message}')

	cipher=AES.new(key,AES.MODE_ECB)

	encoded=EncodeAES(cipher,message)
	print(f'Encrypted Message: {encoded}')
	#decryption(encoded,key)
   


def decryption(encoded,key):
	PADDING='{'
	DecodeAES=lambda c, e: c.decrypt(base64.b64decode(e))#.rstrtip(PADDING)
	
	#key=secret
	cipher=AES.new(key,AES.MODE_ECB)
	decoded=DecodeAES(cipher,encoded)
	print(f'Decrypted Message: {decoded}')
    
encryption('1234567890123456')

start = timeit.default_timer()
for i in range(1001):
	x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
	encryption(x)
    #decryption(encoded,key)

stop = timeit.default_timer()

print('Time: ', stop - start) 