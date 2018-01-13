from ciphers import Cipher
import string


class Affine(Cipher):

    def __init__(self):
        self.alphabets = list(string.ascii_uppercase)
        # makes adict taking every letter and giving it its corresponding value example A:0
        self.alphabet_keys = {key: value for key, value in zip(self.alphabets, range(26))}

    def encrypt(self, text):
        """
        Encrypts plain text using
        the formula (5x + 8) % 26
        x being the value of alphabet example A:0
        would result to 8 than add 65 to get its encrypted letter
        """
        text = text.upper()
        string = []
        for letter in text:
            if letter in self.alphabet_keys.keys():
                string.append(chr((self.alphabet_keys[letter] * 5 + 8) % 26 + 65))
            else:
                string.append(letter)

        return "".join(string)

    def decrypt(self, cipher_text):
        """
        decrypts plain text using
        the formula ((y-8) *21) % 26
        y being the value of alphabet

        """
        cipher_text = cipher_text.upper()
        string = []
        for letter in cipher_text:
            if letter in self.alphabet_keys.keys():
                string.append(chr(((self.alphabet_keys[letter] - 8) * 21) % 26 + 65))
            else:
                string.append(letter)

        return "".join(string)
