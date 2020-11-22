import functions as fn

e, d, n = fn.generatePublicAndSecretKey()
print('e: ', e)
print('d: ', d)
print('n: ', n)

print('\n')

text = 'привки, чувакк'

encrypted = fn.encryptText(e, n, text)

decrypted = fn.decryptText(d, n, encrypted)

print('\n')

print('Text in indexes : ', fn.textToIndexes(text))

print('Encrypted text  : ', encrypted)

print('Decrypted text  : ', decrypted)
