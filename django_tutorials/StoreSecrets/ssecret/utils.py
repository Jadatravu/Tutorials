from Crypto.Cipher import AES
import base64
KEY="abcdefghijklmnop"
def encryption_function(normal_value):
    nor_value = str(normal_value)
    encryption_secret = AES.new(KEY)
    tag_string = (nor_value + (AES.block_size - len(nor_value) % AES.block_size) * "\0")
    encryption_value = base64.b64encode(encryption_secret.encrypt(tag_string))
    return encryption_value

def decryption_function(enc_value):
    decryption_secret = AES.new(KEY)
    decrypted_value = decryption_secret.decrypt(base64.b64decode(enc_value))
    normal_value = decrypted_value.rstrip("\0")
    return normal_value

def main():
    pass1 = "qwerty@123" 
    enc_pass = encryption_function(pass1)
    print enc_pass
    dec_pass = decryption_function(enc_pass)
    print dec_pass

#main()

