from Crypto.Cipher import AES
import socket

key=b"ThisIsASecretKey"
cipher=AES.new(key,AES.MODE_EAX)
nonce=cipher.nonce

data=b"This is a secret ip packet"
cipher_text,tag=cipher.encrypt_and_digest(data)

s=socket.socket()
s.connect(("localhost",9999))

s.send(nonce+cipher_text)

print("packet send ")
s.close()
