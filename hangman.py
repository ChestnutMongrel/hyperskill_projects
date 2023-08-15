from random import choice


def get_word() -> str:
    dictionary = ('python', 'java', 'swift', 'javascript')
    return choice(dictionary)


def guess_word() -> None:
    word = get_word()
    hint = make_hint(word)
    user_guess = input(f'Guess the word {hint}: ')

    print('You survived!' if word == user_guess else 'You lost!')


def make_hint(word: str) -> str:
    hint_size = 3
    hint_symbol = '-'
    len_word = len(word)

    if len_word <= hint_size:
        return hint_symbol * len_word

    return word[:hint_size] + hint_symbol * (len_word - hint_size)


def test_make_hint() -> None:
    assert make_hint('python') == 'pyt---'
    assert make_hint('sdf') == '---'
    assert make_hint('') == ''


def print_title() -> None:
    print('H A N G M A N')


def main() -> None:
    print_title()
    guess_word()


if __name__ == '__main__':
    main()
    