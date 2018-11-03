"""
    This contains the Player class.

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""


class Player:
    """
    A Player class to store points, words solved, and name.

    This is for multiple purposes, such as highscore recording,
    point tallying, and etc.
    """

    points, words_solved, name = 0, 0, ""
    gamerecord = "" # put a tuple here later: (gamemode, word/string)
