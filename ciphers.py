class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    @classmethod
    def key_pad(cls,key):
        key = "12345"
        cls(key)
