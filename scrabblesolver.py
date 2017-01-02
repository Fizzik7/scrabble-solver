def scrabble(rackset, word_to_make):
    '''
    Scrabble solver that compares a word to the Scrabble Dictionary with
    score keeping. Then determines if the word can be created from the players
    tile rack.
    Also accepts blank tiles represented by '?'.

    Usage Example: scrabble('piz?a', 'pizza') -> True /w score
                   scrabble('pizda', 'pizza') -> False
    '''

    # Dictionary that represens letter score.
    letter_score = {'a': 1, 'b': 3, 'c': 3, 'd': 4, 'e': 1, 'f': 4, 'g': 2,
                    'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
                    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                    'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '?': 0}

    list_rackset = list(rackset)  # Create character list from string
    list_word_to_make = list(word_to_make)  # Create character list from string
    blank_tiles = []  # Blank tiles known as wildcards represented as '?'
    score = 0  # Starting score.

    # Open and read Scrabble Dictionary.
    file = open('wordlist.txt')
    word_dictionary = file.read()

    if word_to_make in word_dictionary:  # Determines if word to make is valid.

        for tile in list_rackset:  # Create a list with wildcards
            if tile == '?':
                blank_tiles.append('?')

        while '?' in list_rackset:  # Remove wildcards from original list
            list_rackset.remove('?')

        for char in list_word_to_make:  # Remove letter or use wildcard.
            if char in list_rackset:
                list_rackset.remove(char)
                score += letter_score[char]
            else:
                if len(blank_tiles) > 0:
                    blank_tiles.remove('?')
                else:
                    return(False)
        return("You scored: {}".format(score))

    else:
        return('Your word is not in the Scrabble Dictionary')
