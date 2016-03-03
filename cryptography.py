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
input=input('Enter e to encrypt, d to decrypt, or q to quit: ')

if input=='e':
    message=str(input("Message: "))
    key=str(input("Key: "))
    l=len(message)
elif input=='d':
elif input=='q':

for x in range (0,l):
    let.append(associations.find(message[x]))

print(let)