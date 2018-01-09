from ciphers import Cipher
import string

class Affine(Cipher):
    def __init__(self):
        self.alphabets = list(string.ascii_uppercase)
        self.alphabet_keys = {key:value for key, value in zip(self.alphabets,range(26)) }
    def encrypt(self,text):
        text = text.upper()
        string =[]
        for letter in text:
            if letter in self.alphabet_keys.keys():
                string.append(chr((self.alphabet_keys[letter] * 5 + 8)%26 + 65))
        return "".join(string)
    
    def decrypt(self,cipher_text):
        cipher_text = cipher_text.upper()
        string = []
        for letter in cipher_text:
            if letter in self.alphabet_keys.keys():
                string.append(chr(((self.alphabet_keys[letter] - 8 )* 21)%26 + 65))
        return "".join(string)
