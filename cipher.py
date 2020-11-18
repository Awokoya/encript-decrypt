#from math import random
import random
from cryptography.fernet import Fernet, InvalidToken

def generate_key():
     #generates keys and saves it to a file
    key = Fernet.generate_key()
    with open("secret.txt", "wb") as key_file:
        key_file.write(key)

def load_key():
    #load key
    return open("secret.key", "rb").read()

def encrypt_message(message):
     #encrypt message
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print("ciphered text : ",encrypted_message)

def decrypt(text):
    t = text.encode()
    key = load_key()
    f = Fernet(key)
    try:
        print ("\nValid key.Decrypted message: ", f.decrypt(t).decode())
    #to catch all errors like invalid key or text
    except InvalidToken as e:
        print("Decryption Unsuccessful")

#def decode_message (text):


def main ():
    generate_key()
    message = input("Enter in the message you want to encode: ")
    encrypt_message(message)
    text = input("Enter in the message you want to decode: ")
    decrypt(text)

main()
