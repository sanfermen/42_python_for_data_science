import sys


morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '\\ '
}


def main():
    if len(sys.argv) != 2:
        print("AssertionError: Provide a string as argument.")
        return
    else:
        for char in sys.argv[1]:
            if char.upper() not in morse_code and char != " ":
                print("AssertionError: Invalid character")
                return
        morse_resul = " ".join(morse_code[char.upper()]
                               for char in sys.argv[1])
        print(morse_resul)
        return


if __name__ == "__main__":
    main()
