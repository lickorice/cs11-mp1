def fileToList(filename):
    """This function returns a list given a filename"""
    with open(filename, 'r') as f:
        data = [line.rstrip() for line in f.readlines()]
    return data


def generateSequence(word_list):
    """This function returns an absolute minimum dictionary of letters required
    to form a given list of words."""
    alphabet = {chr(i): 0 for i in range(97, 122)}
    for word in word_list:
        character_dict = {}
        for character in word:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1

        # resolving output alphabet:
        for character in character_dict:
            alphabet[character] = max(character_dict[character], alphabet[character])
    return alphabet


def generateString(sequence):
    """Given a sequence (alphabet dictionary), generate a string of *ordered* letters."""
    output_str = ''
    for character in sequence:
        output_str += character*sequence[character]
    return output_str


def main():
    container = fileToList(input())
    for x in range(int(input())):
        word_list = input().split()
        alphabet_sequence = generateSequence(word_list)
        print(generateString(alphabet_sequence))


if __name__ == '__main__':
    main()