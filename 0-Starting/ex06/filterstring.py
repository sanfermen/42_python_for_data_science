import sys
import ft_filter


def main():
    if len(sys.argv) == 3 and isinstance(sys.argv[1], str):
        try:
            nbr = int(sys.argv[2])
        except ValueError:
            print("AssertionError: Second argument must be a number")
            return

        split_str = ft_filter.ft_filter(lambda x: len(x) > nbr, sys.argv[1].split())
        return print(split_str)

    else:
        print("AssertionError: Provide a string and a number as arguments.")


if __name__ == "__main__":
    main()
