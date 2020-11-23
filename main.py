import functions as fn

# задаём имена участникам
names = 'AB'

# генерируем закрытый, публичный ключи и число N для каждого пользователя из names
keys = {}
for i in names:
    keys[i] = fn.generatePublicAndSecretKeys(5)
# вывод ключей всех пользователей
for i in keys:
    print('key for', i, ' : ', keys[i])

# A шифрует сообщение для B. Для этого берёт открытый ключ и N пользователя B
M = ord('H')
d, e, N = keys['B']['d'], keys['B']['e'], keys['B']['N']

C = fn.power(M, e, N)

MO = fn.power(C, d, N)

print(e, N)

print(M, C, MO)
