# Transposition Cipher Encrypt/Decrypt File

import time, os, sys
from transEncrypt import encryptMessage
from transDecrypt import decryptMessage

def main():
    inputFilename = input('File name: ')
    inputFilename = inputFilename[:len(inputFilename) - 4]
    

    # Be careful. Tis will overwrite that file
    myMode = input('Encrypt or decrypt: ')
    myMode = myMode.lower()
    myKey = int(input('Key: '))

    # This sets the file name
    if myMode == 'encrypt':
        outputFilename = inputFilename + '.encrypted.txt'

    if myMode == 'decrypt':
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
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long it takes
    startTime = time.time()
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))
    
    # write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' (myMode.title(), str(outputFilename)))

# Make it run
if __name__ == '__main__':
    main() 
