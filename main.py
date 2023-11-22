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
    presidents_name = name_of_presidents(files_names) # Return a list a president name

    # Create a list of full names with the concatenation of first name and name
    presidents_first_name = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    presidents_full_name = [presidents_first_name [i] + " " + presidents_name[i] for i in range(len(presidents_first_name ))]

    # Call the function display_full_name to display president name
    print()
    print("President's name of the corpus: ")
    display(presidents_full_name)
    print()

    # Create a dictionary as : { 'name of file' : 'president full name'}
    # Call the function fill_dico
    dico_presidents = fill_dico(presidents_full_name, files_names, presidents_name)
    date_president = {"Valéry Giscard d'Estaing": 1974, "François Mitterrand": 1981,
                      "Jacques Chirac": 1995, "Nicolas Sarkozy": 2007, "François Hollande": 2012,
                      "Emmanuel Macron": 2017}

# ----Creation of dictionaries---------------------------------------------------------------------
    directory = "./cleaned"
    dictionary_of_files, total_dictionary = dict(), dict() 
    string_of_file, total_string = str(), str()
    
    # Creation of a dico of words occurrence for each file saved in dictionary_of_files
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
    
    # Creation a dico of words occurrence for the corpus
    # Call the function count_words
    total_dictionary = count_words(total_string)

    # Create a list with keys of total_dictionary
    all_words = []
    for key in total_dictionary.keys():
        all_words.append(key)
    all_words.sort()
# ----Creation of the TF-IDF matrix ------------------------------------------------------------
    
    # Call the functions dico_IDF and mat_TF_IDF
    IDF = dico_IDF(all_words, dictionary_of_files)
    mat = mat_TF_IDF(all_words, dictionary_of_files, IDF)

# ----Features---------------------------------------------------------------------------------
    # Menu
    menu = ["1- Least important words of the corpus",
            "2- Word(s) with the highest TDF-IDF score",
            "3- The most repeated word by Chirac",
            "4- Who spoke about 'nation' and who repeated it the most",
            "5- Who spoke about 'climate' or 'ecology' for the first time",
            "6- What are words that all presidents said ?"]

    # Call the function display
    display(menu)
    print()

    # Ask the user to choice an action in the menu
    choice = 0
    while choice < 1 or choice > len(menu):
        choice = int(input("Choose an action in the menu, enter it's number: "))
    print()

    if choice == 1:
        # Call the function less_important_words and display the result
        list_less_imp = less_important_words(all_words, total_dictionary, mat)
        print("Least important words in the document corpus :", list_less_imp)
        print()

    if choice == 2:
        # Call the function higher_TF_IDF and display the result
        biggest_score_TF_IDF = higher_TF_IDF(all_words, total_dictionary, mat)
        print("Word(s) with the highest TD-IDF score : ", biggest_score_TF_IDF)

    if choice == 3:

        # Call the function frequent_word_for_a_president : display the most repeated word(s) by a President
        name = 'Chirac'
        frequent_words = frequent_word_for_a_president(name, dictionary_of_files)
        print(f"Most repeated word(s) by President {name} :", frequent_words)

    if choice == 4:
        # Look for who said "nation" and who repeated it the most
        word = 'nation'
        # Call the function term_research
        repeated = term_research(word, dictionary_of_files, dico_presidents)

        print(f'The word {word} is repeated by: ', end="")
        # Call the function display to display presidents who spoke about 'nation'
        display(repeated.keys(), ", ")

        # Who repeated 'nation' the most
        max_word = max(repeated.values())
        for name in repeated:
            if repeated[name] == max_word:
                president = name
                print(f'{president} is the one who repeated {word} the most')

    if choice == 5:
        # Look for who said "climat" or "écologie" and who repeated it the most
        word1 = 'climat'
        word2 = 'écologie'
        # Call the function term_research
        # Return a dico as : {president : occurrence of the word}
        repeated1 = term_research(word1, dictionary_of_files, dico_presidents)
        repeated2 = term_research(word2, dictionary_of_files, dico_presidents)

        # Comparing the values of date_president for names in repeated to know who is the oldest
        repeated = repeated1 | repeated2
        oldest = 2023
        for name in repeated.keys():
            if date_president[name] < oldest:
                name_oldest = name
                oldest = date_president[name]
        print(f'{name_oldest} is the first president to talk about "{word1}" or "{word2}".')

    if choice == 6:
        # Look for the words said by all presidents
        common_words = []
        word_occurrence = dict()

        for word in all_words:
            # Call the function term_research
            # Give the president who said the word and how much
            word_occurrence = term_research(word, dictionary_of_files, dico_presidents)

            # Verify is all presidents are in word_occurrence
            if len(word_occurrence) == len(presidents_full_name):
                common_words.append(word)
        print(common_words)

