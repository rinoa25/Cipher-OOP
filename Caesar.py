def CaeserEncrypt(text,shift):
    Text=text.lower()
    code=[]
    encrypt=[]
    space=' '
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in Text:
        symbol = alpha.find(i)
        if symbol==-1:
            code.append(" ")
        else:
            firstIndex=alpha.index(i)
            newIndex=(firstIndex+shift)%26
            encrypt.append(newIndex)
            letter=alpha[newIndex]
            code.append(letter)
    ", ".join(code)
    print("".join(code))

def CaeserDecrypt(text,shift):
    Text=text.lower()
    plainText=[]
    decrypt=[]
    space = ' '
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in Text:
        symbol = alpha.find(i)
        if symbol == -1:
            plainText.append(" ")
        else:
            firstIndex=alpha.index(i)
            newIndex=(firstIndex-shift)%26
            decrypt.append(newIndex)
            letter=alpha[newIndex]
            plainText.append(letter)
    ", ".join(plainText)
    print("".join(plainText))

while True:
    test1=CaeserEncrypt("ok bye",2)
    test2=CaeserDecrypt("qm dag",2)

