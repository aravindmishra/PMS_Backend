import hashlib

class Common:
    def encryptPassword(password):
        try:
            return hashlib.pbkdf2_hmac('sha256', bytes(password,encoding='utf8'), b'salt', 100000).hex()            
        except Exception as e:
            print(str(e))
            return False