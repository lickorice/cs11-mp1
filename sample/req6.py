# Point configuration
point_index = {
    1 : ['e', 'a', 'i', 'o', 'u', 'n', 'r', 't', 'l', 's', 'u'],
    2 : ['d', 'g'],
    3 : ['b', 'c', 'm', 'p'],
    4 : ['f', 'h', 'v', 'w', 'y'],
    5 : ['k'],
    8 : ['j', 'x'],
    10 : ['q', 'z']
}



def fileToList(filename):
    """This function returns a list given a filename"""
    with open(filename, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data


def maxPoints(input_str, input_dict):
    """This returns the maximum points (integer) that you can achieve
    given a scrambled string (input_str) and a dictionary (input_dict)"""
    output_pts, output_words = 0, []

    for _word in input_dict:
        check_list, in_dict = [i for i in input_str], True
        for _char in _word:
            if _char not in check_list:
                in_dict = False
                break
            else:
                check_list.remove(_char)
        if in_dict:
            output_words.append(_word)

    for word in output_words:
        for character in word:
            for entry in point_index:
                if character in point_index[entry]:
                    output_pts += entry
                    break
    return output_pts


def main():
    container = fileToList(input())
    for x in range(int(input())):
        print(maxPoints(input(), container))


if __name__ == '__main__':
    main()