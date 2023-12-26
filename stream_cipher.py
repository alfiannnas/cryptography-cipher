MOD = 256

def KSA(key):
    key_length = len(key)
    S = list(range(MOD))
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i] 
    return S

def PRGA(S):
    i, j = 0, 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD
        S[i], S[j] = S[j], S[i] 
        yield S[(S[i] + S[j]) % MOD]

def get_keystream(key):
    S = KSA([ord(c) for c in key])
    return PRGA(S)

def encrypt_logic(key, text):
    keystream = get_keystream(key)
    return ''.join(["%02X" % (c ^ next(keystream)) for c in text])

def stream_cipher():
    print("-----SELAMAT DATANG di PROGRAM KAMI!-----")
    print("=====STREAM CIPHER=====")
    key = input("Silakan Masukkan Encyption Key: ")
    
    while True:
        print("===MENU STREAM CIPHER===")
        print("1.Enkripsi \n2.Keluar")
        choice = int(input("Pilih program yang Anda inginkan: "))
        
        if choice == 1: 
            plaintext = input("Masukkan Pesan Anda: ")
            ciphertext = encrypt_logic(key, [ord(c) for c in plaintext])
            print('Plain Text:', plaintext)
            print('Cipher Text (Result):', ciphertext)
            print("\n")
        elif choice == 2:
            exit("Program ditutup")
        else:
            print("Pilihan Anda Salah, Silakan Pilih dengan Benar!")

if __name__ == '__main__':
    stream_cipher()
