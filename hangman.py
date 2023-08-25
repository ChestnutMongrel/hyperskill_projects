from collections.abc import Iterable
from random import choice


def get_letter() -> str:
    return input('Input a letter: ')


def get_word() -> str:
    dictionary = ('python', 'java', 'swift', 'javascript')
    return choice(dictionary)


def guess_word() -> None:
    word = get_word()
    hint = make_hint(word)
    user_guess = input(f'Guess the word {hint}: ')

    print('You survived!' if word == user_guess else 'You lost!')


def make_hint(word: str, hint: str, symbol: str) -> str:
    if len(word) != len(hint):
        raise ValueError

    hint = list(hint)
    for i in symbol_indexes(word, symbol):
        hint[i] = symbol

    return ''.join(hint)


def symbol_indexes(word: str, symbol: str) -> Iterable:
    # result = list()
    for i, letter in enumerate(word):
        if letter == symbol:
            yield i
    # return result


def test_symbol_indexes() -> None:
    result = [*symbol_indexes('afaafa', 'a')]
    assert result == [0, 2, 3, 5], result
    result = [*symbol_indexes('afafa', 'r')]
    assert result == [], result
    result = [*symbol_indexes('', 's')]
    assert result == [], result
    result = [*symbol_indexes('asdf', '')]
    assert result == [], result


def test_make_hint() -> None:
    result = make_hint('affaaf', '-' * 6, 'a')
    assert result == 'a--aa-', result
    result = make_hint('afafaff', '-' * 7, 'v')
    assert result == '-' * 7, result


def print_title() -> None:
    print('H A N G M A N')


def main() -> None:
    print_title()

    word = get_word()
    hint = '-' * len(word)
    attempts = 8

    while attempts:
        print()
        print(hint)
        
        if hint == word:
            print('You guessed the word!')
            print('You survived!')
            break
            
        letter = get_letter()

        if letter not in word:
            print("That letter doesn't appear in the word.")
        elif letter in hint:  # That letter was already used before.
            print('No improvements.')
        else:  # The letter is new and is in the word.
            attempts += 1  # Adding to overcome subtraction later.
            hint = make_hint(word, hint, letter)

        attempts -= 1

    else:
        print('You lost!')


if __name__ == '__main__':
    main()
    