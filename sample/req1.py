def fileToList(filename):
    """This function returns a list given a filename"""
    with open(filename, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data


def main():
    container = fileToList(input())
    for entry in container:
        print(entry)


if __name__ == '__main__':
    main()