def fileToList(filename):
    """This function returns a list given a filename"""
    with open(filename, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data


def checkAnswer(sequence_str, input_str, input_dict):
    """This function returns a Boolean given a sequence string (sequence_str),
    an answer string (input_str), and an input dictionary (input_dict)."""
    if input_str not in input_dict:
        return False

    sequence_list = [i for i in sequence_str]

    for character in input_str:
        if character in sequence_list:
            sequence_list.remove(character)
        else:
            return False
    return True


def main():
    container = fileToList(input())
    for x in range(int(input())):
        input_list = input().split()
        print(checkAnswer(input_list[0], input_list[1], container))


if __name__ == '__main__':
    main()