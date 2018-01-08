from ciphers import Cipher
import numpy as np
import random


class Hill(Cipher):
    def __init__(self,key_martix):
        self.random_number = random.randint(2,5)
        self.key_martix =  np.random.random_integers(0,25,(self.random_number,self.random_number))
        #string = []
        print(self.key_martix)
        #print(self.key_matrix)
        #for key in self.key_matrix:
            #print(key)

            #for dooda in key:
                #string.append(chr(dooda + 65))



        #print("".join(string))
    def encrypt(self,text):
        text = text.upper()
        temp = list(text)
        numbers_text = []
        matrix_text = []
        for letter in temp:
            numbers_text.append([ord(letter) - ord("A")])
        matrix_text = np.matrix(numbers_text)
        print(matrix_text)
        mate = matrix_text * self.key_martix

        print(mate % 26)




mate = Hill(5)
mate.encrypt("ACT")
