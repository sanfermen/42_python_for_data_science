import shutil


def bar_progress(iter, total, bar_length):
    """
    This function generates a progress bar in the terminal.

    Parameters:
    iter (int): The current iteration number.
    total (int): The total number of iterations.
    bar_length (int): The length of the progress bar.

    Prints:
    str: A string representation of the progress bar, including the percentage
    of completion, the visual bar, and the current iteration over the total
    number of iterations.

    Note:
    Progress bar's length is determined by the terminal's width minus 40 char.
    """

    # Perc = nmb of current iter / total nmb of iters * 100.
    # Format to string without decimals
    percent = ("{0:.0f}").format(100 * (iter / (total)))
    # Filled = nmb of current iter / total nmb of iters * bar length
    filled = int(bar_length * iter // total)
    # Creating the progress bar
    bar = "=" * filled + ">" + " " * (bar_length - filled)
    # Printing the progress bar to the console
    # flush=True: forces the output to be written to the console immediately
    print(f"{percent}%|{bar}| {iter}/{total}\r", end='', flush=True)


def ft_tqdm(lst: range) -> None:
    """
    This fnc generates a progress bar in the terminal for an iterable object.

    Parameters:
    lst (range): The iterable object for which the progress bar is generated.

    Yields:
    int: The next number in the range.
    """
    # Get the total number of iterations
    total = len(lst)
    # Get the width of the terminal window and subtract 40 chars
    bar_length = shutil.get_terminal_size().columns - 40

    for i, n in enumerate(lst):
        bar_progress(i+1, total, bar_length)
        yield n
