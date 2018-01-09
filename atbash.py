from ciphers import Cipher
import string


class Atbash(Cipher):
    def __init__(self):
        self.output = []

    def encrypt(self,text):
        text = text.upper()
        self.output = []
        for letter in text:
            if letter in string.ascii_uppercase:
                letters  = (26 -  (ord(letter) - ord("A")) ) + ord("A")-1
                self.output.append(chr(letters))
            elif letter in string.ascii_lowercase:
                letters  = (26 -  (ord(letter) - ord("a")) ) + ord("a")-1
                self.output.append(chr(letters))
            else:
                self.output.append(letter)
        return "".join(self.output)

    def decrypt(self,cipher_text):
        self.output = []
        for letter in cipher_text:
            if letter in string.ascii_uppercase:
                letters  = (26 -  (ord(letter) - ord("A")) ) + ord("A")-1
                self.output.append(chr(letters))
            elif letter in string.ascii_lowercase:
                letters  = (26 -  (ord(letter) - ord("a")) ) + ord("a")-1
                self.output.append(chr(letters))
            else:
                self.output.append(letter)
        return "".join(self.output)
