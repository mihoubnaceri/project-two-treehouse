from keywords import KeyWords
from atbash import Atbash
from keywords import KeyWords
from hill import Hill


def main():
    print()
    print("This is the Secret Messages project for the Treehouse Techdegree \n")
    cipher_text = None
    print("These are the current available ciphers:\n")
    ciphers = ["Caesar","Atbash","Keyword","Hill"]
    for cipher in ciphers:
        print("- {}".format(cipher))

    answer = input("Which cipher would you like to use? ")
    print()
    if answer == "Atbash":
        cipher_text = Atbash()
    elif answer == "KeyWord":
        keyword = input("what key word would you like to use")
        try:
            cipher_text = KeyWords(keyword)
        except TypeError:
            print("your key will be KEYWORD")
        else:
            cipher_text = KeyWords()
    elif answer == "Hill":
        cipher_text = Hill()

    else:
        print("not a valid cipher")
    message = input("{} is an excellent cipher , type in your message ".format(answer))
    what_to_do = input("Do you want to encrypt ot decrypt? ")
    if what_to_do == "encrypt":
        encrypted_message = cipher_text.encrypt(message)
    elif what_to_do =="decrypt":
        encrypted_message = cipher_text.decrypt(message)

    print("Your {}ed message is {} ".format(what_to_do,encrypted_message))










if __name__ == "__main__":
    main()
