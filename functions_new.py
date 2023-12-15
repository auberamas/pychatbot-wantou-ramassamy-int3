# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:58:30 2023

Name of the Project : My first chatbot

@authors: Ariel WANTOU, Aube RAMASSAMY

role of the file : store all functions of the project

"""
import os
from math import *
import string


# Create a list of files name from a given directory and extension of the files
def list_of_files(directory: str, extension: str):

    files_names = []
    for filename in os.listdir(directory):  # scan the list of file in the directory
        if filename.endswith(extension):  # verify the extension of the file
            files_names.append(filename)
            
    return files_names


# Replace all uppercase by lowercase one by one
def turn_text_in_lowercase(file_list: list):
    lowercase_file_list = []
    for line in file_list:
        for char in line:
            if char.isupper():
                line = line.replace(char, chr(ord(char) + 32))
        lowercase_file_list.append(line)
    return lowercase_file_list


# Remove punctuation and put space instead of "'" and "-"
def clean_text(file:list):
    ponctuation = string.punctuation  # list of all punctuation
    cleaned_file = []
    for line in file:
        for char in line:
            if char in ponctuation:
                if char != "'" or char != "-":
                    line = line.replace(char, " ")
                else:
                    line = line.replace(char, "")
        cleaned_file.append(line)
    return cleaned_file

# Display a list in two different ways
# "choice" allows to display a list either one element by line or in one line with comma
def display(l, choice="\n", message1="", message2=""):
    """
    :param l: list
    :param choice: choose if we display one element by line (by default)
    :param message1: we can choose to display a message before the result
    :param message2: we can choose to display a message after the result
    :return: nothing, just display messages
    """
    count= 0

    if message1 != "":
        print()
        print(message1, end = "")

    for name in l :
        # If we are at the end of the list we go to a new line
        if count == len(l)-1 and choice != '\n':
            choice = "\n"
        print(name, end=choice)
        count += 1
    print()

    if message2!= "":
        print(message2)


# Create a list of presidents name from a list of file's name
# Return a list of president's name
def name_of_presidents(files_name:list):
    
    presidents_name = []
    for name in files_name :
        name = name.split('_')  # Create a list : [nomination, name.txt]
        name[1] = name[1].strip('.txt')  # Clean the name from extension
        
        # Clean the name from numbers
        if name[1][-1].isdigit() :
            name[1] = name[1].replace(name[1][-1],"")
        
        # Add "'" when there is a lower case next to an upper case as : dEstain to have -> d'Estain
        if " " in name[1] :
            sub_name = name[1].split(' ')  # We work on the part after the space
            for char in range(len(sub_name[1])-1) :
                # Try to find an uppercase next to a lowercase to put an apostrophe between
               if sub_name[1][char].islower() and sub_name[1][char+1].isupper() :
                    sub_name[1] = "'".join(sub_name[1][char:char+2]) + sub_name[1][char+2:]
            name[1] = sub_name[0]+" " + sub_name[1]
            
        # Verify if the name is already in the list of names
        if name[1] not in presidents_name : 
            presidents_name.append(name[1])
            
    return presidents_name


# Return the list of président's names
def list_of_names(files_names):
    # Call the function name_of_presidents
    presidents_name = name_of_presidents(files_names)

    presidents_first_name = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    # Create a list of full names with the concatenation of first name and name
    presidents_full_name = [presidents_first_name[i] + " " + presidents_name[i] for i in
                            range(len(presidents_first_name))]

    return presidents_full_name


# Create a dictionary as : {"file_name" : "name"}
# Take three lists as parameters
def fill_dico(full_name, file_list, name_list):
    """
    :param full_name: list
    :param file_list: list
    :param name_list:
    :return: dictionary
    """
    president_file = {}
    for file in range(len(file_list)):
        for name in range(len(name_list)):
            if (name_list[name].split(" "))[0] in file_list[file]:
                president_file[file_list[file]] = full_name[name]

    return president_file


def str_of_file(lines ):

    string_of_file = str()
    for line in lines:  # Run over line of the file
        # Word run over a list of words from a line of the file without the '\n'
        for word in (line.strip()).split(' '):
            # Create a string of all words in a file
            string_of_file = string_of_file + " " + word

    return string_of_file


# Computation of the occurrence of words in a text
def count_words(string):  # create a dico : {"word" : occurrence of the word }

    list_words = string.split(" ")
    words_dico = dict()
    for word in list_words:
        if word not in words_dico and word != "" and word != "\n":
            words_dico[word] = list_words.count(word)
    return words_dico


# Creation of a dictionary of the occurrence of words for each file saved in dictionary_of_files
# Creation of a dictionary of words occurrence for the corpus
def dico_tot (directory):

    dictionary_of_files, total_dictionary = dict(), dict()
    total_string = str()
    all_words = []

    # Call of the function list_of_files
    files_names = list_of_files(directory, "txt")
    # Open each file of the directory
    for file in files_names:
        dico_of_file, string_of_file = {}, str()  # Start with empty dico and string for each file
        with open(directory + "/" + file, "r", encoding='utf-8') as opened_file:
            lines = opened_file.readlines()
            # Call the function str_of_file
            string_of_file = str_of_file(lines)

        # Call the function count_words which returns a dico as : {"word" : occurrence} for each file
        dico_of_file = count_words(string_of_file)
        # Fill the dico dictionary_of_files as : {"file name" : dico of the file }
        dictionary_of_files[file] = dico_of_file

        # Create a string which is the concatenation of the string of all the corpus
        total_string += string_of_file

        # Call the function count_words
        total_dictionary = count_words(total_string)

        # Create a list of total_dictionary's keys
        all_words = [*total_dictionary.keys()]
        all_words.sort()

    return all_words, dictionary_of_files


# Calcul the IDF (Inverse Document Frequency)
# return a dico as : {"word": IDF of the word"}
def dico_IDF(directory):

    # Call the function dic_tot
    all_words, dico_files = dico_tot (directory)
    IDF_score_dico = dict()
    for word in all_words :
        word_in_file, IDF = 0, 0
        for file in dico_files :
            if word in dico_files[file] :
                word_in_file += 1  # Count the number of file where is "word"
        # Log((nb document/ nb document with the word)+1)
        IDF = log10((len(dico_files)/word_in_file) )   # Add 1 to avoid IDF = log(1) = 0
        IDF_score_dico[word] = IDF
    return IDF_score_dico


# Calculate the TF-IDF matrix of the shape : line = word ; column = file
def mat_TF_IDF(directory):

    all_words, dico_files = dico_tot(directory)
    IDF = dico_IDF((directory))
    mat = []    
    for word in all_words :
        line = []
        for file in dico_files :
            if word in dico_files[file] :
                # TF = occurrence of the word in the file
                TF = dico_files[file][word]
                line.append(TF * IDF[word])
            else :
                line.append(0.0)
        mat.append(line)   
    return mat


# Create a list of the highest or lowest TF-IDF vector
def vector_research(all_words, mat, vector: float):

    vect_word = tuple()
    same_vect = []

    # Search all vectors equals to the vector
    for line in range(len(mat)):
        vect_word = (sum(mat[line]),line)
        if vector == vect_word[0] :
            same_vect.append(all_words[line])

    return same_vect


# Look for the less important words (lowest TD-IDF score)


# Return the word with the highest TF-IDF score
def score_research(all_words, mat):
    """

    :param all_words: list of all the words in the corpus
    :param mat: matrix TF-IDF
    :return: the score of the word
    """
    list_highest = []
    highest = ("word", 0.0)
    for line in range(len(mat)):
        if highest[1] < max(mat[line]) :
            highest = (all_words[line], max(mat[line]))

    # Look if there is another word with the same score
    for line in range(len(mat)):
        if highest[1] == max(mat[line]) and highest[0] not in list_highest:
            highest = (all_words[line], max(mat[line]))
            list_highest.append(highest[0])

    return highest[0]


# Create a list with the most repeated word(s) by a president
def frequent_word_for_a_president(name, dico_of_files,  not_important):
    """

    :param name: it's the name of a président
    :param dico_of_files: it's the dictionary of file's dictionaries as {name_file:{ 'word' : occurrence},...}
    :param not_important: it's a float which the sum of a vector
    :return: the vector of the most frequent word
    """
    frequent_words = []
    for file in dico_of_files :
        if name in file :
            # Remove the list important words from the dictionary
            for word in not_important:
                if word in dico_of_files[file] :
                    del dico_of_files[file][word]

            most_frequent = max(dico_of_files[file].values())
            for word in dico_of_files[file]:
                if dico_of_files[file][word] == most_frequent and word not in frequent_words:
                    frequent_words.append(word)

    return frequent_words


def max_occurrence_word(repeated):

    max_word = max(repeated.values())  # keep the occurrence of the most repeated word
    for name in repeated:
        if repeated[name] == max_word:
            president = name

    return president


def oldest_president(repeated):

    print(repeated)
    oldest= 2023
    date_president = {"Valéry Giscard d'Estaing": 1974, "François Mitterrand": 1981,
                      "Jacques Chirac": 1995, "Nicolas Sarkozy": 2007, "François Hollande": 2012,
                      "Emmanuel Macron": 2017}

    # Comparing the values of date_president for names in repeated to know who is the oldest
    for name in [*repeated]:
        if date_president[name] < oldest:
            name_oldest = name
        oldest = date_president[name]

    return name_oldest


def common_words(dictionary_of_files, less_imp_words):
    list_set = []
    common = set()

    for file in dictionary_of_files:
        new_set = set()
    for word in dictionary_of_files[file].keys():
        new_set.add(word)
    list_set.append(new_set)
    print(list_set)

    common = list_set[0]
    for element in list_set[0:]:
        common = element & common
    common = common - less_imp_words

    return common


# Create a dico to know the occurrence of a word in each president's speech
def term_research(term, dico_files, dico_name ):
    """

    :param term:
    :param dico_files:
    :param dico_name:
    :return: a dico as  {"president" : occurrence of the word}
    """
    term_in = dict()
    for file in dico_files :
        if term in dico_files[file] :
            if dico_name[file] in term_in :
                term_in[dico_name[file]] += dico_files[file][term]
            else :
                term_in[dico_name[file]]= dico_files[file][term]
    return term_in


# Return a list of the words from a question
def question_treatment(list_text):

    # Call the function turn_text_in_lowercase
    list_text = turn_text_in_lowercase(list_text)
    # Call the function clean_text
    list_text = clean_text(list_text)

    # Create a list of words from list_text
    list_text = list_text[0].split(" ")
    # Remove spaces from the list
    for char in list_text :
        if char == " ":
            del list_text[char]

    return list_text


# Return the transpose of a matrix
def transpose_matrix(M):

    MT = []

    for col in range(len(M[0])):
        line = []
        for row in range(len(M)):
            line.append(M[row][col])
        MT.append(line)
    return MT


# Return the vector of a question
def vector_question(IDF, intersection_question_corpus, question, all_words):

    vect = []

    for word in all_words :
        if word in intersection_question_corpus:
            TF = question.count(word) / len(question)
            vect.append(TF * IDF[word])
        else :
            vect.append(0.0)
    return vect


# Return the scalar product of 2 vectors
def scalar_product(vect_A, vect_B):

    res = float()
    for val in range(len(vect_A)):
        res += vect_A[val] * vect_B[val]
    return res


# Return the norm of a vector
def norm(vect):

    res = float()
    for val in vect:
        res += val**2
    res = sqrt(res)

    return res


# Return the similarity value of 2 vectors
def similarity(vect_A, vect_B):

    # Call the function scalar_product
    scalar_p = scalar_product(vect_A, vect_B)
    # Call the function norm
    norm_A, norm_B = norm(vect_A), norm(vect_B)
    # Compute the similarity
    similar = scalar_p / (norm_A * norm_B)

    return similar


# Return the highest similarity between a vector and a matrix
def higher_similarity(T_mat, vect_question, files):

    highest, document = float(), str()

    for vect in range(len(T_mat)):
        res = similarity(T_mat[vect], vect_question)
        if highest < res :
            highest = res
            document = files[vect]

    return document

def actions(choice, directory):

    if choice == 1:
        # Call the function vector_research to search all the vectors equal to the lowest one
        lowest_score_TF_IDF = vector_research(all_words=dico_tot(directory)[0], mat=mat_TF_IDF(directory), vector = sum(min(mat_TF_IDF(directory))))
        display(lowest_score_TF_IDF, ", ", "Least important word(s) in the corpus: ")

    elif choice == 2:
        display(score_research(all_words = dico_tot (directory)[0], mat = mat_TF_IDF(directory)), "", "Most important word(s) in the corpus: " )

    elif choice == 3:
        # Look for the most frequent word of a president
        name = 'Chirac'
        lowest_score_TF_IDF = vector_research(all_words = dico_tot (directory)[0], mat = mat_TF_IDF(directory), vector = sum(min(mat_TF_IDF(directory))))
        display(frequent_word_for_a_president(name, dico_tot (directory)[1], lowest_score_TF_IDF ),", ", f"Most repeated word(s) by President {name}: ")

    elif choice == 4:
        # Look for who said "nation" and who repeated it the most
        word = 'nation'
        # Call the function fill_dico to create a dictionary as : { 'name of file' : 'president full name'}
        dico_presidents = fill_dico(list_of_names(list_of_files(directory, "txt")), list_of_files(directory, "txt"), name_of_presidents(list_of_files(directory, "txt")))
        display(term_research(word, dico_tot(directory)[1], dico_presidents), ", ", f"The word '{word}' is repeated by: ")
        # Look for who repeated 'nation' the most
        president = max_occurrence_word(term_research(word, dico_tot(directory)[1], dico_presidents))
        display(term_research(word, dico_tot(directory)[1], dico_presidents), ", ", f'{president} is the one who repeated {word} the most.')

    elif choice == 5:
        # Look for who said "climat" or "écologie" and who repeated it the most
        word1, word2 = 'climat', 'écologie'

        # Call the function fill_dico to create a dictionary as : { 'name of file' : 'president full name'}
        dico_presidents = fill_dico(list_of_files(directory, "txt"), list_of_files(directory, "txt"), name_of_presidents(list_of_files(directory, "txt")))

        # Call the function term_research for word1 and word2 and do the intersection of the two sets
        repeated = term_research(word1, dico_tot(directory)[1], dico_presidents) | term_research(word2, dico_tot(directory)[1], dico_presidents)
        print(repeated)
        display([], message1=f'{oldest_president(repeated)} is the first president to talk about "{word1}" or "{word2}".')

    elif choice == 6:

        # Look for the words said by all presidents
        common = dict()
        common = common_words(vector_research(all_words=dico_tot(directory)[0], mat=mat_TF_IDF(directory), vector = 0.0) )
        if common != {}:
            message = "The common words to all presidents are: "
        else:
            message = "There are no common words to all presidents."

        display(common, "", message)


def question():
    try:
        question = input("Enter your question: ")

        # Convert the set intersection into a list
        intersection_question_corpus = [*set(dico_tot(directory)[0]) & set(question_treatment([question]))]

        # Call the function vector_question
        vect_of_question = vector_question(dico_IDF(directory), intersection_question_corpus, question_treatment([question]), dico_tot(directory)[0])

        # Call the function higher_similarity
        similarity = higher_similarity(transpose_matrix(mat_TF_IDF(directory)), vect_of_question, list_of_files(directory, "txt"))
        display(similarity, "", "The question is similar to the following text: ")

    except:
        print("Enter something else")



def play(launch, directory):

    Do = int(input("What do you want to do ? Enter the number of an available action :   "))
    if Do == 1:
        choice = int(input("Choose a feature in the menu, enter it's number: "))
        actions(choice, directory)
    elif Do == 2:
        # Call the function question
        question()

    """
    try:
        Do = int(input("What do you want to do ? Enter the number of an available action :   "))
        if Do == 1:
            try:
                choice = int(input("Choose a feature in the menu, enter it's number: "))
                print(choice)
                actions(choice, directory)
            except Exception :
                print("Enter somthing else")

        elif Do == 2:
            # Call the function question
            question()
    except:
        print("Enter something else")
    """


