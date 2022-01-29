# Student Name: Rinoa Malapaya
# Student Number: 100743955
# RSA

import random


# Generates a random prime number
def getPrimeNum():
    # randomly generates numbers between 5 and 101
    while True:
        randomNum = random.randint(5, 102)
        if not checkPrime(randomNum):
            continue
        else:
            break
    return randomNum


# Performs a primality test to verify if generated number is truly prime
def checkPrime(randomNum):
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
def gcd(a, b):
    while b:
        tempA = a % b
        a = b
        b = tempA
    return a


# Find the modular multiplicative inverse of e modulo φ(n)
def modInv(a, m):
    g, x, y = extendedGCD(a, m)
    if g != 1:
        return None
    else:
        return x % m


# Performs Extended Euclidean Algorithm; this is needed to calculate modINV
def extendedGCD(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extendedGCD(b % a, a)
        return g, x - (b // a) * y, y


# Converts user's message to ASCII numbers
def encryptStringASCII(message):
    listASCII = [ord(c) for c in message]
    return listASCII


def main():
    # Randomly choose two different prime #s (p, q)
    p = getPrimeNum()
    # Make sure p != q
    while True:
        q = getPrimeNum()
        if p != q:
            break
    # to verify: print("p:", p)
    # to verify: print("q:", q)

    # Generate the RSA modulus which is n
    n = p * q
    # to verify: print("n:", n)

    # Compute φ(n) by using Euler totient function
    phi = (p - 1) * (q - 1)
    # to verify: print("phi:", phi)

    # Attains an integer e (public key exponent) which fulfils the following two conditions:
    maxRange = phi - 1
    # ONE. 1 < e < φ(n)
    for x in range(2, maxRange):
        # TWO. Make sure e and φ(n) are coprime; using gcd(e, φ(n)) = 1
        if gcd(x, phi) == 1:
            e = x
    # to verify: print("e:", e)

    # Determine private key d
    d = modInv(e, phi)
    # to verify: print("d:", d)

    # To Verify:
    # public = (e, n)
    # private = (d, n)
    # print("Public Key:", public)
    # print("Private Key:", private)

    # Asks user to enter a message
    message = input("Enter your message: ")
    # In order to encrypt the given string to RSA, it has to be converted to ASCII numbers first
    converted = encryptStringASCII(message)
    # to verify: print("Plain text converted to ascii:", *converted, sep=" ")

    # To encrypt a message public key is needed (e, n)
    encryptedList = []
    # i = message in ascii
    for i in converted:
        # Turns i (the plaintext message) into an integer i (padded plaintext)
        # Done by modular exponentiation: c = (i**e) % n
        c = pow(i, e, n)
        encryptedList.append(c)
    # Shows encrypted message
    print("Encrypted Message:", *encryptedList, sep=" ")

    # To decrypt a message, private key is needed (d, n)
    decryptedList = []
    for x in encryptedList:
        # c is now x
        # recover m from x (initially c) by using her private key exponent d by computing
        # m = (x**d) % n
        m = pow(x, d, n)
        decryptedList.append(m)
    # to verify: print("Decrypted Message (in ASCII):", *decryptedList, sep=" ")

    # what we have right now is the decrypted message in ASCII, so this converts ASCII to plain text string
    convertedBack = ''.join(chr(i) for i in decryptedList)
    print("Decrypted Message:", convertedBack)


# Calls main function
if __name__ == '__main__':
    main()
