#Aranya Sutharasn
#Substitution cipher
def encryptString(message, key):
    result = ''
    for c in message.lower():
        if c.isalpha():
            result += key[ord(c) - ord('a')]
        else:
            result += c
    return result

def decryptString(message, key):
    result = ''
    for c in message.lower():
        if c.isalpha():
            result += chr(ord('a') + key.find(c))
        else:
            result += c
    return result




def main():
    message = input("Enter a message: ")
    key = "etaoinshrdlcumwfgypbvkjxqz"
    secret = (encryptString(message, key))
    print ("Encrypted:", secret)
    plaintext = (decryptString(secret, key))
    print ("Decrypted:", plaintext)


main()

