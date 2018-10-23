def fileToList(filename):
    """This function returns a list given a filename"""
    with open(filename, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data


def anagramMatch(target_word, input_dict):
    """This function returns a list of words given an anagram and a dictionary."""
    target_arrangement, output_list = sorted(target_word), []
    for word in input_dict:
        if sorted(word) == target_arrangement:
            output_list.append(word)
    return output_list


def main():
    container = fileToList(input())
    for x in range(int(input())):
        matches = anagramMatch(input(), container)
        outputstr = ''
        for match in matches:
            outputstr += match + ' '
        print(outputstr.rstrip())


if __name__ == '__main__':
    main()