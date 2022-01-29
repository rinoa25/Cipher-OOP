# Rinoa Malapaya, 100743955: RSA cipher, Product cipher, Main
# Aranya Sutharsan, 100748986: Substitution cipher, Documentation
# Sania Salim,100745490: Playfair cipher, Documentation
# Denis Wagle, 100756476: Transposition cipher, Documentation
# Kainat Rashid, 100752341: Caesar cipher, Main

# The purpose of this program is to recieve a message from the user and then encrypt it through a random cipher
# and decrypt it back for the user

import random
from abc import ABC, abstractmethod


class Message(ABC):  # An abstract class to be inherited by the other classes with values already inputted
    def __init__(self, message, num, alpha, key):
        self.message = message
        self.alpha = alpha
        self.key = key
        self.num = num


class PlainTextMsg(Message):  # class for encrypting
    def __init__(self, message, num, alpha, key):
        super().__init__(message, num, alpha, key)  # inheriting Message classes variables

    def OverAllEncrypt(self):  # this class encrypts the given message for the randomly picked number
        if self.num == 1:  # this is the caesar code encryption
            Text = self.message
            code = []
            encrypt = []
            alpha = "abcdefghijklmnopqrstuvwxyz"
            for i in Text:  # this loop finds spaces and puts a space in the encrypted version too
                symbol = alpha.find(i)
                if symbol == -1:
                    code.append(" ")
                else:
                    firstIndex = alpha.index(i)
                    newIndex = (firstIndex + self.key) % 26  # this shifts the index by the key
                    encrypt.append(newIndex)
                    letter = alpha[newIndex]  # the new letter is found from this shifted indec
                    code.append(letter)
            x = "".join(code)
            print(x)
            return x
        if self.num == 2:  # this is the substitution code
            result = ''
            # Loop through each letter in the message
            for c in self.message.lower():
                if c.isalpha():
                    # Replacing the letter from the key list
                    result += self.key[ord(c) - ord('a')]
                else:
                    result += c
            # print(result)
            return result
        if self.num == 3:  # this is transpostion code
            ciphertext = [""] * self.key  # Generates the list with empty elements for the number of key set
            for column in range(self.key):  # for column in the range of key
                pointer = column  # both will be 0 untill they reach one number below the key. this is because the the cipler starts from 0-7 instead of 1-8
                while pointer < len(self.message):  # if the pointer is less than the lenghth of the text
                    ciphertext[column] += self.message[pointer]  # the ciphertext coloumn is equal to message
                    pointer += self.key  # pointer is equal to pointer + key
            # print("".join(ciphertext))
            return "".join(ciphertext)


class CipherTextMessage(Message):  # class for decrypting
    def __init__(self, message, num, alpha, key):
        super().__init__(message, num, alpha, key)  # inheriting the Message class variables

    def OverallDecrypt(self):
        if self.num == 1:  # Decryption for Caesar code
            plainText = []
            decrypt = []
            alpha = "abcdefghijklmnopqrstuvwxyz"
            for i in self.message:
                symbol = alpha.find(i)  # finding any spaces in the encrypted text to put in the decrypted text
                if symbol == -1:
                    plainText.append(" ")
                else:
                    firstIndex = alpha.index(i)
                    newIndex = (
                                       firstIndex - self.key) % 26  # this shifts the index by given key back to original version
                    decrypt.append(newIndex)
                    letter = alpha[newIndex]
                    plainText.append(letter)
            ", ".join(plainText)
            print("".join(plainText))
            return plainText
        if self.num == 2:  # this is the substitution code decryption
            result = ''
            # Loop through each letter in the message
            for c in self.message.lower():
                if c.isalpha():
                    # Replaces the encrpyted letters from the key list to its original letters
                    result += chr(ord('a') + self.key.find(c))
                else:
                    result += c
            print(result)
            return result
        if self.num == 3:  # this is the transposition code decryption
            newKey = len(self.message)  # key is set to the length of the message
            plainText_length = 0  # starts counting from 0

            for i in self.message:
                plainText_length += len(i)  # to decrypt the message, this finds the length of the plaintext
            decryption = [""] * plainText_length  # list multiplied by the length of the plaintext

            for column in range(newKey):  # for column in the range of key
                pointer = column  # both start from 0 untill they reach the key
                word = self.message[column]
                c = 0

                while pointer < plainText_length:  # executes till pointer is less than plain text
                    decryption[pointer] = word[c]
                    pointer += newKey
                    c += 1
            print("".join(self.message))
            return decryption  # returns the decrypted text


