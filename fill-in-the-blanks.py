guess = [['__1__', '__2__', '__3__', '__4__'],
         ['__1__', '__2__', '__3__', '__4__'],
         ['__1__', '__2__', '__3__', '__4__']]


answer = [['high', 'interpreted', 'high', 'dynamic'],
          ['Guido van Rossum', '1991', 'non-profit', 'Python'],
          ['Beautiful', 'Complex', 'counts', 'Errors']]


def puzzle(level):
    if level == 1:
        return ('Python is a widely used {0}-level,general-purpose, '
                'interpreted, dynamic programming language. An '
                '{1} language is a programming language for '
                'which most of it\'s implementations execute instructions '
                'directly, without previously compiling a program into '
                'machine-language instructions. In computer science, a '
                '{2}-level programming language is a programming '
                'language with strong abstraction from the details of '
                'the computer. {3} programming language is a term '
                'used in computer science to describe a class of '
                'high-level programming languages which, at runtime, '
                'execute many common programming behaviors that static '
                'programming languages perform during compilation.'
                ).format(*guess[0])
    if level == 2:
        return ('Python is designed by {0}. Python first appeared in year '
                '{1}. Python is currently developed by Python Software '
                'Foundation (PSF) is a {2} organization devoted to the '
                '{3} programming language.').format(*guess[1])
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
                '-- let\'s do more of those!\n').format(*guess[2])


def choose_level():
    valid_levels = [1, 2, 3]
    message = ('Enter the level\n1. Easy\n2. Medium\n3. Hard\n')
    user_choice = 4  # set to an invalid level
    while user_choice not in valid_levels:
        user_choice = int(raw_input(message))
    return user_choice


def play_game():
    choose_level()


play_game()
