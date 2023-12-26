def get_input(message):
    return input(message).replace(" ", "").upper()

def matrix(x, y, initial):
    return [[initial for _ in range(x)] for _ in range(y)]

def create_playfair_matrix(secret_key):
    result = []
    for c in secret_key:
        if c not in result:
            result.append('I' if c == 'J' else c)

    flag = 0
    for i in range(65, 91):
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))

    k = 0
    playfair_matrix = matrix(5, 5, 0)
    for i in range(5):
        for j in range(5):
            playfair_matrix[i][j] = result[k]
            k += 1

    return playfair_matrix

def locate_index(matrix, c):
    if c == 'J':
        c = 'I'
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if c == value:
                return i, j

def encrypt_message(playfair_matrix, message):
    encrypted_text = ""
    i = 0
    while i < len(message):
        loc = locate_index(playfair_matrix, message[i])
        loc1 = locate_index(playfair_matrix, message[i + 1])
        if loc[1] == loc1[1]:
            encrypted_text += "{}{}".format(playfair_matrix[(loc[0] + 1) % 5][loc[1]],
                                            playfair_matrix[(loc1[0] + 1) % 5][loc1[1]])
        elif loc[0] == loc1[0]:
            encrypted_text += "{}{}".format(playfair_matrix[loc[0]][(loc[1] + 1) % 5],
                                            playfair_matrix[loc1[0]][(loc1[1] + 1) % 5])
        else:
            encrypted_text += "{}{}".format(playfair_matrix[loc[0]][loc1[1]], playfair_matrix[loc1[0]][loc[1]])
        i += 2

    return encrypted_text

def playfair_cipher():
    print("-----SELAMAT DATANG di PROGRAM KAMI!-----")
    print("=====PLAYFAIR CIPHER=====")
    secret_key = get_input("Silakan Masukkan Encryption key: ")
    playfair_matrix = create_playfair_matrix(secret_key)

    while True:
        print("===MENU PLAYFAIR CIPHER===")
        print("1.Enkripsi \n2.Keluar")
        choice = int(input("Pilih program yang Anda inginkan: "))

        if choice == 1:
            message = get_input("Masukkan Pesan Anda: ")
            encrypted_text = encrypt_message(playfair_matrix, message)
            print("Plain Text:", message)
            print("Cipher Text (Result):", encrypted_text)
            print("\n")
        elif choice == 2:
            exit("Program ditutup")
        else:
            print("Pilihan Anda Salah, Silakan Pilih dengan Benar!")

if __name__ == "__main__":
    playfair_cipher()
