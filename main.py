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

    #debug
    #for i in range(len(all_words)) :
    #   print(all_words[i],mat[i], sum(mat[i]))
# ----Features---------------------------------------------------------------------------------

    Do = 0
    print( "Actions:")
    print("- 1 to choose an action from the menu")
    print("- 2 to ask a question")
    Do = int(input("What do you want to do: " ))
    print()

    if Do == 1 :

        menu = ["1- Least important word(s) of the corpus",
                "2- Most important word(s) of the corpus",
                "3- The most repeated word by Chirac",
                "4- Who spoke about 'nation' and who repeated it the most",
                "5- Who spoke about 'climate' or 'ecology' for the first time",
                "6- Words that all presidents said"]

        action =  1
        while action == 1 :

            choice = 0
            print("-" * 60)
            print("Menu of features: ")
            display(menu)
            print()

            # Ask the user to choice an action in the menu
            choice = 0
            # Verify that "choice" is available in the menu
            while choice < 1 or choice > len(menu):
                choice = int(input("Choose an action in the menu, enter it's number: "))
            print()

            if choice == 1:
                # Look for the less important words (lowest TD-IDF score)
                min_vector = sum(min(mat))  # Calculate the sum of the lowest vector's values in the TF-IDF matrix

                # Call the function vector_research to search all the vectors equal to the lowest one
                lowest_score_TF_IDF = vector_research(all_words, mat, min_vector)
                print("Least important word(s) in the corpus: ", end = "")
                # Call the function display
                display(lowest_score_TF_IDF, ", ")
                print()

            if choice == 2:
                # Looking for the most important words (highest TD-IDF score)

                # Call the function vector_research to search all the vectors equal to the highest one
                biggest_score_TF_IDF = score_research(all_words, mat)
                print("Most important word(s) in the corpus: ", end = "")
                # Call the function display
                display(biggest_score_TF_IDF, "")
                print()

            if choice == 3:
                # Look for the most frequent word of a president
                name = 'Chirac'

                # Look for the less important words (lowest TD-IDF score)
                min_vector = sum(min(mat))
                # Call the function vector_research to search all the vectors equal to the lowest one
                lowest_score_TF_IDF = vector_research(all_words, mat, min_vector)

                # Call the function frequent_word_for_a_president : display the most repeated word(s) by a President
                frequent_words = frequent_word_for_a_president(name, dictionary_of_files, lowest_score_TF_IDF)
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

                # Look for the less important words (lowest TD-IDF score)
                min_vector = sum(min(mat))
                # Call the function vector_research to search all the vectors equal to the lowest one
                lowest_score_TF_IDF = vector_research(all_words, mat, min_vector)

                for word in all_words:
                    if word not in lowest_score_TF_IDF :
                        # Call the function term_research : give the presidents who said the word and how much
                        word_occurrence = term_research(word, dictionary_of_files, dico_presidents)

                        # Verify if all presidents are in word_occurrence
                        if len(word_occurrence) == len(presidents_full_name):
                            common_words.append(word)

                print("The common words to all presidents are: ", end = "")
                # Call the function display
                display(common_words, ", ")
                print()

            # Ask the user if he wants to execute another action
            print("Do you want to execute another action?")
            again = -1
            while again !=0 and again!= 1:
                again = int(input("YES: 1, NO: 0 \n"))
            action = again

# ---- User's question ----------------------------------------------------------------

    if Do == 2 :

        can_answer, count, size = False, 0, 0

        # Check if the question can be treated
        while can_answer == False :
            if count == 0 and size == 0:
                question = input("Enter your question: ")
            elif size != 0 :
                print()
                print("We are sorry, but this is not a question.")
                question = input("Enter your question: ")
            else :
                print()
                print("We are sorry, but we can't answer to your question.")
                question = input("Enter another question: ")

            # Call the function question_treatment to see
            list_question = question_treatment([question])

            # Create a set of the intersection of the words in the question and in the corpus
            intersection_question_corpus = set(all_words) & set(list_question)
            # Convert the set into a list
            intersection_question_corpus = [*intersection_question_corpus]

            # Check if the intersection_question_corpus is empty
            # If it's not empty we can answer to the question otherwise the user have to ask something else

            if 0 < len(intersection_question_corpus) < 2:
                size += 1
            elif len(intersection_question_corpus) == 0:
                count += 1
            else :
                can_answer = True

        # Call transpose_matrix
        T_mat = transpose_matrix(mat)

        # Call the function vector_question
        vect_of_question = vector_question(IDF, intersection_question_corpus, list_question, all_words)

        # Call the function higher_similarity
        similarity = higher_similarity(T_mat, vect_of_question, files_names)
        display(similarity, "", "The question is similar to the following text: ")
