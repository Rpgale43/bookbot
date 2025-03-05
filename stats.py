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

def sort_on(dict):
    return dict["num"]

def produce_report_items(book):
    report_list = []
    char_count_dict = count_per_char(book)
    for item in char_count_dict:
        if item.isalpha():
            report_list.append({"char": item, "num": char_count_dict[item]})
    report_word_count = count_words(book)
    report_list.sort(reverse=True, key=sort_on)
    return report_list, report_word_count