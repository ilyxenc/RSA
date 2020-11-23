import functions as fn

# задаём имена участникам
names = 'AB'

# генерируем закрытый, публичный ключи и число N для каждого пользователя из names
keys = {}
for i in names:
    keys[i] = fn.generatePublicAndSecretKeys()
# вывод ключей всех пользователей
for i in keys:
    print('key for', i, ' : ', keys[i])

# A шифрует сообщение для B. Для этого берёт открытый ключ и N пользователя B
M = 'Hello'
print('original message        :', M)

d, e, N = keys['B']['d'], keys['B']['e'], keys['B']['N']

# получение зашифрованного сообщения для пользователя B с помощью ключа e и числа N пользователя B
encrypted, encryptedText = fn.encrypt(M, e, N)
print('encrypted message for B :', encryptedText)

# получение расшифрованного сообщения пользователем B с помощью ключа d и числа N
decrypted, decryptedText = fn.decrypt(encrypted, d, N)
print('B`s decrypted message   :', decryptedText)
