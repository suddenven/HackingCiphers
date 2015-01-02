#Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = input('Message: ')
    myKey = input('Key: ')

    ciphertext = encryptMessage(myKey, myMessage)

    #Add a | to the end of the ciphertext

    print(ciphertext + '|')

    #Copy the string to the keyboard
    pyperclip.copy(ciphertext)

    
