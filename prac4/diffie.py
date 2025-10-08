p=23
q=9
a=4
b=6

print("The value of P is : ",p)
print("The value of q is : ",q)
print("The private key of a is : ",a)
print("The private key of b is : ",b)

X=int(pow(p,a,q))
Y=int(pow(p,b,q))

print("\nThe public key of a is : ",X)
print("The public key of b is : ",Y)

Xa=int(pow(Y,a,q))
Xb=int(pow(X,b,q))

print("\nThe secret key for a is : ",Xa)
print("The secret key for b is : ",Xb)