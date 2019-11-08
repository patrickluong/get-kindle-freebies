import sys
import random
import pyperclip

def _random_upper(char):
    if (random.random() < 0.5):
        return char.upper()
    return char.lower()

def main():
    if len(sys.argv) > 1:
        should_copy = False
        text = ' '.join(sys.argv[1:])
    else:
        should_copy = True
        text = pyperclip.paste()

    result_text = ''.join(map(_random_upper, text))

    if should_copy:
        pyperclip.copy(result_text)
    else:
        print(result_text)


if __name__ == '__main__':
    main()