# Transposition Cipher Test

import random, sys, transEncrypt,transDecrypt

def main():
    random.seed(42) # set the random "seed" to a static value

    for i in range(20): # run 20 tests
        # Generate random messages to test.

        # The message will have a random length
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)

        # Convert the message string to a list to shuffle it.
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # Convert list to string

        print('Test #%s: "%s..."' % (i+1, message[:50]))

        # Check all possible keys for each message.
        for key in range(1, len(message)):
            encrypted = transEncrypt.encryptMessage(key, message)
            decrypted = transDecrypt.decryptMessage(key, encrypted)

            # If message and decrypted don't match, display an error message
            # and quit.

            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print(decrypted)

                sys.exit()

    print('Transposition cipher test passed.')

# Make it run as a program
if __name__ == '__main__':
    main()
