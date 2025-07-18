import sys


def count_char(text):
    """
    Count the numbers of characters, upper and lower case letters,
    punctuation marks, spaces and digits in the given text.

    Parameters:
    - text : The input text to analyze

    Prints the analysis resuts
    """
    chars = len(text)
    punct_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    upper_case = sum(1 for i in text if i.isupper())
    lower_case = sum(1 for i in text if i.islower())
    punct = sum(1 for i in text if i in punct_marks)
    sp = sum(1 for i in text if i.isspace())
    dig = sum(1 for i in text if i.isdigit())

    print(f"The text contains {chars} characters:")
    print(f"{upper_case} upper letters")
    print(f"{lower_case} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{sp} spaces")
    print(f"{dig} digits")


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Only one argument is allowed")

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")

        count_char(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
