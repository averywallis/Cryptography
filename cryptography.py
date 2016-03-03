"""
cryptography.py
Author: Avery Wallis
Credit: Daniel, Payton

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
let=[]
thing=[]
c=0

ip=input('Enter e to encrypt, d to decrypt, or q to quit: ')
if  ip not in('e','d','q'):
    print("Did not understand command, try again.")
    ip=input('Enter e to encrypt, d to decrypt, or q to quit: ')

if ip=='e':
    message=input("Message: ")
    key=str(input("Key: "))
    l=len(message)
    k=len(key)
    for x in range (0,l):
        let.append(associations.find(message[x]))
    for y in range(0,k):
        thing.append(associations.find(key[y]))
    b=l-k
    for e in range(0,b):
        a=0
        thing.append(associations.find(key[a]))
        print(thing)
        a=a+1

elif ip=='d':
        print(let)
elif ip=='q':
    print("Goodbye!")


