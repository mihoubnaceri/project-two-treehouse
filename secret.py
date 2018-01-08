from keywords import KeyWords
from atbash import Atbash




mate = Atbash()
nasro = KeyWords()
print(mate.encrypt("wizard"))
print(mate.decrypt("draziw"))
print(nasro.encrypt("chafik naceri"))
print(nasro.decrypt("YAKRBF IKYONB"))
