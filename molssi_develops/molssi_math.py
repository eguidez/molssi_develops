"""
molssi_math.py
A package containing math functions

Handles the primary functions
"""


def mean(my_list):
    """
    This function calculates the mean of a list
  
    Parameters
    ----------
    my_list: list
        The list of numbers that we want to average

    Returns
    -------
    mean_list : float
        The mean of the list

    Examples
    -------
    >>> mean ([1,2,3,4,5])
    3.0
    """
    if not isinstance(my_list, list):
        raise TypeError("Mean: {} is not a list".format(my_list))

    return sum(my_list) / len(my_list)


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
