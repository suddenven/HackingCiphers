#Caesar Cipher

import pyperclip

#The string to be encrypted
message = input('Enter message:')

#The encryption key
key = input('Enter an integer between 0 and 25, inclusive')

#Encrypt or Decrypt?
mode = input('Encrypt or Decrypt:')
mode = mode.lower()

#Every possible symbol
LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

#Stores the switched form of the message
translated = ''

#Capitalize the message
message = message.upper()

#Run the decryption code
for symbol in message:
    if symbol in LETTERS:
        #Get the number for this symbol
        num = LETTERS.find(symbol)
        if mode == 'encrypt'
