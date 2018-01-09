from keywords import KeyWords
from atbash import Atbash
from keywords import KeyWords
from hill import Hill
from affine import Affine


def main():
    print()
    print("This is the Secret Messages project for the Treehouse Techdegree \n")
    cipher_text = None
    print("These are the current available ciphers:\n")
    ciphers = ["Caesar","Atbash","Keyword","Affine"]
    for cipher in ciphers:
        print("- {}".format(cipher))

    answer = input("Which cipher would you like to use? ")
    print()
    if answer == "Atbash":
        cipher_text = Atbash()
    elif answer == "KeyWord":
        keyword = input("what key word would you like to use")

        cipher_text = KeyWords(keyword)

    elif answer == "Affine":
        cipher_text = Affine()

    else:
        print("not a valid cipher")
    message = input("{} is an excellent cipher , type in your message ".format(answer))
    what_to_do = input("Do you want to encrypt ot decrypt? ")
    if what_to_do == "encrypt":
        encrypted_message = cipher_text.encrypt(message)
    elif what_to_do =="decrypt":
        encrypted_message = cipher_text.decrypt(message)

    print("Your {}ed message is {} ".format(what_to_do,encrypted_message))
    regame = input("Do you want to encrypt/decrypt again y/n ")
    if regame.lower() == "y" :
        main()
    else:
        print("Good bye hope you had fun {}ing ".format(what_to_do))


if __name__ == "__main__":
    main()
