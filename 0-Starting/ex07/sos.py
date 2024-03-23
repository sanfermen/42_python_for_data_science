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
        morse_char = morse_code_dict.get(letter.upper())
        if morse_char is None:
            print(f"Error: Character '{letter}' is not valid.")
            return
            # raise ValueError(f"Error: Character '{letter}' is not valid.")
        morse_chars.append(morse_char)

    print(" ".join(morse_chars))

def main():
    """
    Main function to execute the program.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py 'text_to_encode'")
    elif not sys.argv[1]:
        print("Error: Empty input text")
    # elif not is_valid_text(sys.argv[1]):
    #     print("Error: Input text contains invalid characters")
    else:
        encode_morse(sys.argv[1])

if __name__ == "__main__":
    main()
