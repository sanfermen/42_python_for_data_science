import time
import shutil

def bar_progress(iter, total, bar_length):
    """
    This function generates a progress bar in the terminal.

    Parameters:
    iter (int): The current iteration number.
    total (int): The total number of iterations.
    bar_length (int): The length of the progress bar.

    Prints:
    str: A string representation of the progress bar, including the percentage of completion,
         the visual bar, and the current iteration over the total number of iterations.

    Note:
    The progress bar's length is determined by the terminal's width minus 40 characters.
    """
    # Takes the current iteration number, divides it by the total number of iterations `total`,
    # multiplies by 100 to get a percentage value, and then formats it to have one decimal
    percent = ("{0:.0f}").format(100 * (iter / (total)))
    # Calculate the number of filled characters that should be displayed in a progress bar 
    # based on the current iteration number, the total number of iterations, and the length
    # of the progress bar `bar_length`.
    filled = int(bar_length * iter // total)
    # Create a progress bar visualization by combining three different strings
    bar = "=" * filled + ">" + " " * (bar_length - filled)
    print(f"{percent}%|{bar}| {iter}/{total}\r", end= '', flush= True)


def ft_tqdm(lst: range) -> None:
    """
    This function generates a progress bar in the terminal for an iterable object.

    Parameters:
    lst (range): The iterable object for which the progress bar is generated.

    Yields:
    int: The next number in the range.

    Note:
    The progress bar's length is determined by the terminal's width minus 40 characters.
    """
    total = len(lst)
    bar_length = shutil.get_terminal_size().columns - 40

    for i, n in enumerate(lst):
        bar_progress(i+1, total, bar_length)
        yield n
