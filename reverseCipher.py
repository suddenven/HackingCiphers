#Reverse Cipher

message = '.daed era meht fo owt fi ,terces a peek nac eerhT'

translated = ''

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