class PlayFair:  # this class is for the encryption and decryption of the playfair cipher
    def __init__(self, word):
        self.word = word
        self.word.upper()  # Converting letters into upper case
        self.word.replace(" ", "")

    def grid(self, q, r, initial):  # this method creates a grid with given values
        return [[initial for i in range(q)] for j in range(r)]

    def overall(self):  # this method goes through the key word
        table = list()  # Creating a new list
        for x in self.word:
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
        if x == 'J':  #
            x = 'I'
        for i, j in enumerate(self.grid_value):
            for k, l in enumerate(j):
                if x == l:
                    location.append(i)
                    location.append(k)
                    return location

    def encrypt(self, message):  # #Encryptes the Code; takes the original word and converts it into cipher text.
        self.message = message
        i = 0  # grouping them
        for s in range(0, len(self.message) + 1, 2):  # deleting unused spaces
            if s < len(self.message) - 1:
                if self.message[s] == self.message[s + 1]:
                    self.message = self.message[:s + 1] + 'X' + self.message[s + 1:]
        if len(self.message) % 2 != 0:  # putting the coded message into pairs
            self.message = self.message[:] + 'X'  # If something is repeated add a X after the letter
        print("Your cipher text: ", end=' ')
        while i < len(self.message):  # a while loop to go through message
            place = list()
            place = self.location(self.message[i])
            place1 = list()
            place1 = self.location(self.message[i + 1])
            if place[1] == place1[1]:
                print("{}{}".format(self.grid_value[(place1[0] + 1) % 5][place1[1]],  # finding the modulus with 5
                                    self.grid_value[(place[0] + 1) % 5][place[1]]),
                      end=' ')
                return (self.grid_value[(place1[0] + 1) % 5][place1[1]],
                        self.grid_value[(place[0] + 1) % 5][place[1]])
            elif place[0] == place1[0]:
                print("{}{}".format(self.grid_value[place[0]][(place[1] + 1) % 5],
                                    self.grid_value[place1[0]][(place1[1] + 1) % 5]),
                      end=' ')
                return (self.grid_value[place[0]][(place[1] + 1) % 5],
                        self.grid_value[place1[0]][(place1[1] + 1) % 5])
            else:
                print("{}{}".format(self.grid_value[place[0]][place1[1]],
                                    self.grid_value[place1[0]][place[1]]),
                      end=' ')
                return (self.grid_value[place[0]][place1[1]],
                        self.grid_value[place1[0]][place[1]])

            i = i + 2  # takes you to every second character

    def decrypt(self, code):  # decryptes the code; takes the cipher text and converts it into place
        print("\n")
        self.code = code
        i = 0
        while i < len(self.code):
            place = list()
            place = self.location(self.code[i])
            place1 = list()
            place1 = self.location(self.code[i + 1])
            if place[1] == place1[1]:
                print("{}{}".format(self.grid_value[(place[0] - 1) % 5][place[1]],  # function to find modulus with 5
                                    self.grid_value[(place1[0] - 1) % 5][place1[1]]),
                      end=' ')
            elif place[0] == place1[0]:
                print("{}{}".format(self.grid_value[place[0]][(place[1] - 1) % 5],
                                    self.grid_value[place1[0]][(place1[1] - 1) % 5]),
                      end=' ')
            else:
                print("{}{}".format(self.grid_value[place[0]][place1[1]],
                                    self.grid_value[place1[0]][place[1]]),
                      end=' ')
            i = i + 2


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
        # Used to decide which cipher is applied
        randomNumber = random.randint(1, 6)

        # User is asked to input a sentence for it to be encrypted / decrypted
        message = input("Enter a sentence: ")

        # While user does not input stop, program will keep asking user to enter a sentence for it to be encrypted /
        # decrypted
        def CipherExceptions():
            try:
                shift = input("What number would you like the key to be?")
            except TypeError:
                print("Enter numerical value")
            else:
                return shift

        if message.lower() != "stop":
            if randomNumber == 1:
                shift = CipherExceptions()
                message = message.lower()
                # Prints the encrypted version of the plain text in Caesar
                EncryptCode = PlainTextMsg(message, randomNumber, alphaKainat, int(shift))
                encrypted = EncryptCode.OverAllEncrypt()
                # Prints the decrypted version of the encrypted text in Caesar
                DecryptCode = CipherTextMessage(encrypted, randomNumber, alphaKainat, int(shift))
                DecryptCode.OverallDecrypt()
                # Variables for the dictionary
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypted
                appliedMethod = 'Caesar'
                # every encryption is added to the dictionary (this includes its plaintext and applied method)
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                # Continues to the top of the loop and asks the user for a sentence again
                print()
                continue
            if randomNumber == 2:
                # Prints the encrypted version of the plain text in Substitution
                EncryptCode = PlainTextMsg(message, randomNumber, keyAranya, keyAranya)
                encrypting = EncryptCode.OverAllEncrypt()
                print(encrypting)
                # Prints the decrypted version of the encrypted text in Substitution
                DecryptCode = CipherTextMessage(encrypting, randomNumber, keyAranya, keyAranya)
                DecryptCode.OverallDecrypt()
                # Variables for the dictionary
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "Substitution"
                # every encryption is added to the dictionary (this includes its plaintext and applied method)
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                # Continues to the top of the loop and asks the user for a sentence again
                print()
                continue
            if randomNumber == 3:
                # print("Transposition")
                # Prints the encrypted version of the plain text in Transposition
                EncryptCode = PlainTextMsg(message, randomNumber, alphaKainat, 2)
                encrypting = EncryptCode.OverAllEncrypt()
                print(encrypting)
                # Prints the decrypted version of the encrypted text in Transposition
                DecryptCode = CipherTextMessage(message, randomNumber, alphaKainat, 2)
                DecryptCode.OverallDecrypt()
                # Variables for the dictionary
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "Transposition"
                # every encryption is added to the dictionary (this includes its plaintext and applied method)
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                # Continues to the top of the loop and asks the user for a sentence again
                print()
                continue
            if randomNumber == 4:
                # print("Product")
                # Prints the encrypted version of the plain text in Product
                EncryptCode = PlainTextMsg(message, 2, keyAranya, keyAranya)
                first = EncryptCode.OverAllEncrypt()
                EncryptCode = PlainTextMsg(first, 3, alphaKainat, 5)
                second = EncryptCode.OverAllEncrypt()
                print(second)
                # Prints the decrypted version of the encrypted text in Product
                Decrypt = CipherTextMessage(message, 3, alphaKainat, 2)
                Decrypt.OverallDecrypt()
                # Variables for the dictionary
                plainText = 'Plaintext Message : ' + message
                encryptedText = second
                appliedMethod = "Product"
                # every encryption is added to the dictionary (this includes its plaintext and applied method)
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                # Continues to the top of the loop and asks the user for a sentence again
                print()
                continue
            if randomNumber == 5:
                # print("RSA")
                # Prints the encrypted version of the plain text in RSA
                code = RSA(message)
                encrypting = code.encrypt()
                print(encrypting)
                # Prints the decrypted version of the encrypted text in RSA
                decrypting = code.decrypt()
                print(decrypting)
                # Varaibles for the dictionary
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "RSA"
                # every encryption is added to the dictionary (this includes its plaintext and applied method)
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                # Continues to the top of the loop and asks the user for a sentence again
                print()
                continue
            if randomNumber == 6:
                word = str(input("Enter your key word: "))
                word = word.upper()
                word = word.replace(" ", "")
                obj1 = PlayFair(word)
                code = message
                code = code.upper()
                code = code.replace(" ", "")
                encrypting = obj1.encrypt(code)
                obj1.decrypt(encrypting)
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "Playfair"
                # every encryption is added to the dictionary (this includes its plaintext and applied method)
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                # Continues to the top of the loop and asks the user for a sentence again
                print(), print()
                continue
        else:
            # When user enters stop, program will stop the loop and will then iterate through the updated dictionary
            if message.lower() == "stop":
                print()
                # Prints every encryption made, it's plain text and applied method
                for key in myDict:
                    print(key)
                    for value in myDict[key]:
                        print(value, ':', myDict[key][value])
                    print()
            break


main()
