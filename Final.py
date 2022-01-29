from abc import ABC, abstractmethod
import random


class Message(ABC):
    # Contains attributes (variables) and methods (functions) that could be used to apply a cipher
    # to a string, either to encrypt or to decrypt a message.
    def __init__(self, m):
        self.m = m

    # Method used to apply to RSA cipher
    def getPrimeNum(self):
        # randomly generates numbers between 5 and 101
        while True:
            randomNum = random.randint(5, 102)
            if not self.checkPrime(randomNum):
                continue
            else:
                break
        return randomNum

    # Method used to apply to RSA cipher
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

    # Method used to apply to RSA cipher
    # Finds greatest common divisor
    def gcd(self, a, b):
        while b:
            tempA = a % b
            a = b
            b = tempA
        return a

    # Method used to apply to RSA cipher
    # Find the modular multiplicative inverse of e modulo φ(n)
    def modInv(self, a, m):
        g, x, y = self.extendedGCD(a, m)
        if g != 1:
            return None
        else:
            return x % m

    # Method used to apply to RSA cipher
    # Performs Extended Euclidean Algorithm; this is needed to calculate modINV
    def extendedGCD(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.extendedGCD(b % a, a)
            return g, x - (b // a) * y, y

    # Method used to apply to RSA cipher
    # Randomly choose two different prime #s (p, q)
    def twoDiffPrimeNums(self):
        p = self.getPrimeNum()
        # Make sure p != q
        while True:
            q = self.getPrimeNum()
            if p != self.q:
                break
        self.p = p
        self.q = q
        # to verify: print("p:", p)
        # to verify: print("q:", q)

    @abstractmethod
    # Method used to apply to RSA cipher
    # Gets the components for RSA public key (e, n); needed for encryption
    def rsaPublicKey(self):
        # Compute φ(n) by using Euler totient function
        phi = (self.p - 1) * (self.q - 1)
        # to verify: print("phi:", phi)
        self.phi = phi

        # Attains an integer e (public key exponent) which fulfils the following two conditions:
        maxRange = self.phi - 1
        # ONE. 1 < e < φ(n)
        for x in range(2, maxRange):
            # TWO. Make sure e and φ(n) are coprime; using gcd(e, φ(n)) = 1
            if self.gcd(x, self.phi) == 1:
                e = x
        # to verify: print("e:", e)
        self.e = e

        # Generate the RSA modulus which is n
        n = self.p * self.q
        self.n = n

        # To Verify:
        # public = (e, n)
        # print("Public Key:", public)

    @abstractmethod
    # Method used to apply to RSA cipher
    # Gets the components for RSA private key (d, n); needed for decryption
    def rsaPrivateKey(self):
        # Determine private key d
        d = self.modInv(self.e, self.phi)
        # to verify: print("d:", d)

        # Generate the RSA modulus which is n
        n = self.p * self.q
        self.n = n
        # to verify: print("n:", n)

        # To Verify:
        # private = (d, n)
        # print("Private Key:", private)


# Class's Purpose: Has attributes and methods to ENCRYPT a message.
class PlainTextMsg(Message):

    def __init__(self, m):
        super().__init__(m)

    def rsaPublicKey(self):
        super().rsaPublicKey()
        print("ok")

    def rsaEncryption(self):
        # Converts user's message to ASCII numbers
        converted = [ord(c) for c in self.m]
        # to verify: print("Plain text converted to ascii:", *converted, sep=" ")

        # To encrypt a message public key is needed (e, n)
        encryptedList = []
        # i = message in ascii
        for i in converted:
            # Turns i (the plaintext message) into an integer i (padded plaintext)
            # Done by modular exponentiation: c = (i**e) % n
            c = pow(i, self.e, self.n)
            encryptedList.append(c)
        # Shows encrypted message
        print("Encrypted Message:", *encryptedList, sep=" ")

    # Displays the original message and the encrypted version of it.
    def displayMsges(self):
        pass


# Class's Purpose: Contains a method used to DECRYPT a message
class CipherTextMsg(Message):

    def __init__(self, m):
        super().__init__(m)

    def rsaPrivateKey(self):
        super().rsaPrivateKey()
        print("ok")

    def rsaDecryption(self):
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
        print("Decrypted Message:", convertedBack)


def main():
    # Randomly generates numbers between 1 and 6 (there are 6 ciphers available)
    encryptionChoice = random.randint(1, 6)
    m = input("Enter a sentence: ")
    if m == "Stop":
        # Displays all the plaintext messages, the encrypted versions and the applied method
        pass
    else:
        # testing for   rsa first
        encryptCode = PlainTextMsg(m)
        encryptCode.rsaEncryption()
        decryptCode = CipherTextMsg(m)
        decryptCode.rsaDecryption()


# Calls main function
if __name__ == '__main__':
    main()
