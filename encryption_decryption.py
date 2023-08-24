import math
from tkinter import *
import tkinter.messagebox
import random
root=Tk()
root.title("Encryptor And Decryptor Device")
root.config(bg='CadetBlue4')

def is_prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1

    if count==2:
        return True
    else:
        return False

def prime_gen():
    k=random.randint(10,200)
    while True:
        if is_prime(k):
            break
        else:
            k=k+1

    return k


p=prime_gen()
while True:
    q=prime_gen()
    if q!=p:
        break
Label(root,text="The value of P is "+str(p)).grid(row=2,column=1,padx=10,pady=30)
Label(root,text="The value of Q is "+str(q)).grid(row=2,column=2,padx=10,pady=30)
n=p*q
Label(root,text="The value of N is "+str(n)).grid(row=3,column=1,padx=10,pady=30)
t=(p-1)*(q-1)
Label(root,text="The value of T is "+str(t)).grid(row=3,column=2,padx=10,pady=30)
e=2

def egcd(a,b):
    if a==0:
        return (b,0,1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)




def modinv(a,m):
    g,x,y = egcd(a,m)
    if g != 1:
        return None
    else:
        return x%m


def gcd(a,b):
    if(b==0):
        return a
    else:
        return(gcd(b,a%b))
while(e<t):
    if(gcd(e,t)==1):
        break
    else:
        e=e+1


d = modinv(e,t)


text=Text(root,width=100,height=8)
text.grid(row=4,column=0,padx=10,pady=30,columnspan=4)
global enc
enc=[]
def encrypt():
    plain_text=text.get(1.0,END)
    ascii=[]
    for i in plain_text:
        ascii.append(ord(i))
    print(ascii)
    for j in ascii:
        C=pow(j,e)
        C=C%n
        enc.append(C)
    print(enc)

    Label(root,text="The Encrypted Message Is-").grid(row=9,column=0)
    texten = Text(root,width=20,height=5)
    texten.grid(row=9, column=1,padx=10,pady=30)
    for i in enc:
        texten.insert(END,str(i)+" ")
def decrypt():
    dec = []
    plain_text = text.get(1.0, END)
    plain_text = plain_text.split()
    plain_text = [int(x) for x in plain_text]
    print(plain_text)
    for k in plain_text:
        M=pow(k,d)
        M=int(M%n)
        dec.append(M)
    print(dec)
    org = ''.join(chr(val) for val in dec)
    print(str(org))
    Label(root, text="The Decrypted Message Is-").grid(row=9, column=2)
    textdn = Text(root, width=20, height=5)
    textdn.grid(row=9, column=3, padx=10,pady=30)
    textdn.insert(END,str(org))


button1=Button(root,text="ENCRYPT",command=encrypt,font=("comic sans ms",10),bg='indian red')
button1.grid(row=7,column=1,padx=10,pady=30)
button2=Button(root,text="DECRYPT",command=decrypt,font=("comic sans ms",10),bg='SpringGreen2')
button2.grid(row=7,column=3,padx=10,pady=30)
root.mainloop()