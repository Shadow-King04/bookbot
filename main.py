import sys
from stats import get_word_count
from stats import get_character_count
from stats import sorted_char_list

def get_book_text(file_path):
    #Opens the file
    with open(file_path) as f:
        #Reads the file as the output of the function
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_word_count(text)
    num_characters = get_character_count(text)
    sorted_list = sorted_char_list(num_characters)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

main()