# Transposition Cipher Encrypt/Decrypt File

import time, os, sys
from transEncrypt import encryptMessage
from transDecrypt import decryptMessage

def main():
    inputFilename = input('File name: ')

    # Be careful. Tis will overwrite that file
    myMode = input('Encrypt or decrypt: ')
    myMode = myMode.lower()
    myKey = int(input('Key: '))

    # This sets the file name
    if myMode == 'encrypt':
        outputFilename = inputFilename + '.encrypted.txt'

    elif myMode == 'decrypt':
        outputFilename = inputFilename + '.decrypted.txt'
    
   

    # If the file does not exist, terminate early
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response =  input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileOBJ.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long it takes
    startTime = time.time()
    
