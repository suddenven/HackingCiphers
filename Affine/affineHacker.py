# Affine Cipher Hacker
#

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    # this is copied
    # from the website
    myMessage = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG'<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        # The plaintext is displayed on the screen. For the convenience of
        # the user, we copy the text of the code to the clipboard.
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


    
