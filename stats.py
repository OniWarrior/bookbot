def get_num_words(book_text):

        word_count = len(book_text.split())
        return word_count


# This function receives two arguments: symbol and book_text
# The function will count the number of instances that it
# encounters the given symbol and return the count
def count_symbol(symbol,book_text):
    count = 0
    for character in book_text:
        if symbol == character:
            count +=1
    return count





# simple. find the letter that contains the maximum count then returns a dictionary of that letter 
# and its count
def find_max_letter_count(symbol_dict,arbitrary_letter):

    #initialize empty letter dictionary
    letter_dict = {}
    # get all of the keys
    symbol_keys = symbol_dict.keys()

    # use an arbitrary letter for finding the max count
    greatest_letter = arbitrary_letter

    # iterate using the keys
    for key in symbol_keys:
        if key.isalpha():
            if symbol_dict[key] > symbol_dict[greatest_letter]:
                greatest_letter = key


    # once the letter with the greatest count is found return it
    letter_dict[greatest_letter] = symbol_dict[greatest_letter]
    return letter_dict

# converts the current dictionary, which is both letters and non letters, into a dictionary that only has
# the letters and their counts
def convert_to_alpha_dict(symbol_dict):
    # initialize an empty dictionary
    alpha_dict = {}

    # get the keys for the symbol_dict
    symbol_keys = symbol_dict.keys()

    # iterate through the symbol_dict to start loading new dict with letters
    for key in symbol_keys:
        # check if the key is a letter
        if key.isalpha():

            # true, then load the key and the value into the new dictionary
            alpha_dict[key] = symbol_dict[key]
    # return the new dictionary
    return alpha_dict

# use the dictionary provided as the argument, and return a sorted list of dictionaries of the letters
def sort_dict(alpha_dict):

    #initialize an empty list of dictionarys
    sort_dict_list=[]

    # get the keys from the dictionary provided
    alpha_keys = alpha_dict.keys()
    
    # local dict that will be constantly shrunk as the greatest is continuously removed
    current_dict = {}

    # load the current dict with the key/value pairs of alpha_dict
    for key in alpha_keys:
        current_dict[key] = alpha_dict[key]
    
    # key previously removed
    previous_removed_key_list = []

    # iterate through the keys
    for key in alpha_keys:
        
        if key  in  previous_removed_key_list:
            continue
        
            
        

        # return the current greatest letter as a dictionary
        greatest_letter_dict = find_max_letter_count(current_dict,key)

        # insert into the sort_dict_list sorted list of dictionaries
        sort_dict_list.append(greatest_letter_dict)

        # shrink the current alpha_dict
        greatest_letter_key = greatest_letter_dict.keys()

        greatest_letter = ""

        for letter_key in greatest_letter_key:
            greatest_letter = letter_key

        del current_dict[greatest_letter]
        
        # assign greatest_letter as previous_removed key
        previous_removed_key = str(greatest_letter)
        
        # put it into the list of removed keys
        previous_removed_key_list.append(previous_removed_key)
        
         
            

            
    # return the sorted list
    return sort_dict_list







def get_character_count(book_text):
    

    # initialize an empty dictionary for symbols counted
    symbol_count_dict={}

    # parse the book text
    for character in book_text:


       # check if the character is in the dictionary
       if symbol_count_dict.get(str(character)) != None or symbol_count_dict.get(str(character.lower())) != None:

                      
           # it is true that the symbol is in the dictionary and therefore should not be counted
           continue
       
       # otherwise, check if the character is a letter
       if character.isalpha() != True:  
           
           

           # character is not a letter
           # count the symbol
           symbol_count = count_symbol(character,book_text)

           # assign the count to dictionary
           symbol_count_dict[str(character)] = symbol_count

       else:

           # it is true that the character is a letter, then count the capital letter version 
           # and lower case version of the letter
            
           capital_count = 0
           lower_count = 0

           # check if the letter is uppercase
           if character.isupper() == True:
               capital_count = count_symbol(character,book_text)
               lower_count = count_symbol(character.lower(),book_text)
           else:
               capital_count = count_symbol(character.upper(),book_text)
               lower_count = count_symbol(character,book_text)

           # count both versions and insert into the dictionary
           final_count = capital_count + lower_count
           symbol_count_dict[character.lower()] = final_count
      

            

    return symbol_count_dict
        


