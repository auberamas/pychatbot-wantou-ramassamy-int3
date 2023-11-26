# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:33:02 2023

@author: Ariel WANTOU, Aube RAMASSAMY
"""
from functions import *
    
# Call of the function list_of_files
directory = "./speeches"
files_names = list_of_files(directory, "txt")

if __name__ == '__main__':

    # Call of the function name_of_presidents
    presidents_name = name_of_presidents(files_names) # Return a list of president's name

    # Create a list of full names with the concatenation of first name and name
    presidents_first_name = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    presidents_full_name = [presidents_first_name [i] + " " + presidents_name[i] for i in range(len(presidents_first_name ))]

    print("-" * 60)
    print("President's name of the corpus: ")
    # Call the function display_full_name to display president name
    display(presidents_full_name)
    print()

    # Call the function fill_dico to create a dictionary as : { 'name of file' : 'president full name'}
    dico_presidents = fill_dico(presidents_full_name, files_names, presidents_name)
    date_president = {"Valéry Giscard d'Estaing": 1974, "François Mitterrand": 1981,
                      "Jacques Chirac": 1995, "Nicolas Sarkozy": 2007, "François Hollande": 2012,
                      "Emmanuel Macron": 2017}

# ----Creation of dictionaries---------------------------------------------------------------------

    directory = "./cleaned"
    dictionary_of_files, total_dictionary = dict(), dict() 
    total_string = str()
    
    # Creation of a dictionary of the occurrence of words for each file saved in dictionary_of_files
    # Open each file of the directory
    for file in files_names :
        dico_of_file, string_of_file = {}, str()  # Start with empty dico and string for each file
        with open(directory + "/" + file , "r", encoding = 'utf-8') as opened_file:
            for line in opened_file : # Run over line of the file
                # Word run over a list of words from a line of the file without the '\n'
                for word in (line.strip()).split(' ') : 
                    # Create a string of all words in a file
                    string_of_file = string_of_file + " " + word

        # Call the function count_words which returns a dico as : {"word" : occurrence} for each file
        dico_of_file = count_words(string_of_file)
        # Fill the dico dictionary_of_files as : {"file name" : dico of the file }
        dictionary_of_files[file] = dico_of_file

        # Create a string which is the concatenation of the string of all the corpus
        total_string += string_of_file
    
    # Creation of a dictionary of words occurrence for the corpus
    # Call the function count_words
    total_dictionary = count_words(total_string)

    # Create a list with keys(words) of total_dictionary : it's the list of words of all the corpus
    all_words = []
    for key in total_dictionary.keys():
        all_words.append(key)
    all_words.sort()
    
# ----Creation of the TF-IDF matrix ------------------------------------------------------------
    
    # Call the functions dico_IDF
    IDF = dico_IDF(all_words, dictionary_of_files)
    # Call the functions mat_TF_IDF
    mat = mat_TF_IDF(all_words, dictionary_of_files, IDF)

# ----Features---------------------------------------------------------------------------------

    menu = ["1- Least important word(s) of the corpus",
            "2- Most important word(s) of the corpus",
            "3- The most repeated word by Chirac",
            "4- Who spoke about 'nation' and who repeated it the most",
            "5- Who spoke about 'climate' or 'ecology' for the first time",
            "6- Words that all presidents said"]

    start = 1
    while start == 1 :

        print("-" * 60)
        print("Menu of features: ")
        # Call the function display
        display(menu)
        print()

        # Ask the user to choice an action in the menu
        choice = 0
        # Verify that "choice" is available in the menu
        while choice < 1 or choice > len(menu):
            choice = int(input("Choose an action in the menu, enter it's number: "))
        print()

        if choice == 1:
            # Looking for the less important words (lowest TD-IDF score)
            min_vector = sum(min(mat))  # Calculate the sum of the lowest vector's values in the TF-IDF matrix

            # Call the function vector_research to search all the vectors equal to the lowest one
            lowest_score_TF_IDF = vector_research(all_words, total_dictionary, mat, min_vector)
            print("Least important word(s) in the corpus: ", end = "")
            # Call the function display
            display(lowest_score_TF_IDF, ", ")
            print()

        if choice == 2:
            # Looking for the most important words (highest TD-IDF score)
            max_vector = sum(max(mat))  # Calculate the sum of the highest vector's values in the TF-IDF matrix

            # Call the function vector_research to search all the vectors equal to the highest one
            biggest_score_TF_IDF = vector_research(all_words, total_dictionary, mat, max_vector)
            print("Most important word(s) in the corpus: ", end = "")
            # Call the function display
            display(biggest_score_TF_IDF, ", ")
            print()

        if choice == 3:
            # Look for the most frequent word of a president
            name = 'Chirac'
            # Call the function frequent_word_for_a_president : display the most repeated word(s) by a President
            frequent_words = frequent_word_for_a_president(name, dictionary_of_files)
            print(f"Most repeated word(s) by President {name}: ", end = "")
            # Call the function display
            display(frequent_words, ", ")

        if choice == 4:
            # Look for who said "nation" and who repeated it the most
            word = 'nation'
            # Call the function term_research
            repeated = term_research(word, dictionary_of_files, dico_presidents)

            print(f"The word '{word}' is repeated by: ", end="")
            # Call the function display to display presidents who spoke about 'nation'
            display(repeated.keys(), ", ")

            # Look for who repeated 'nation' the most
            max_word = max(repeated.values()) # keep the occurrence of the most repeated word
            for name in repeated:
                if repeated[name] == max_word:
                    president = name
                    print(f'{president} is the one who repeated {word} the most.')

        if choice == 5:
            # Look for who said "climat" or "écologie" and who repeated it the most
            word1 = 'climat'
            word2 = 'écologie'

            # Call the function term_research for word1 and word2
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
                # Call the function term_research : give the presidents who said the word and how much
                word_occurrence = term_research(word, dictionary_of_files, dico_presidents)

                # Verify if all presidents are in word_occurrence
                if len(word_occurrence) == len(presidents_full_name):
                    common_words.append(word)

            print("The common words to all presidents are: ", end = "")
            # Call the function display
            display(common_words, ", ")

        print("-"*60)

        # Ask the user if he wants to continue to execute actions
        print()
        print("Do you want to execute an other action ?")
        print("YES : 1 ; NO : 0")
        start = int(input("Enter your choice: "))
        print()