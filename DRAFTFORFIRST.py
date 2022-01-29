# Rinoa Malapaya, 100743955
# Aranya Satharsan,
# Sania Salim,100745490
# Denis Wagle,
# Kainat Rashid, 100752341
import random
from abc import ABC, abstractmethod


class Message(ABC):
    def __init__(self, message, num, alpha, key):
        self.message = message
        self.alpha = alpha
        self.key = key
        self.num = num


class PlainTextMsg(Message):  # class for encrypting
    def __init__(self, message, num, alpha, key):
        super().__init__(message, num, alpha, key)

    def OverAllEncrypt(self):
        if self.num == 1:  # --------------------------------------------------------------Kainat
            Text = self.message
            code = []
            encrypt = []
            space = ' '
            alpha = "abcdefghijklmnopqrstuvwxyz"
            for i in Text:
                symbol = alpha.find(i)
                if symbol == -1:
                    code.append(" ")
                else:
                    firstIndex = alpha.index(i)
                    newIndex = (firstIndex + self.key) % 26
                    encrypt.append(newIndex)
                    letter = alpha[newIndex]
                    code.append(letter)
            x = "".join(code)
            print(x)
            return x
        if self.num == 2:  # ----------------------------------------------------------------Aranya
            result = ''
            for c in self.message.lower():
                if c.isalpha():
                    result += self.key[ord(c) - ord('a')]
                else:
                    result += c
            # print(result)
            return result
        if self.num == 3:  # -------------------------------------------------------------------Denis
            ciphertext = [""] * self.key
            for column in range(self.key):
                pointer = column
                while pointer < len(self.message):
                    ciphertext[column] += self.message[pointer]
                    pointer += self.key
            # print("".join(ciphertext))
            return "".join(ciphertext)


class CipherTextMessage(Message):  # for decrypting
    def __init__(self, message, num, alpha, key):
        super().__init__(message, num, alpha, key)

    def OverallDecrypt(self):
        if self.num == 1:  # --------------------------------------------------------------------Kainat
            plainText = []
            decrypt = []
            space = ' '
            alpha = "abcdefghijklmnopqrstuvwxyz"
            for i in self.message:
                symbol = alpha.find(i)
                if symbol == -1:
                    plainText.append(" ")
                else:
                    firstIndex = alpha.index(i)
                    newIndex = (firstIndex - self.key) % 26
                    decrypt.append(newIndex)
                    letter = alpha[newIndex]
                    plainText.append(letter)
            ", ".join(plainText)
            print("".join(plainText))
            return plainText
        if self.num == 2:  # ---------------------------------------------------------------------Aranya
            result = ''
            for c in self.message.lower():
                if c.isalpha():
                    result += chr(ord('a') + self.key.find(c))
                else:
                    result += c
            print(result)
            return result
        if self.num == 3:  # -----------------------------------------------------------------------Denis
            newKey = len(self.message)
            plainText_length = 0

            for i in self.message:
                plainText_length += len(i)
            d_text = [""] * plainText_length

            for column in range(newKey):
                pointer = column
                word = self.message[column]
                c = 0

                while pointer < plainText_length:
                    d_text[pointer] = word[c]
                    pointer += newKey
                    c += 1
            print("".join(self.message))
            return d_text


