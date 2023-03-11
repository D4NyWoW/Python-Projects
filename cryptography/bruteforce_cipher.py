

message ='GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = 'ABCDEFGHIJKMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)): # loop through every possible key
    translated = ''

    #encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)
            
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol # add the symbol without encryption/decryption
    print(f'Key #{key}: {translated}')