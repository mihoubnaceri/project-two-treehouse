from ciphers import Cipher
import string


class KeyWords(Cipher):

    def __init__(self, keyword="keyword"):
        """
        initialisez the KeyWords class
        makes the alphabets list and also list containing
        the unrepeated letters with the keyword start
        and finishes with rest of alphabets
        """
        self.keyword = []
        self.alphabets = list(string.ascii_uppercase)
        for num in keyword.upper():
            if num not in self.keyword:
                self.keyword.append(num)

    def encrypt(self, text):
        """
        encrypts text depending on the keyword example
        alphabets:
        A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
        K,E,Y,W,O,R,D,A,B,C,F,G,H,I,J,L,M,N,P,Q,S,T,U,V,X,Z
        A turnz to K
        the keyword alphabets cant be repeated
        """
        alphabets = []
        text = text.upper()
        string_text = ""
        alphabets[:len(self.keyword)] = self.keyword

        alphabets.extend([letter for letter in self.alphabets if letter not in alphabets])
        # making a dict to store alphbates to key value
        new_dict = {key: value for key, value in zip(self.alphabets, alphabets)}

        for letter in text:
            if letter in new_dict.keys():
                string_text += new_dict[letter]
            else:
                string_text += letter

        return string_text

    def decrypt(self, cipher):
        """
        decrypts changing from letter to corresponding letter
        A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
        K,E,Y,W,O,R,D,A,B,C,F,G,H,I,J,L,M,N,P,Q,S,T,U,V,X,Z
        making dict object containg every alphabet to coresponding letter

        """
        alphabets = []
        cipher = cipher.upper()
        string_text = ""
        alphabets[:len(self.keyword)] = self.keyword
        alphabets.extend([letter for letter in self.alphabets if letter not in alphabets])
        # making a dict to store alphbates to key value
        new_dict = {key: value for key, value in zip(alphabets, self.alphabets)}

        for letter in cipher:
            if letter in new_dict.keys():
                string_text += new_dict[letter]
            else:
                string_text += letter

        return string_text
