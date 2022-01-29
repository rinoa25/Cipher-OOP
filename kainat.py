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
            return (x)
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
        if self.num == 5:  # -------------------------------------------------------------------Rinoa
            pass
        if self.num == 6:  # --------------------------------------------------------------------Sania
            pass


class CipherTextMessage(Message):
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
            key = len(self.message)
            plaintext_length = 0
            for i in self.message:
                plaintext_length += len(i)
            d_text = [""] * plaintext_length
            for column in range(key):
                pointer = column
                word = self.message[column]
                c = 0
                while pointer < plaintext_length:
                    d_text[pointer] = word[c]
                    pointer += key
                    c += 1
            print("".join(d_text))
            return d_text
        if self.num == 5:  # ----------------------------------------------------------------Rinoa
            pass
        if self.num == 6:  # ----------------------------------------------------------------Sania
            pass


def main():
    myDict = {}
    while True:
        alphaKainat = "abcdefghijklmnopqrstuvwxyz"
        keyAranya = "etaoinshrdlcumwfgypbvkjxqz"
        randomNumber = random.randint(1, 4)
        randomNumber = 3
        message = input("Enter a sentence: ")
        if message != "Stop":
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
                EncryptCode = PlainTextMsg(message, randomNumber, alphaKainat, 3)
                encrypting = EncryptCode.OverAllEncrypt()
                print(encrypting)
                DecryptCode = CipherTextMessage(encrypting, randomNumber, alphaKainat, 3)
                DecryptCode.OverallDecrypt()
                plainText = 'Plaintext Message : ' + message
                encryptedText = encrypting
                appliedMethod = "Transposition"
                myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                print()
                continue
            if randomNumber == 4:
                print("Product")
                randomNumber2 = random.randint(1, 2)
                if randomNumber2 == 1:
                    EncryptCode = PlainTextMsg(message, 2, keyAranya, keyAranya)
                    first = EncryptCode.OverAllEncrypt()
                    EncryptCode = PlainTextMsg(first, 3, alphaKainat, 5)
                    second = EncryptCode.OverAllEncrypt()
                    print(second)
                    print(message)
                    plainText = 'Plaintext Message : ' + message
                    encryptedText = second
                    appliedMethod = "Product"
                    myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                    print()
                    continue
                else:
                    EncryptCode = PlainTextMsg(message, 3, alphaKainat, 5)
                    first = EncryptCode.OverAllEncrypt()
                    EncryptCode = PlainTextMsg(first, 2, keyAranya, keyAranya)
                    second = EncryptCode.OverAllEncrypt()
                    print(second)
                    print(message)
                    plainText = 'Plaintext Message : ' + message
                    encryptedText = second
                    appliedMethod = "Product"
                    myDict[plainText] = {'Encrypted Version': encryptedText, 'Applied Method': appliedMethod}
                    print()
                    continue
        else:
            if message.lower() == "Stop":
                print()
                for key in myDict:
                    print(key)
                    for value in myDict[key]:
                        print(value, ':', myDict[key][value])
                    print()
            break


main()
