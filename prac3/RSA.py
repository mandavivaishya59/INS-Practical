from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair (public + private)
key = RSA.generate(1024)
public_key = key.publickey()

# Display keys
print("Public key:")
print(public_key.export_key().decode())

print("\nPrivate key:")
print(key.export_key().decode())

# Take input from user
message = input("\nEnter a message: ").encode()

# Encrypt message
cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(message)
print("\nEncrypted message:", encrypted.hex())

# Decrypt message
decipher = PKCS1_OAEP.new(key)
decrypted = decipher.decrypt(encrypted)
print("\nDecrypted message:", decrypted.decode())
