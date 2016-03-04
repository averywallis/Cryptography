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
scram=[]


def encrypt():
    message=input("Message: ")
    key=str(input("Key: "))
    l=len(message)
    k=len(key)
    for x in range (0,l):
        let.append(associations.find(message[x]))
    for y in range(0,k):
        thing.append(associations.find(key[y]))
    print(let)
    b=l-k
    for e in range(0,b):
        thing.append(associations.find(key[e]))
    print(thing)
    for x in range(0,l):
        scram.append(let[x]+thing[x])
    print(scram)

def decrypt():
    print('thing')
    
def run():
    ip=input('Enter e to encrypt, d to decrypt, or q to quit: ')
    if ip=='e':
        encrypt()
    elif ip=='d':
        decrypt()
    elif ip=='q':
        print("Goodbye!")
        return
    else:
        print("Did not understand command, try again.")
        run()
    
run()
