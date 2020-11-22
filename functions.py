import random
import math
import sys
sys.setrecursionlimit(1500)
from math import gcd as bltin_gcd

# решето Эратосфена
def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False # Zero and one are not prime numbers.
    sieve[1] = False
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes

LOW_PRIMES = primeSieve(100)

# тест Миллера-Рабина
def MillerRabin(num):
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

# определение простое ли число
def isPrime(num):
    if (num < 2):
        return False
    for prime in LOW_PRIMES:
        if (num == prime):
            return True
        if (num % prime == 0):
            return False
    return MillerRabin(num)

# генерация большого простого числа
def randPrime(n):
    rangeStart = 10 ** (n-1)
    rangeEnd = (10 ** n) - 1
    while True:
        num = random.randint(rangeStart, rangeEnd)
        if isPrime(num):
            return num

# генерация m разных случайных простых больших чисел размерности n
def randDifferentPrime(m, n):
    arr = []
    arr.append(randPrime(n))
    m -= 1
    while (m >= 0):
        number = randPrime(n)
        for i in range(len(arr)):
            if arr[i] != number:
                arr.append(number)
                m -= 1
    return arr

# взаимнопростое с f число
def coprime(f):
    while True:
        prime = randPrime(len(str(f)) - 1)
        if math.gcd(f, prime) == 1:
            break
    return prime

# f * x - e * d = 1
# расширенный алгоритм Евклида
# def gcdex(a, b):
#     if b == 0:
#         return a, 1, 0
#     else:
#         d, x, y = gcdex(b, a % b)
#         return d, y, x - y * (a // b)

def gcdex(a, b, m, d = 1):
    a //= d
    b //= d
    m //= d

    newM = m

    arr = []
    while m != 1:
        arr += [float(m // a)]
        p = m
        m = a
        a = p - (p // a) * a

    pN_1, n = fct(arr)

    x0 = (((-1) ** (n - 1)) * pN_1 * b) % newM

    arrX = []
    for i in range(d):
        arrX.append(int(x0 + i * newM))
    return arrX

def fct(arr):
    global b
    if arr == []:
        return 'Null division', 0
    elif arr == [0.0]:
        return 0, b
    p = []
    q = []
    for i in range(len(arr)):
        q.append(0)
        p.append(0)
    p[0] = arr[0]
    p[1] = arr[0] * arr[1] + 1
    q[0] = 1
    q[1] = arr[1]
    for n in range(2,len(arr)):
        p[n] = arr[n] * p[n-1] + p[n-2]
        q[n] = arr[n] * q[n-1] + q[n-2]
    return p[-2], len(p)

# генерация публичного и закрытого ключей шифрования
def generatePublicAndSecretKey(size = 5):
    arrPQ = randDifferentPrime(2, size)
    n = arrPQ[0] * arrPQ[1] # произведение P и Q, часть ключей
    f = (arrPQ[0] - 1 ) * (arrPQ[1] - 1) # функция Эйлера
    e = coprime(f) # взаимнопростое с f число, часть открытого ключа

    d = gcdex(e, 1, f)[0]

    return e, d, n

# строка символов для шифрования
allCharacters = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# быстрый поиск модуля от степени числа
def power(x, n, mod):
    if n == 0:
        return 1
    elif n % 2 == 0:
        p = power(x, n / 2, mod)
        return (p * p) % mod
    else:
        return (x * power(x, n - 1, mod)) % mod

# шифрование исходного текста
def encryptText(e, n, text):
    encrypted = []
    for i in range(len(text)):
        index = allCharacters.index(text[i]) + 2
        encrypted.append(power(index, e, n))
    print('this is your encrypted text : ', indexesToText(encrypted))
    return encrypted

# расшифровка текста
def decryptText(d, n, textArray):
    # textArray = textToIndexes(textArray)
    decrypted = []
    for i in textArray:
        index = power(i, d, n) - 2
        decrypted.append(index)
    print('this is your decrypted text : ', indexesToText(decrypted))
    return decrypted

# перевод текста в индексы
def textToIndexes(text):
    textArray = []
    for i in range(len(text)):
        textArray.append(allCharacters.index(text[i]))
    return textArray

# перевод индексов в текст
def indexesToText(textArray):
    text = ''
    for i in textArray:
        text += allCharacters[i % len(allCharacters)]
    return text
