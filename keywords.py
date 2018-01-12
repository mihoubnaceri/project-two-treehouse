from ciphers import Cipher
import string


class KeyWords(Cipher):
    def __init__(self,keyword = "keyword"):
        self.keyword = []
        self.alphabets  = list(string.ascii_uppercase)
        for num in keyword.upper():
            if num not in self.keyword:
                self.keyword.append(num)




    def encrypt(self,text):
        #print(self.keyword)
        alphabets = []
        text = text.upper()
        string_text= ""
        alphabets[:len(self.keyword)] = self.keyword

        alphabets.extend([letter for letter in self.alphabets if not letter in alphabets])

        new_dict = {key: value for key, value in zip(self.alphabets,alphabets)}
        #print(new_dict)
        for letter in text:
            if letter in new_dict.keys():
                string_text+= new_dict[letter]
            else:
                string_text += letter

        return string_text

    def decrypt(self,cipher):
        alphabets = []
        cipher = cipher.upper()
        string_text=""
        alphabets[:len(self.keyword)] = self.keyword
        alphabets.extend([letter for letter in self.alphabets if not letter in alphabets])
        new_dict = {key: value for key, value in zip(alphabets,self.alphabets)}

        for letter in cipher:
            if letter in new_dict.keys():
                string_text+= new_dict[letter]
            else:
                string_text += letter

        return string_text
#mate = KeyWords()
#mate.encrypt("chafik")
