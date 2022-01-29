# BACKGROUND INFO

# encryption key = public
# decryption key = private

# factoring the product of two large prime numbers

# user of RSA creates and then publishes a public key
# which is based on 2 large prime numbers (must be kept a secret)

# anyone can use the public key to encrypt a message
# but only someone with the knowledge of the prime #s can decode the message

# _______________________________________________________________________________

# OPERATION OF THE WORKINGS OF RSA

# RSA Algorithm involves 4 steps:
# Key generation, Key distribution, Encryption, Decryption

# Equation in wiki about e, d, n, m

# KEY GENERATION

# 1. Randomly choose two different prime #s (p, q)
# Chosen randomly for security purposes
# #s are kept a secret

# 2. Generate the RSA modulus which is n (by computing n = pq)
# n is used as the modulus for both private and public keys
# its length, usually expressed in bits, is the key length
# n is released as part of the public key

# 3. Calculate the private exponent d (by using, in this case, Euler totient function)
# φ(n) = (p − 1)(q − 1)
# φ(n) is kept secret

# 4. Choose an integer e
# which fulfills the following conditions:  1 < e < φ(n) and e is coprime with φ(n)
# The smallest (and fastest) possible value for e is 3
# e is released as part of the public key

# 5. Determine d by finding the modular multiplicative inverse of e modulo φ(n)
# as said before, d is kept secret as the private key exponent

# The public key consists of the modulus n and the public (or encryption) exponent e
# The private key consists of the private (or decryption) exponent d, which must be kept secret
# p, q, and φ(n) must also be kept secret because they can be used to calculate d

# KEY DISTRIBUTION
# public key is used to encrypt messages
# private key used to decrypt messages
# In order for person 1 to send their encrypted message to person 2
# person 2 has to send their public key (n, e) to person 1
# person 2's private key (d) is never transmitted / distributed

# ENCRYPTION
# Turn M (the plaintext message) into an integer m (padded plaintext)
# Done by modular exponentiation

# DECRYPTION
# recover m from c by using her private key exponent d by computing