# Sania
class PlayFair:
    def __init__(self, message):
        self.message = message
        self.message.upper()
        self.message.replace(" ", "")

    def grid(self, q, r, initial):
        return [[initial for i in range(q)] for j in range(r)]

    def overall(self):
        table = list()
        for x in self.message:
            if x not in table:
                if x == 'J':
                    table.append('I')
                else:
                    table.append(x)

        store = 0
        for i in range(65, 91):  # storing other character
            if chr(i) not in table:
                if i == 73 and chr(74) not in table:
                    table.append("I")
                    store = 1
                elif store == 0 and i == 73 or i == 74:
                    pass
                else:
                    table.append(chr(i))

        y = 0
        self.grid_value = self.grid(5, 5, 0)  # This will place all the alphabets in the key
        for i in range(0, 5):  # Making the 5x5 grind
            for j in range(0, 5):
                self.grid_value[i][j] = table[y]
                y += 1

    def location(self, x):  # getting location
        self.overall()
        location = list()
        if x == 'J':
            x = 'I'
        for i, j in enumerate(self.grid_value):
            for k, l in enumerate(j):
                if x == l:
                    location.append(i)
                    location.append(k)
                    return location

    def encrypt(self):  # Encrypts the Code; takes the original word and converts it into cipher text.
        self.message = self.message.upper()
        self.message = self.message.replace(" ", "")
        i = 0
        for s in range(0, len(self.message) + 1, 2):
            if s < len(self.message) - 1:
                if self.message[s] == self.message[s + 1]:
                    self.message = self.message[:s + 1] + 'X' + self.message[s + 1:]
        if len(self.message) % 2 != 0:
            self.message = self.message[:] + 'X'  # If something is repeated
        print(end='')
        while i < len(self.message):
            loc = list()
            loc = self.location(self.message[i])
            loc1 = list()
            loc1 = self.location(self.message[i + 1])
            if loc[1] == loc1[1]:
                print("{}{}".format(self.grid_value[(loc[0] + 1) % 5][loc[1]],
                                    self.grid_value[(loc1[0] + 1) % 5][loc1[1]]),
                      end=' ')
            elif loc[0] == loc1[0]:
                print("{}{}".format(self.grid_value[loc[0]][(loc[1] + 1) % 5],
                                    self.grid_value[loc1[0]][(loc1[1] + 1) % 5]),
                      end=' ')
            else:
                print("{}{}".format(self.grid_value[loc[0]][loc1[1]], self.grid_value[loc1[0]][loc[1]]), end=' ')
            i = i + 2


