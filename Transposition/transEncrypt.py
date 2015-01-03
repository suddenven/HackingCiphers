#Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = input('Message: ')
    myKey = int(input('Key: '))

    ciphertext = encryptMessage(myKey, myMessage)

    #Add a | to the end of the ciphertext

    print(ciphertext + '|')

    #Copy the string to the keyboard
    pyperclip.copy(ciphertext)

    
def encryptMessage(key, message):

    #Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    #Loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        #Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            #Place the character at pointer in message at the end of the
            #Current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            #move pointer over
            pointer += key + 1

    #Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

#If tranpositionEncrypt.py is run (instead of imported as a module) call
#the main() function
if __name__ == '__main__':
    main()
