#Client is ALICE
import socket
from chatCipher import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8001))

print("Secret message of Alice for Bob!!")
msg = "Heyy Bob, It's Alice!!"
ct = encryptMessage(msg)
print "secremsg: " + ct
client.send(ct)
print("\n")

server_msg = client.recv(4096).strip()
print("Bob sent you a Secret Message, Alice!!!")
print server_msg
print("\n")

print("**Alice decrypts Bob's message**")
server_msg = decryptMessage(server_msg)
print(server_msg)

client.close()


