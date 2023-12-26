from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import base64
import binascii

def pad(s):
    block_size = AES.block_size
    return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encrypt_aes_cbc(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext.encode("utf-8"))
    return ciphertext

def decrypt_aes_cbc(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext)).decode("utf-8")
    return decrypted_text

def cbc_main():
    while True:
        print("\n-----SELAMAT DATANG di PROGRAM KAMI!-----")
        print("=====CBC Encryption=====")
        key_size = int(input("Masukkan key size (128, 192, or 256): "))
        key = input("Masukkan secret key ({} characters): ".format(key_size // 8))
        iv_size = 128
        iv = input("Masukkan Inisialisasi vektor ({} characters): ".format(iv_size // 8))
        plaintext = input("Masukkan Plain Text: ")

        key = key[:key_size // 8].encode("utf-8")
        iv = iv[:iv_size // 8].encode("utf-8")

        try:
            ciphertext = encrypt_aes_cbc(key, iv, plaintext)
            print("\n===OUTPUT===")
            print("Encrypted Text (Base64):", base64.b64encode(ciphertext).decode("utf-8"))
            print("Encrypted Text (Hex):", binascii.hexlify(ciphertext).decode("utf-8"))
        except Exception as e:
            print("Error(Masukkan Key Size dengan Benar!):", e)

        repeat = input("Apakah Anda ingin mengulang? (y/n): ")
        if repeat.lower() != 'y':
            print("Program ditutup")
            break

if __name__ == "__main__":
    cbc_main()
