import random
import string

name = input("enter your name: ")
print(f"hello {name}")

all_chars = string.ascii_letters + string.digits + string.punctuation + " "
all_chars = list(all_chars)

keys = all_chars.copy()


random.shuffle(keys)

print("-----Encryption-----")

plain_text = input("enter your message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = all_chars.index(letter)
    cipher_text += keys[index]


print(f"Encrypted message: {cipher_text}")


print("-----Decryption-----")

cipher_text = input("enter your message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += all_chars[index]

print(f"Decrypted message: {plain_text}")
# this is my Encryption program
