import sys
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_counter(text)
    counted_letters = character_counter(text)
    new_counted = character_list(counted_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for counted in new_counted:
        if counted["char"].isalpha():
            print(f"{counted["char"]}: {counted["num"]}")
    print("============= END ===============")
def get_book_text(path):
    with open(path) as f:
        return f.read()
from stats import word_counter
from stats import character_counter
from stats import character_list
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()