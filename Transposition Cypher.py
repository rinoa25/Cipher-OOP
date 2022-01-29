def encrypt(plaintext, key):
    ciphertext = [""] * key

    for coloum in range(key):

        pointer = coloum

        while pointer < len(plaintext):
            ciphertext[coloum] += plaintext[pointer]

            pointer += key

    return ciphertext


def decrypt(e_text):
    key = len(e_text)

    plaintext_length = 0

    for i in e_text:
        plaintext_length += len(i)

    d_text = [""] * plaintext_length

    for coloum in range(key):

        pointer = coloum

        word = e_text[coloum]

        c = 0

        while pointer < plaintext_length:
            d_text[pointer] = word[c]

            pointer += key

            c += 1

    return d_text


plaintext = str(input("Enter your message:"))

e_text = encrypt(plaintext, 8)

print("".join(e_text))

d_text = decrypt(e_text)


print("".join(d_text))