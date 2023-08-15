def guess_word() -> None:
    word = 'python'
    user_guess = input('Guess the word: ')

    print('You survived!' if word == user_guess else 'You lost!')


def print_title() -> None:
    print('H A N G M A N')


def main() -> None:
    print_title()
    guess_word()


if __name__ == '__main__':
    main()
    