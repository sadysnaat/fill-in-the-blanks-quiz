guesses = [['__{0}__'.format(i) for i in range(1, 5)] for j in range(3)]
# to generate array of 4 guesses for 3 level of puzzles
# [['__1__', '__2__', '__3__', '__4__'],
# ['__1__', '__2__', '__3__', '__4__'],
# ['__1__', '__2__', '__3__', '__4__']]


answers = [['high', 'interpreted', 'high', 'dynamic'],
           ['Guido van Rossum', '1991', 'non-profit', 'Python'],
           ['Beautiful', 'Complex', 'counts', 'Errors']]


def puzzle(level):
    if level == 1:
        return ('Python is a widely used {0}-level,general-purpose, '
                'interpreted, dynamic\nprogramming language. An '
                '{1} language is a programming language for '
                'which most\nof it\'s implementations execute instructions '
                'directly, without previously\ncompiling a program into '
                'machine-language instructions.\nIn computer science, a '
                '{2}-level programming language is a programming\n'
                'language with strong abstraction from the details of '
                'the computer.\n{3} programming language is a term '
                'used in computer science to describe\na class of '
                'high-level programming languages which, at runtime, '
                'execute\nmany common programming behaviors that static '
                'programming languages perform\nduring compilation.'
                ).format(*guesses[0])
    if level == 2:
        return ('Python is designed by {0}. Python first appeared in year '
                '{1}.\nPython is currently developed by Python Software '
                'Foundation (PSF).\nPSF is a {2} organization devoted to the '
                '{3} programming language.').format(*guesses[1])
    if level == 3:
        return ('{0} is better than ugly.\n'
                'Explicit is better than implicit.\n'
                'Simple is better than complex.\n'
                '{1} is better than complicated.\n'
                'Flat is better than nested.\n'
                'Sparse is better than dense.\n'
                'Readability {2}.\n'
                'Special cases aren\'t special enough to break the '
                'rules.\n'
                'Although practicality beats purity.\n'
                '{3} should never pass silently.\n'
                'Unless explicitly silenced.\n'
                'In the face of ambiguity, refuse the temptation to '
                'guess.\n'
                'There should be one-- and preferably only one '
                '--obvious way to do it.\n'
                'Although that way may not be obvious at first unless '
                'you\'re Dutch.\n'
                'Now is better than never.\n'
                'Although never is often better than *right* now.\n'
                'If the implementation is hard to explain, '
                'it\'s a bad idea.\n'
                'If the implementation is easy to explain, '
                'it may be a good idea.\n'
                'Namespaces are one honking great idea '
                '-- let\'s do more of those!').format(*guesses[2])


def reset_guess(level):
    # to reset the guesses for a given level
    # otherwise if a player plays the same level again
    # he will have all the answers already
    guesses[level-1] = ['__{0}__'.format(i) for i in range(1, 5)]


def print_seperator(character='=', count=80):
    print character * count


def print_puzzle(level):
    print_seperator()
    print "Puzzle: Level {0}".format(level).center(80)
    print_seperator()
    print puzzle(level)
    print_seperator()


def print_game_complete():
    print_seperator()
    print "Congratulations you have completed the puzzle."
    print_seperator()


def choose_level():
    valid_levels = [1, 2, 3]
    message = ('Enter the level\n1 for Easy\n2 for Medium\n3 for Hard\n')
    user_choice = int(raw_input(message))
    while user_choice not in valid_levels:
        print "Please select a valid level."
        user_choice = int(raw_input(message))
    return user_choice


def start_guessing(level, guess_number):
    message = "What should go in blank number {0} ".format(guess_number + 1)
    user_guess = raw_input(message).strip()
    while user_guess.lower() != answers[level-1][guess_number].lower():
        print "Wrong guess try again."
        user_guess = raw_input(message).strip()
    guesses[level-1][guess_number] = answers[level-1][guess_number]
    print "Right answer :)"
    print_seperator()


def print_game_greeting():
    print_seperator()
    print "Welcome to Python Fill in the blank Puzzle".center(80)
    print_seperator()


def play_game():
    print_game_greeting()
    play_more = 'y'
    while play_more.lower() == 'y' or play_more.lower() == '':
        level = choose_level()
        for i in range(len(guesses[level-1])):
            print_puzzle(level)
            start_guessing(level, i)
        print_puzzle(level)
        print_game_complete()
        reset_guess(level)
        play_more = raw_input('Want to play more.(y/n) ').strip()

play_game()
