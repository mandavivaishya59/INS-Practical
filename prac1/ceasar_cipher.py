def encrypt(text,s):
    result=""
    for char in text:
        if char.isupper():
            result+=chr((ord(char)+s-65)%26+65)
        elif char.islower():
            result+=chr((ord(char)+s-97)%26+97)
        else:
            result+=char
    return result

def decrypt(text,s):
    result=""
    for char in text:
        if char.isupper():
            result+=chr((ord(char)-s-65)%26+65)
        elif char.islower():
            result+=chr((ord(char)-s-97)%26+97)
        else:
            result+=char
    return result
            
if __name__=="__main__":
    text=input("enter the text : ")
    s=int(input("enter the key : "))

    E=encrypt(text,s)
    print("Encrypted text : ",E)

    D=decrypt(E,s)
    print("Decrypted text : ",D)
