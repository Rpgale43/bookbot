from stats import count_words, count_per_char, produce_report_items

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report_list, report_word_count = produce_report_items(file_contents)
        print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {report_word_count} total words
--------- Character Count -------""")
        for char in report_list:
            print(f"{char["char"]}: {char["num"]}")
        print("============= END ===============")

main()