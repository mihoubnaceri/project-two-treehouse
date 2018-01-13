from ciphers import Cipher
import string


class Atbash(Cipher):
    def __init__(self):
        self.output = []

    def encrypt(self, text):
        """

        encypts a text and every letter is
        encrypted to its revers for example A becomes Z
        Z becomes A


        """
        text = text.upper()
        self.output = []
        for letter in text:
            if letter in string.ascii_uppercase:
                letters = (26 - (ord(letter) - ord("A"))) + ord("A")-1
                self.output.append(chr(letters))
            elif letter in string.ascii_lowercase:
                letters = (26 - (ord(letter) - ord("a"))) + ord("a")-1
                self.output.append(chr(letters))
            else:
                self.output.append(letter)
        return "".join(self.output)

    def decrypt(self, cipher_text):
        """
        changes back the encrypted version into plain tex
        if the letter is Z it should go back to A
        takes letter and convers it to the reverse letter

        """
        return self.encrypt(cipher_text)
