def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)

def count_words(words_to_count):
    word_count = 0
    words = words_to_count.split()
    for word in words:
        word_count += 1
    print(word_count)

def count_per_char(book):
    lowercase_book = book.lower()
    char_dict = {}

main()