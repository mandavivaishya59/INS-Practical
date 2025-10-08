from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

key=RSA.generate(2048)

pubkey=key.publickey().export_key()
privkey=key.export_key()

original_msg=b"Hello this is original msg"
modified_msg=b"Hello this is modified msg"

original_hash=SHA256.new(original_msg)
modified_hash=SHA256.new(modified_msg)

signature=pkcs1_15.new(RSA.import_key(privkey)).sign(original_hash)

try:
    pkcs1_15.new(RSA.import_key(pubkey)).verify(original_hash,signature)
    print("Validate Signature")
except(ValueError, TypeError):
    print("Inavlid Signature")