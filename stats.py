def count_words(words_to_count):
    word_count = 0
    words = words_to_count.split()
    for word in words:
        word_count += 1
    return word_count

def count_per_char(book):
    lowercase_book = book.lower()
    char_dict = {}
    for c in lowercase_book:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict