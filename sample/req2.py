def fileToList(filename):
    """This function returns a list given a filename"""
    with open(filename, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data


def concatenateWords(input_list, input_dict):
    """This function returns a string from a given dictionary and an input list"""
    output_str = ''
    for element in input_list:
        output_str += input_dict[element] + ' '
    return output_str.rstrip()


def main():
    container = fileToList(input())
    for x in range(int(input())):
        input_list = list(map(int, input().split()))
        print(concatenateWords(input_list, container))


if __name__ == '__main__':
    main()