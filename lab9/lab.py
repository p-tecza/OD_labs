from math import sqrt
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import random

def isPrime(n):
  for i in range(2,int(n/2)):
    if (n%i) == 0:
      return False
  return True

def coPrime(num1, num2):
    mn = min(num1, num2) 
    for i in range(1, mn+1): 
        if num1%i==0 and num2%i==0: 
            hcf = i 
    if hcf == 1: 
        return True
    else: 
        return False

def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def modInverse(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

# ZAD 1

p=0
q=0

for x in range (0,2):
    p = random.randint(10,500)
    q = random.randint(10,500)

    while(not isPrime(p)):
        p+=1
    while((not isPrime(q)) and p!=q):
        q+=1

print("p:"+str(p))
print("q:"+str(q))

n = p*q

print("n:"+str(n))

wsp=(p-1)*(q-1)

e = random.randint(10,20)

while(not coPrime(wsp,e)):
    e+=1

print("e:"+str(e))



d=modInverse(e,(p-1)*(q-1))

print("d:"+str(d))

m = 100

print("start: "+str(m))

c = pow(m,e) % n

print("crypted: "+str(c))

back = pow(c,d) % n

print("decrypt: "+str(back))


print("kl. publ ("+str(e)+","+str(n)+")")
print("kl. pr ("+str(d)+","+str(n)+")")

# ZAD 2

message=200


rsa_keys = RSA.generate(2048) 
pub_key = rsa_keys.public_key().e
priv_key = rsa_keys.d
n_of_key=rsa_keys.n

crypt = pow(message,pub_key,n_of_key)
decrypt = pow(crypt,priv_key,n_of_key)


print("Original message: "+str(message))
print("Crypted RSA[2048]: "+str(crypt))
print("Decrypted RSA[2048]: "+str(decrypt))



