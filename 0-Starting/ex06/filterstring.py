import sys
import ft_filter


def main():
    """
    Filter a string by a given number.

    Takes a string and an integer as command line arguments.
    Prints out a list of words in the string that are longer than the given
    number.

    If the arguments are not correct, prints out an AssertionError with a
    message.
    """
    if len(sys.argv) == 3 and isinstance(sys.argv[1], str):
        try:
            nbr = int(sys.argv[2])
        except ValueError:
            print("AssertionError: Second argument must be a number")
            return

        split_str = ft_filter.ft_filter(lambda x: len(x) > nbr,
                                        sys.argv[1].split())
        return print(split_str)

    else:
        print("AssertionError: Provide a string and a number as arguments.")


if __name__ == "__main__":
    main()