# Rinoa
class RSA:
    def __init__(self, message, d=None, n=None):
        self.message = message
        self.encryptedList = []
        self.d = d
        self.n = n

    # Generates a random prime number
    def getPrimeNum(self):
        # randomly generates numbers between 5 and 101
        while True:
            randomNum = random.randint(5, 102)
            if not self.checkPrime(randomNum):
                continue
            else:
                break
        return randomNum

    # Performs a primality test to verify if generated number is truly prime
    def checkPrime(self, randomNum):
        # 2 and 3 are the first second prime numbers
        if randomNum == 2 or randomNum == 3:
            return True
        # 2 is the first prime number, anything lower isn't considered
        if randomNum < 2:
            return False
        # if generated number (randomNum) is divisible by the following, it is not a prime number
        if randomNum % 3 == 0 or randomNum % 2 == 0:
            return False
        i = 5
        while i * i <= randomNum:
            if randomNum % i == 0:
                return False
            if randomNum % (i + 2) == 0:
                return False
            i += 6
        return True

    # Finds greatest common divisor
    def gcd(self, a, b):
        while b:
            tempA = a % b
            a = b
            b = tempA
        return a

    # Find the modular multiplicative inverse of e modulo φ(n)
    def modInv(self, a, m):
        g, x, y = self.extendedGCD(a, m)
        if g != 1:
            return None
        else:
            return x % m

    # Performs Extended Euclidean Algorithm; this is needed to calculate modINV
    def extendedGCD(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.extendedGCD(b % a, a)
            return g, x - (b // a) * y, y

    # Converts user's message to ASCII numbers
    def encryptStringASCII(self, message):
        listASCII = [ord(c) for c in message]
        return listASCII

    def encrypt(self):
        # Randomly choose two different prime #s (p, q)
        p = self.getPrimeNum()
        # Make sure p != q
        while True:
            q = self.getPrimeNum()
            if p != q:
                break
        # to verify: print("p:", p)
        # to verify: print("q:", q)

        # Generate the RSA modulus which is n
        self.n = p * q
        # to verify: print("n:", n)

        # Compute φ(n) by using Euler totient function
        phi = (p - 1) * (q - 1)
        # to verify: print("phi:", phi)

        # Attains an integer e (public key exponent) which fulfils the following two conditions:
        maxRange = phi - 1
        # ONE. 1 < e < φ(n)
        for x in range(2, maxRange):
            # TWO. Make sure e and φ(n) are coprime; using gcd(e, φ(n)) = 1
            if self.gcd(x, phi) == 1:
                e = x
        # to verify: print("e:", e)

        # Determine private key d
        self.d = self.modInv(e, phi)
        # to verify: print("d:", d)

        # To Verify:
        # public = (e, n)
        # private = (d, n)
        # print("Public Key:", public)
        # print("Private Key:", private)

        # In order to encrypt the given string to RSA, it has to be converted to ASCII numbers first
        converted = self.encryptStringASCII(self.message)
        # to verify: print("Plain text converted to ascii:", *converted, sep=" ")

        # To encrypt a message public key is needed (e, n)

        # i = message in ascii
        for i in converted:
            # Turns i (the plaintext message) into an integer i (padded plaintext)
            # Done by modular exponentiation: c = (i**e) % n
            c = pow(i, e, self.n)
            self.encryptedList.append(c)
        # Shows encrypted message
        # print("Encrypted Message:", *self.encryptedList, sep=" ")
        rsaEncrypt = ' '.join(map(str, self.encryptedList))
        return rsaEncrypt

    def decrypt(self):
        # To decrypt a message, private key is needed (d, n)
        decryptedList = []
        for x in self.encryptedList:
            # c is now x
            # recover m from x (initially c) by using her private key exponent d by computing
            # m = (x**d) % n
            m = pow(x, self.d, self.n)
            decryptedList.append(m)
        # to verify: print("Decrypted Message (in ASCII):", *decryptedList, sep=" ")

        # what we have right now is the decrypted message in ASCII, so this converts ASCII to plain text string
        convertedBack = ''.join(chr(i) for i in decryptedList)
        # print("Decrypted Message:", convertedBack)
        return convertedBack


def main():
    myDict = {}
    while True:
        alphaKainat = "abcdefghijklmnopqrstuvwxyz"
        keyAranya = "etaoinshrdlcumwfgypbvkjxqz"
        randomNumber = random.randint(1, 6)
        randomNumber = 6
        message = input("Enter a sentence: ")
        if message.lower() != "stop":
            if randomNumber == 1:
                print("Caesar")
                message = message.lower()
                EncryptCode = PlainTextMsg(message, randomNumber, alphaKainat, 2)
                encrypted = EncryptCode.OverAllEncrypt()
                DecryptCode = CipherTextMessage(encrypted, randomNumber, alphaKainat, 2)
                DecryptCode.OverallDecrypt()
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypted
                appliedMethod = 'Caesar'
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                print()
                continue
            if randomNumber == 2:
                print("Substitution")
                EncryptCode = PlainTextMsg(message, randomNumber, keyAranya, keyAranya)
                encrypting = EncryptCode.OverAllEncrypt()
                print(encrypting)
                DecryptCode = CipherTextMessage(encrypting, randomNumber, keyAranya, keyAranya)
                DecryptCode.OverallDecrypt()
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "Substitution"
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                print()
                continue
            if randomNumber == 3:  # Transpostition decrypt is printing the same thing idk
                print("Transposition")
                EncryptCode = PlainTextMsg(message, randomNumber, alphaKainat, 2)
                encrypting = EncryptCode.OverAllEncrypt()
                print(encrypting)
                DecryptCode = CipherTextMessage(message, randomNumber, alphaKainat, 2)
                DecryptCode.OverallDecrypt()
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "Transposition"
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                print()
                continue
            if randomNumber == 4:
                print("Product")
                EncryptCode = PlainTextMsg(message, 2, keyAranya, keyAranya)
                first = EncryptCode.OverAllEncrypt()
                EncryptCode = PlainTextMsg(first, 3, alphaKainat, 5)
                second = EncryptCode.OverAllEncrypt()
                print(second)
                Decrypt = CipherTextMessage(message, 3, alphaKainat, 2)
                Decrypt.OverallDecrypt()
                plainText = 'Plaintext Message : ' + message
                encryptedText = second
                appliedMethod = "Product"
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                print()
                continue
            if randomNumber == 5:
                print("RSA")
                code = RSA(message)
                encrypting = code.encrypt()
                print(encrypting)
                decrypting = code.decrypt()
                print(decrypting)
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "RSA"
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                print()
                continue
            if randomNumber == 6:
                print("Playfair")
                code = PlayFair(message)
                code.encrypt()
                # DECRYPTING NEEDED FOR PLAYFAIR
                plainText = 'Plaintext Message : ' + message
                encryptedText = code.encrypt()
                appliedMethod = "Playfair"
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                print(), print()
                continue
        else:
            if message.lower() == "stop":
                print()
                for key in myDict:
                    print(key)
                    for value in myDict[key]:
                        print(value, ':', myDict[key][value])
                    print()
            break


main()
