# Simple sub cipher
#

import sys
import random
import pyperclip


LETTERS = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXY
Z[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. the origin of myths is explained in this way. -Bertrand Russel'
    myKey = r"""/{9@6hUf:q?_)^eTi|W1,NLD7xk(-
SF>Iz0E=d;Bu#c]w~'VvHKmpJ+}s8y& XtP43.b[OA!*\Q<M%$ZgG52YloaRCn"`rj"""
    myMode = 'encrypt'

    checkValidKey(myKey)

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard')


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. we
        # just need to swap where the key and LETTERS strings are used
        charsA, charsB = charsB, charsA

    # Loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/Decrypt the symbol
            symIndex = charsA.find(symbol)
            translated += charsB[symIndex]
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()