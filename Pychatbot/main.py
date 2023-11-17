# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:33:02 2023

@author: Aube
"""

from functions import *
    
# Call of the function list_of_files
directory = "./speeches"
files_names = list_of_files(directory, "txt")

if __name__ == '__main__':
    # Call of the function name_of_presidents
    presidents_name = name_of_presidents(files_names)

    # Create a list of full names with the concatenation of first name and name
    presidents_first_name = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    presidents_full_name = [presidents_first_name [i] + " " + presidents_name[i] for i in range(len(presidents_first_name ))]

    # Call the function display_full_name to display president name
    display_full_name(presidents_full_name)
    print()

    # Create a dictionary with full name as key and file_name linked to the name as value
    # Call the function fill_dico
    dico_presidents = fill_dico(presidents_full_name, files_names, presidents_name)

    # to erase
    print(dico_presidents)
    print()

# ----DICTIONARY------------------------------------------------------------------------------
    directory = "./cleaned"
    dictionary_of_files, total_dictionary = dict(), dict() 
    string_of_file, total_string = str(), str()
    
    # Creation of a dico of words occurency for each file saved in dictionary_of_files
    for file in files_names :
        
        with open(directory + "/" + file , "r", encoding = 'utf-8') as f:
            for line in f :
                for word in (line.strip()).split(' ') :
                    string_of_file = string_of_file + " " + word
        # Call the function count_words
        dico_of_file = count_words(string_of_file)
        # Fill the dico dictionary_of_files as : {"name file" : dico of the file }
        dictionary_of_files[file] = dico_of_file
        
        total_string += string_of_file
    
    # Creation a dico of words occurence for the corpus
    # Call the function count_words
    total_dictionary = count_words(total_string)

    # Create a list with keys of total_dictionary
    all_words = []
    for key in total_dictionary.keys():
        all_words.append(key)
    all_words.sort()
# --------------------------------------------------------------------------------------------
    
    # Call the functions dico_IDF and mat_TF_IDF
    IDF = dico_IDF(all_words, dictionary_of_files)
    mat = mat_TF_IDF(all_words, dictionary_of_files, IDF)

    # Call the function less_important_words and display the result
    list_less_imp = less_important_words(all_words, total_dictionary, mat)
    print("Least important words in the document corpus :", list_less_imp)
    print()

    # Call the function higher_TF_IDF and display the result
    biggest_score_TF_IDF = higher_TF_IDF(all_words, total_dictionary, mat)
    print("Word(s) with the highest TD-IDF score : ",biggest_score_TF_IDF)

    # Call the function frequent_word_for_a_president : display the most repeated word(s) by a President
    name = 'Chirac'
    frequent_words = frequent_word_for_a_president(name, dictionary_of_files)
    print(f"Most repeated word(s) by President {name} :", frequent_words)

    # Look for who said "nation" and who repeated it the most
    word = 'nation'
    repeated = term_research(word, dictionary_of_files, dico_presidents)
    print(f'{word} is repeated by  :', repeated)




