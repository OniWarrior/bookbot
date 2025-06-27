from stats import get_num_words
from stats import get_character_count
from stats import convert_to_alpha_dict
import sys
from stats import sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents





def main():
    argument_list = sys.argv
    if len(argument_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = argument_list[1] 

    book_content = get_book_text(file_path)
    book_word_count = get_num_words(book_content)
    book_msg = f"Found {book_word_count} total words"
    character_count = get_character_count(book_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")

    print(book_msg)

    print("--------- Character Count -------")

    # first convert the dictionary, character_count, into an alphabet dictionary
    alpha_dict = convert_to_alpha_dict(character_count)
    
    # iterate through the alphabet dictionary and 
    # return the dictionaries of the letters and their count from greatest to smallest
    final_list = sort_dict(alpha_dict)

    # print the final list of sorted dictionaries 
    for dict in final_list:
        dict_keys = dict.keys()
        for key in dict_keys:
            print(f"{key}: {dict[key]}")

    sys.exit(0)    

if __name__ == "__main__" :
    main()
