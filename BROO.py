code = input("Enter your message: ")
letters = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter your key: ").lower()
key = ""

x = ""
text = []
encrypt = ''

for i in code:
    position = letters.find(i)
    newposition = position+5
    encrypt += letters[newposition]
print(encrypt)

for char in code:
    if char in letters:
        x += char

for char in word:
    if char in letters:
        if char not in key:
            key += char #It will add the users keyword into the key being used, in the encryption method.

for char in letters: #after the user inputs its keyword it will then run through the letters and check to see which one was used
    if char not in key:
        key += char

def encrypt():
    values = [letters.index(char) for char in x]
    return "".join(key[indexKey] for indexKey in values)

print(encrypt())