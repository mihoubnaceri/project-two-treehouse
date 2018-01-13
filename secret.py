from keywords import KeyWords
from atbash import Atbash
from keywords import KeyWords
from affine import Affine
from caesar import Caesar
import os


def clear():
    # clears screen
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    print()
    print("This is the Secret Messages project for Treehouse  \n")
    cipher_text = None
    print("These are the current available ciphers:\n")
    ciphers = ["Caesar", "Atbash", "Keyword", "Affine"]
    for cipher in ciphers:
        print("- {}".format(cipher))
    while True:

        answer = input("Which cipher would you like to use? ")
        print()
        if answer.lower() == "atbash":
            cipher_text = Atbash()
            break
        elif answer.lower() == "keyword":
            keyword = input("what key word would you like to use ")
            if keyword is None or keyword == "":
                cipher_text = KeyWords()
                break
            else:
                cipher_text = KeyWords(keyword)
                break

        elif answer.lower() == "affine":
            cipher_text = Affine()
            break
        elif answer.lower() == "caesar":

            key_value = input("Shift Key Value:")
            if isinstance(int(key_value), int):
                cipher_text = Caesar(int(key_value))
                break
            else:
                cipher_text = Caesar()
                break

        else:
            print("not a valid cipher")

    message = input("{} Cipher,type in your message ".format(answer))
    while True:
        what_to_do = input("Do you want to encrypt ot decrypt? ")
        if what_to_do == "encrypt":
            encrypted_message = cipher_text.encrypt(message)
            break
        elif what_to_do == "decrypt":
            encrypted_message = cipher_text.decrypt(message)
            break
        else:
            print("not valid command")

    print("Your {}ed message is {} ".format(what_to_do, encrypted_message))
    regame = input("Do you want to encrypt/decrypt again y/n ")
    clear()
    if regame.lower() == "y":
        main()
    else:
        print("Good bye hope you had fun {}ing ".format(what_to_do))


if __name__ == "__main__":
    main()
