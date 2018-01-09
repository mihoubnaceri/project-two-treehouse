from ciphers import Cipher
import numpy as np
import random


class Hill(Cipher):
    def __init__(self,key_martix):
        self.key_martix =  np.array([[26,24,1],
                                    [13,16,10],
                                    [20,17,15]])

    def encrypt(self,text):
        text = text.upper()
        string = []
        temp = list(text)
        numbers_text = []
        matrix_text = []
        if len(text ) == 3:
            for letter in temp:
                numbers_text.append([ord(letter) - ord("A")])
            matrix_text = self.key_martix.dot(np.array(numbers_text))
            matrix_text %= 26
            for key in matrix_text:
                for dooda in key:
                    string.append(chr(dooda+65))
        else:
            print("word has more than three words")
        print("".join(string))




mate = Hill(5)
mate.encrypt("ACT")
