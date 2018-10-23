# developed by Carlos Panganiban, 2018

def initDictionary(filename):
    """This function returns a dictionary (list) given a filename."""
    with open(filename, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data