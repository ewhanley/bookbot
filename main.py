def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_word_count(text)

    num_letters = get_letter_count(text)

    sorted_letters = sort_letters_dict(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words in this document\n")
    for k, v in sorted_letters:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")


def get_word_count(text):
    words = text.split()
    return len(words)


def get_letter_count(text):
    letter_counts = {}
    for letter in text:
        letter = letter.lower()
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    return letter_counts


def sort_letters_dict(letters_dict):
    return sorted(letters_dict.items(), key=lambda x: x[1], reverse=True)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
