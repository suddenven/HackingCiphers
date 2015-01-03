# Transposition Decryption

import math, pyperclip

def main():
    myMessage = input('Message: ')
    myKey = int(input('Key: '))

    plaintext = decryptMessage(myKey, myMessage)

    # Add a pipe (|) at the end of the message

    print(plaintext + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # The transposition decrypt function will simulate columns and rows
    # by using a list of strings.
    # Some calculations first.

    # Number of columns in our grid
    numColumns = math.ceil(len(message) / key )

    # Number of rows
    numRows = key
