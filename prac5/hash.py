import hashlib

msg=input("Enter the Message : ")
result=hashlib.sha1(msg.encode())

print("The hexadecimal equivalent of hash is :" )
print(result.hexdigest())