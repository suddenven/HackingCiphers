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

    # Number of "shaded boxes" in the last "column"
    numShadedBoxes = (numColumns * numRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numColumns

    # the col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numColumns) or (col == numColumns -1 and row >= numRows - numShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Makes the program run if it is run.

if __name__ == '__main__':
    main()
