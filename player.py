"""
    This contains the Player class.
"""


class Player:
    """
    A Player class to store points, words solved, and name.

    This is for multiple purposes, such as word count recording,
    point tallying, and etc.

    :property: points
    :type: int
    :returns: The number of scrabble points the player has (Combine mode).

    :property: words_solved
    :type: int
    :returns: The number of words the player has solved (Anagram mode).
    """

    points = 0
    words_solved = 0

