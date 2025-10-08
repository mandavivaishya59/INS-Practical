from Crypto.Cipher import AES
import socket

key=b"ThisIsASecretKey"

ser=socket.socket()
ser.bind(("localhost",9999))
ser.listen(1)

print("Waiting for encrypted packet....")

conn,addr=ser.accept()
data=conn.recv(1024)

nonce=data[:16]
cipher_text=data[16:]

cipher=AES.new(key,AES.MODE_EAX,nonce)
plaintext=cipher.decrypt(cipher_text)

print("Decrypted Message : ",plaintext.decode())