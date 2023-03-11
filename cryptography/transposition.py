plaintext = ""
key = 8

ciphertext = [''] * key

for column in range(key):
    pointer = column

    while pointer < len(plaintext):
        ciphertext[column] += plaintext[pointer]
       #print(ciphertext)
        pointer += key
#print(ciphertext)
print(''.join(ciphertext))