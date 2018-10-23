import engine

# Configure some values:
point_index = {
    1 : ['e', 'a', 'i', 'o', 'u', 'n', 'r', 't', 'l', 's', 'u'],
    2 : ['d', 'g'],
    3 : ['b', 'c', 'm', 'p'],
    4 : ['f', 'h', 'v', 'w', 'y'],
    5 : ['k'],
    8 : ['j', 'x'],
    10 : ['q', 'z']
}
str_init = "Enter dictionary name: "


def main():
    """The main method run when running the game."""

    # Initiate the main dictionary
    dictionary = engine.initDictionary(input(str_init))


if __name__ == '__main__':
    main()