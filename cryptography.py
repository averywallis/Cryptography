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


ip=input('Enter e to encrypt, d to decrypt, or q to quit: ')
if not ip=='q' or ip=='e' or ip=='d':
    print("Did not understand command, try again.")
    ip=input('Enter e to encrypt, d to decrypt, or q to quit: ')

if ip=='e':
    message=input("Message: ")
    key=str(input("Key: "))
    l=len(message)
    k=len(key)
    for x in range (0,l):
        let.append(associations.find(message[x]))
    if k<l:
        for y in range(0,k):
            
        
elif ip=='d':
        print(let)
elif ip=='q':
    print("Goodbye!")


