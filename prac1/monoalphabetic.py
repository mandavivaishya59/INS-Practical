def encrypt(s,p,ch):
    c=['']*len(s)
    for i in range(len(s)):
        char=s[i]
        if char.lower() in p:
            index=p.index(char.lower())
            if char.isupper():
                c[i]=ch[index].upper()
            else:
                c[i]=ch[index].lower()
        else:
            c[i]=char

    return "".join(c)

def decrypt(s,p,ch):
    m=['']*len(s)
    for i in range(len(s)):
        char=s[i]
        if char.lower() in [x.lower() for x in ch]:
            index=[x.lower() for x in ch].index(char.lower())
            if char.isupper():
                m[i]=p[index].upper()
            else:
                m[i]=p[index].lower()
        else:
            m[i]=char

    return "".join(m)

def main():
    p=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    ch=['j','e','i','o','u','m','n','d','v','t','r','s','h','l','b','f','c','g','a','k','p','q','w','y','z','x']

    s=input("Enter the text: ")
    en=encrypt(s,p,ch)
    dn=decrypt(en,p,ch)
    print("Encrypted text: ", en)
    print("Decrypted text: ", dn)

if __name__=="__main__":
    main()