#Server is BOB
import socket
from chatCipher import *
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8001))
server.listen(5)
conn, addr = server.accept()
client_msg = ''

print("Alice sent uh this secret message, Bob!!")
data = conn.recv(4096)
print "secretmsg: " + data + "\n"

print("**Bob decrypts Alice's message**")
print decryptMessage(data.strip())
print("\n")

print("Bob sends this message to Alice!!")
ct = encryptMessage("Hellooo Alicee!! Bob Here!!")
print ct + '\n'
conn.send(ct)

conn.close()
print("client ended conversation")
