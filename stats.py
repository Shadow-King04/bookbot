def get_word_count(book_text):
    #Counts the number of words in the string provided, seperated by whitespace [.split() method]
    return len(book_text.split())

def get_character_count(book_text):
    #Creates an empty dictionary
    chars = {}
    #Loops through characters in provided text, for each it sets the character to lowercase
    #For each character, checks the dictionary for a character, if it doesn't exist sets it to 0, then incremennts for each one found
    for x in book_text:
        lower_char = x.lower()
        chars[lower_char] = chars.get(lower_char, 0) + 1
    return chars

def sort_on(char_dict):
    return char_dict["num"]

def sorted_char_list(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            new_dict = {"char":char, "num": char_dict[char]}
            char_list.append(new_dict)
    
    char_list.sort(key=sort_on, reverse=True)
    return char_list

