# Sania Salim
# 100745490

word = str(input("Enter your key word: "))
word = word.upper()
word = word.replace(" ", "")


def grid(q, r, initial):
    return [[initial for i in range(q)] for j in range(r)]


table = list()
for x in word:
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
grid_value = grid(5, 5, 0)  # This will place all the alphabets in the key
for i in range(0, 5):  # Making the 5x5 grind
    for j in range(0, 5):
        grid_value[i][j] = table[y]
        y += 1


def location(x):  # getting location
    location = list()
    if x == 'J':
        x = 'I'
    for i, j in enumerate(grid_value):
        for k, l in enumerate(j):
            if x == l:
                location.append(i)
                location.append(k)
                return location


def encrypt():  # #Encryptes the Code; takes the original word and converts it into cipher text.
    code = str(input("Enter your message: "))
    code = code.upper()
    code = code.replace(" ", "")
    i = 0
    for s in range(0, len(code) + 1, 2):
        if s < len(code) - 1:
            if code[s] == code[s + 1]:
                code = code[:s + 1] + 'X' + code[s + 1:]
    if len(code) % 2 != 0:
        code = code[:] + 'X'  # If something is repeated
    print("Your cipher text: ", end=' ')
    while i < len(code):
        loc = list()
        loc = location(code[i])
        loc1 = list()
        loc1 = location(code[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(grid_value[(loc[0] + 1) % 5][loc[1]], grid_value[(loc1[0] + 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(grid_value[loc[0]][(loc[1] + 1) % 5], grid_value[loc1[0]][(loc1[1] + 1) % 5]), end=' ')
        else:
            print("{}{}".format(grid_value[loc[0]][loc1[1]], grid_value[loc1[0]][loc[1]]), end=' ')
        i = i + 2


def decrypt():  # decryptes the code; takes the cipher text and converts it into place
    code = str(input("Enter your cipher text: "))
    code = code.upper()
    code = code.replace(" ", "")
    print("Your plain text: ", end=' ')
    i = 0
    while i < len(code):
        loc = list()
        loc = location(code[i])
        loc1 = list()
        loc1 = location(code[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(grid_value[(loc[0] - 1) % 5][loc[1]], grid_value[(loc1[0] - 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(grid_value[loc[0]][(loc[1] - 1) % 5], grid_value[loc1[0]][(loc1[1] - 1) % 5]), end=' ')
        else:
            print("{}{}".format(grid_value[loc[0]][loc1[1]], grid_value[loc1[0]][loc[1]]), end=' ')
        i = i + 2


while (1):
    user_input = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if user_input == 1:
        encrypt()
    elif user_input == 2:
        decrypt()
    elif user_input == 3:
        exit()
    else:
        print("Choose correct choice")
