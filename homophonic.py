import random

class Homophony:
    @staticmethod
    def encode(plaintext):
        return ''.join(str(random.choice(Homophony.char_table[char])) for char in plaintext.upper())

    @staticmethod
    def decode(encrypted_text):
        return ''.join(char for each_number in encrypted_text.split() for char, numbers in Homophony.char_table.items() if each_number in numbers)


    char_table = {
        'A': ["01", "02", "03", "04"],
        ' ': ["05", "06", "07", "08"],
        'B': ["09", "10", "11", "12"],
        'C': ["13", "14", "15", "16"],
        'D': ["17", "18", "19", "20"],
        'E': ["21", "22", "23", "24"],
        'F': ["25", "26", "27", "28"],
        'G': ["29", "30", "31", "32"],
        'H': ["33", "34", "35", "36"],
        'I': ["37", "38", "39"],
        'J': ["40", "41", "42", "43"],
        'K': ["44", "45", "46", "47"],
        'L': ["48", "49", "50", "51"],
        'M': ["52", "53", "54", "55"],
        'N': ["56", "57", "58", "59"],
        'O': ["60", "61", "62", "63"],
        'P': ["64", "65", "66", "67"],
        'Q': ["68", "69", "70", "71"],
        'R': ["72", "73", "74", "75"],
        'S': ["76", "77", "78", "79"],
        'T': ["80", "81", "82", "83"],
        'U': ["84", "85", "86", "87"],
        'V': ["88", "89", "90", "91"],
        'W': ["92", "93", "94", "95"],
        'X': ["96", "97", "98"],
        'Y': ["99", "100", "101"],
        'Z': ["102", "103", "104"],
        '0': ["105", "106", "107"],
        '1': ["108", "109", "110"],
        '2': ["111", "112", "113"],
        '3': ["114", "115", "116"],
        '4': ["117", "118", "119"],
        '5': ["120", "121", "122"],
        '6': ["123", "124", "125"],
        '7': ["126", "127", "128"],
        '8': ["129", "130", "131"],
        '9': ["132", "133", "134"],
    }


if __name__ == '__main__':
    while True:
        print("\n-----SELAMAT DATANG di PROGRAM KAMI!-----")
        print("=====SUBSTITUSI HOMOFONIK=====")
        plain_text = input('Masukkan Plain Text: ')
        encoded = Homophony.encode(plain_text)

        print("\n===OUTPUT===")
        print("Encryption text:\n",(encoded))
        repeat = input("Apakah Anda ingin mengulang? (y/n): ")
        if repeat.lower() != 'y':
            print("Program ditutup")
            break
