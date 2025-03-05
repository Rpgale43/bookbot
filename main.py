from stats import count_words, count_per_char

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        print(f"{num_words} words found in the document")
        char_count = count_per_char(file_contents)
        print(char_count)

main()