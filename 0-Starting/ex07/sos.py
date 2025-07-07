import sys


def encode_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }

    morse_chars = []

    for letter in text:
        upper_letter = letter.upper()
        if upper_letter not in morse_code_dict:
            raise AssertionError(f"Error: {letter} is not a valid character")
        morse_chars.append(morse_code_dict[upper_letter])

    print(" ".join(morse_chars))


def main():
    """
    Main function to execute the program.
    """
    if len(sys.argv) != 2:
        raise AssertionError("Usage: python script.py 'text_to_encode'")
    if not sys.argv[1]:
        raise AssertionError("Error: Empty input text")

    encode_morse(sys.argv[1])


if __name__ == "__main__":
    main()
