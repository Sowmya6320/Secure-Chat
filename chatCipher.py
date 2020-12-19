from Crypto.Util.number import *
from Crypto.Cipher import AES
import os
from Crypto.Hash import HMAC, SHA512

def pad(s):
	bs = 16
	s += chr(bs - (len(s) % bs)) * (bs - (len(s) % bs))
	return s	

def encrypt(msg,key):
	iv = os.urandom(16)
	aes = AES.new(key, AES.MODE_CBC, iv)
	ct = iv + aes.encrypt(pad(msg))
	return ct.encode("hex")

def decrypt(ct,key):
	ct = ct.decode("hex")
	iv = ct[:16]
	ciphertext = ct[16:]
	aes = AES.new(key,AES.MODE_CBC,iv)
	pt = aes.decrypt(ciphertext)
	return pt[:-ord(pt[-1])] #to remove padding

def mac(msg):
	secret = "hashbash"
	h = HMAC.new(secret, digestmod=SHA512)
	h.update(msg)
	return h.hexdigest()

def validate(msg,mac_):
	secret = "hashbash"
	h = HMAC.new(secret, digestmod=SHA512)
	h.update(msg)
	if mac_ == h.hexdigest():
		return True
	else:
		return False
	
def encryptMessage(msg):
	key = "SilverTeaCupss!!"
	cipher = encrypt(msg,key)
	mac_ = mac(msg)
	return cipher + "||" + mac_ 
	
def decryptMessage(cipher):
	key = "SilverTeaCupss!!"
	cipher = cipher.split('||')
	ct = cipher[0]
	mac_ = cipher[1]
	pt = decrypt(ct,key)
	if validate(pt,mac_):
		return pt





	
	

