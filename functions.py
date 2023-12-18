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
    """
    :param directory: name of the repertory were are the files
    :param extension: extension of the files
    :return: the list of file's name in the directory
    """
    files_names = []
    for filename in os.listdir(directory):  # scan the list of file in the directory
        if filename.endswith(extension):  # verify the extension of the file
            files_names.append(filename)
            
    return files_names


# Replace all uppercase by lowercase one by one
def turn_text_in_lowercase(file_list):
    """
    :param file_list: list of str
    :return: list of str in lowercase
    """
    lowercase_file_list = []
    for line in file_list:
        for char in line:
            if char.isupper():
                line = line.replace(char, chr(ord(char) + 32))
        lowercase_file_list.append(line)

    return lowercase_file_list


# Remove punctuation and put space instead of "'" and "-"
def clean_text(file_lines):
    """
    :param file_lines: list of lines from a file
    :return: list of lines cleaned from "'" and "-"
    """
    ponctuation = string.punctuation  # list of all punctuation
    cleaned_file = []
    for line in file_lines:
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
def display(result, choice="\n", message1="", message2=""):
    """
    :param result: list of result to display
    :param choice: displays one element by line by default, we can also choose to display
    elements separated by commas
    :param message1: we can choose to display a message before the result
    :param message2: we can choose to display a message after the result
    :return: nothing, just display messages
    """
    count = 0

    if message1 != "":
        print()
        print(message1, end="")

    for elm in result:
        # If we are at the end of the list we go to a new line
        if count == len(result)-1 and choice != '\n':
            choice = "\n"
        print(elm, end=choice)
        count += 1
    print()

    if message2 != "":
        print(message2)


# Create a list of presidents name from a list of file's name
# Return a list of president's name
def name_of_presidents(files_name):
    """
    :param files_name: list of files names
    :return: list of names from files names
    """
    presidents_name = []
    for name in files_name:
        name = name.split('_')  # Create a list : [nomination, name.txt]
        name[1] = name[1].strip('.txt')  # Clean the name from extension
        
        # Clean the name from numbers
        if name[1][-1].isdigit():
            name[1] = name[1].replace(name[1][-1], "")
        
        # Add "'" when there is a lower case next to an upper case as : dEstain to have -> d'Estain
        if " " in name[1]:
            sub_name = name[1].split(' ')  # We work on the part after the space
            for char in range(len(sub_name[1])-1):
                # Try to find an uppercase next to a lowercase to put an apostrophe between
                if sub_name[1][char].islower() and sub_name[1][char+1].isupper():
                    sub_name[1] = "'".join(sub_name[1][char:char+2]) + sub_name[1][char+2:]
            name[1] = sub_name[0]+" " + sub_name[1]

        # Verify if the name is already in the list of names
        if name[1] not in presidents_name:
            presidents_name.append(name[1])

    return presidents_name


# Return the list of first name + last name
def list_of_names(files_names):
    """
    :param files_names: list of files names
    :return: the list of full name
    """

    # Call the function name_of_presidents
    presidents_name = name_of_presidents(files_names)

    presidents_first_name = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    # Create a list of full names with the concatenation of first name and name
    presidents_full_name = [presidents_first_name[i] + " " + presidents_name[i] for i in
                            range(len(presidents_first_name))]

    return presidents_full_name


# Create a dictionary which associate each file to a name
def fill_dico(full_name, file_list, name_list):
    """
    :param full_name: list of full names
    :param file_list: list of files name
    :param name_list: list of name
    :return: dictionary as {"file_name" : "name"}
    """
    president_file = {}
    for file in range(len(file_list)):
        for name in range(len(name_list)):
            if (name_list[name].split(" "))[0] in file_list[file]:
                president_file[file_list[file]] = full_name[name]

    return president_file


# Convert the extracted lines of a file to one string
def str_of_file(lines):
    """
    :param lines: list of str
    :return: a string
    """
    string_of_file = str()
    for line in lines:
        # Word run over a list of words from a line of the file without the '\n'
        for word in (line.strip()).split(' '):
            string_of_file = string_of_file + " " + word

    return string_of_file


# Computation of the occurrence of words in a string
def count_words(sentence):
    """
    :param sentence: it's a string
    :return: a dictionary as : {"word" : occurrence of the word }
    """
    list_words = sentence.split(" ")
    words_dico = dict()
    for word in list_words:
        if word not in words_dico and word != "" and word != "\n":
            words_dico[word] = list_words.count(word)

    return words_dico


# Open a file and give its content
def open_file(directory, file):
    """
    :param directory: string as "./name of the repertory"
    :param file:  name of the file
    :return: list of string contented in the file
    """

    with open(directory + "/" + file, "r", encoding='utf-8') as opened_file:
        lines = opened_file.readlines()

    return lines


# Creation of a dictionary of the occurrence of words for each file saved in dictionary_of_files
# Creation of a dictionary of words occurrence for the corpus
def dico_tot(directory):
    """
    :param directory: string as "./name of the repertory"
    :return: a tuple as (dico1, dico2)
    - dico1 : {"word1": occurrence, ...}
    - dico2 : {"file1": { "word1": occurrence, ...}, "file2": { "word1": occurrence, ...}...}
    """

    dictionary_of_files, total_dictionary = dict(), dict()
    total_string = str()
    all_words = []

    # Call of the function list_of_files
    files_names = list_of_files(directory, "txt")
    for file in files_names:
        dico_of_file, string_of_file = {}, str()
        # Call the function open_file, then str_of_file
        string_of_file = str_of_file(open_file(directory, file))
        # Call the function count_words which returns a dico as : {"word" : occurrence} for each file
        dico_of_file = count_words(string_of_file)
        # Fill the dico dictionary_of_files as : {"file name" : dico of the file }
        dictionary_of_files[file] = dico_of_file

        total_string += string_of_file
        # Call the function count_words
        total_dictionary = count_words(total_string)
        # Create a list of total_dictionary's keys
        all_words = [*total_dictionary.keys()]
        all_words.sort()

    return all_words, dictionary_of_files


# Calcul the IDF (Inverse Document Frequency)
def dico_idf(directory):
    """
    :param directory:  string as "./name of the repertory"
    :return: a dictionary as : {"word": IDF of the word"}
    """

    # Call the function dic_tot
    all_words, dico_files = dico_tot(directory)
    IDF_score_dico = dict()
    for word in all_words:
        word_in_file, IDF = 0, 0
        for file in dico_files:
            if word in dico_files[file]:
                word_in_file += 1
        # Log((nb document/ nb document with the word)+1)
        IDF = log10((len(dico_files)/word_in_file))
        IDF_score_dico[word] = IDF

    return IDF_score_dico


# Calculate the TF-IDF matrix
def mat_tf_idf(directory):
    """
    :param directory:  string as "./name of the repertory"
    :return: the TF-IDF matrix of the shape : line = word ; column = file
    """

    all_words, dico_files = dico_tot(directory)
    IDF = dico_idf(directory)
    mat = []    
    for word in all_words:
        line = []
        for file in dico_files:
            if word in dico_files[file]:
                # TF = occurrence of the word in the file
                TF = dico_files[file][word]
                line.append(TF * IDF[word])
            else:
                line.append(0.0)
        mat.append(line)

    return mat


# Create a list of the highest or lowest TF-IDF vector
def vector_research(all_words, mat, vector):
    """
    :param all_words: it's a dictionary as {"word" : occurrence,...}
    :param mat: it's a matrix of float
    :param vector: it's a float
    :return: a list which contain all vectors equal to the parameter vector
    """

    vect_word = tuple()
    same_vect = []

    # Search all vectors equals to the vector
    for line in range(len(mat)):
        vect_word = (sum(mat[line]), line)
        if vector == vect_word[0]:
            same_vect.append(all_words[line])

    return same_vect


# Return the word with the highest TF-IDF score
def highest_score(all_words, mat):
    """
    :param all_words: list of all the words in the corpus
    :param mat: matrix of float
    :return: the word with the highest score in the matrix mat
    """
    list_highest = []
    highest = ("word", 0.0)
    for line in range(len(mat)):
        if highest[1] < max(mat[line]):
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
    :param name: it's the name of a president
    :param dico_of_files: it's the dictionary of file's dictionaries as {name_file:{ 'word' : occurrence},...}
    :param not_important: it's a float which the sum of a vector
    :return: the vector of the most frequent word
    """
    frequent_words = []
    for file in dico_of_files:
        if name in file:
            # Remove the list important words from the dictionary
            for word in not_important:
                if word in dico_of_files[file]:
                    del dico_of_files[file][word]

            most_frequent = max(dico_of_files[file].values())
            for word in dico_of_files[file]:
                if dico_of_files[file][word] == most_frequent and word not in frequent_words:
                    frequent_words.append(word)

    return frequent_words


# Create a dico to know the occurrence of a word in each president's speech
def term_research(term, dico_files, dico_name):
    """
    :param term: it's a word
    :param dico_files: it's a dictionary as {"file1": { "word1": occurrence, ...}, "file2": { "word1": occurrence, ...}...}
    :param dico_name: it's a dictionary as {"file_name" : "name",...}
    :return: a dico as  {"name" : occurrence of the word,...}
    """
    term_in = dict()
    for file in dico_files:
        if term in dico_files[file]:
            if dico_name[file] in term_in:
                term_in[dico_name[file]] += dico_files[file][term]
            else:
                term_in[dico_name[file]] = dico_files[file][term]

    return term_in


# Look in a dictionary the key which have the highest value
def max_occurrence_word(repeated):
    """
    :param repeated: it's a dictionary as { string : value ,...}
    :return: a string
    """
    president = str()
    max_word = max(repeated.values())  # keep the occurrence of the most repeated word
    for name in repeated:
        if repeated[name] == max_word:
            president = name

    return president


# Look for who is the oldest in a dictionary
def oldest_president(repeated):
    """
    :param repeated: it's a dictionary as { string : value ,...}
    :return: a string
    """

    oldest, name_oldest = 2023, str()
    date_president = {"Valéry Giscard d'Estaing": 1974, "François Mitterrand": 1981,
                      "Jacques Chirac": 1995, "Nicolas Sarkozy": 2007, "François Hollande": 2012,
                      "Emmanuel Macron": 2017}

    for name in [*repeated]:
        if date_president[name] < oldest:
            name_oldest = name
        oldest = date_president[name]

    return name_oldest


# Look for the word said by all presidents
def common_words(dictionary_of_files, less_imp_words):
    """
    :param dictionary_of_files: it's the dictionary of file's dictionaries as {name_file:{ 'word' : occurrence},...}
    :param less_imp_words: it's a list of words
    :return: a set of words
    """
    list_set = []
    common = set()

    for file in dictionary_of_files:
        new_set = set()
        for word in dictionary_of_files[file].keys():
            new_set.add(word)
        list_set.append(new_set)

    common = list_set[0]
    for element in list_set[0:]:
        common = element & common
    common = common - {*less_imp_words}  # Turn less_imp_words in a set

    return common


# Return the transpose of a matrix
def transpose_matrix(mat):
    """
    :param mat: it's a matrix
    :return: the transposed matrix
    """

    t_mat = []

    for col in range(len(mat[0])):
        line = []
        for row in range(len(mat)):
            line.append(mat[row][col])
        t_mat.append(line)

    return t_mat


# Return the vector of a question
def vector_question(idf, intersection_question_corpus, sentence, all_words):
    """
    :param idf: a dictionary as : {"word": IDF of the word"}
    :param intersection_question_corpus: a list of words
    :param sentence: a list of words
    :param all_words: a list of words
    :return: a list of float
    """
    vect = []

    for word in all_words:
        if word in intersection_question_corpus:
            TF = sentence.count(word)
            vect.append(TF * idf[word])
        else:
            vect.append(0.0)

    return vect


# Return the scalar product of 2 vectors
def scalar_product(vect_a, vect_b):
    """
    :param vect_a: it's a list of float
    :param vect_b: it's a list of float
    :return: the scalar product of 2 vect_a and vect_b which is a float
    """
    res = float()
    for val in range(len(vect_a)):
        res += vect_a[val] * vect_b[val]

    return res


# Return the norm of a vector
def norm(vect):
    """
    :param vect: it's a list of float
    :return: the norm a vector which is a float
    """
    res = float()
    for val in vect:
        res += val**2
    res = sqrt(res)

    return res


# Return the file name with the highest similarity between a vector and the content of the document
def higher_similarity(t_mat, vect_question, files):
    """
    :param t_mat: it's a matrix (transposed TF_IDF matrix) as lines = files, columns = words
    :param vect_question: list of values
    :param files: list of files names of the "cleaned" directory
    :return: a file name
    """

    highest, document, similar = 0, str(), 0
    # Call the function norm
    norm_a = norm(vect_question)
    for vect in range(len(t_mat)):
        # Verify that the highest IDF of the question is in the document
        if t_mat[vect][vect_question.index(max(vect_question))] != 0:
            # Call the function scalar_product
            scalar_p = scalar_product(t_mat[vect], vect_question)
            # Call the function norm
            norm_b = norm(t_mat[vect])
            # Compute the similarity
            similar = scalar_p / (norm_a * norm_b)

        if highest < similar:
            highest = similar
            document = files[vect]

    return document


# Return the appropriate beginning to answer to the question
def begin_answer(sentence):
    """
    :param sentence: it's a string
    :return: a string
    """

    begin = str()

    question_starters = {
        "comment": "Après analyse, ",
        "pourquoi": "Car, ",
        "peux tu": "Oui, bien sûr ! ",
        "qu est ce que": "Il semblerait que ",
        "est ce que": "Il semblerait que ",
    }
    for word in [*question_starters.keys()]:
        if word in sentence[:15]:
            begin = question_starters[word]

    return begin


# Give the first sentence were a word appear in a file
def answer(word, file, directory, first_directory, begin):
    """
    :param : all parameters are strings
    :return: a tuple of string
    """

    sentence, index_line, count = int(), int(), 0
    lines = open_file(directory, file)
    # Search the line where appears "word" for the first time in the files in "cleaned"
    for sentence in range(len(lines)):
        for term in lines[sentence].split(" "):
            if word == term and count == 0:
                index_line = sentence
                count += 1
    # Search the line find before in the files in "speeches"
    sentence = open_file(first_directory, file)[index_line]

    # Shape the answer according the form of "begin"
    if (begin == str()) or (begin[-2] not in [".", "!"]):
        sentence = chr(ord(sentence[0])+32) + sentence[1:]
    if not sentence[0].isalpha():
        sentence = sentence[1:]

    if sentence.isupper():
        if (begin == str()) or (begin[-2] not in [".", "!"]):
            sentence = sentence[0] + sentence[1:].lower()
        else:
            sentence = sentence.lower()

    return sentence, begin


# Return a list of the words from a question
def question_treatment(list_text):
    """
    :param list_text: list of string
    :return: list of string cleaned from space and special characters
    """

    # Call the function turn_text_in_lowercase
    list_text = turn_text_in_lowercase(list_text)
    # Call the function clean_text
    list_text = clean_text(list_text)

    # Create a list of words from list_text
    list_text = list_text[0].split(" ")
    # Remove spaces from the list
    for char in list_text:
        if char == " ":
            del list_text[char]

    return list_text


# Compute the feature chose by the user
def features(choice, directory):
    """
    :param choice: it's an integer
    :param directory: string as "./name of the repertory"
    :return: nothing, just allow to call the right functions to display the result asked by the user
    """

    if choice == 1:
        # Call the function vector_research to search all the vectors equal to the lowest one
        lowest_score_TF_IDF = vector_research(all_words=dico_tot(directory)[0], mat=mat_tf_idf(directory), vector=sum(min(mat_tf_idf(directory))))
        display(lowest_score_TF_IDF, ", ", "Least important word(s) in the corpus: ")

    elif choice == 2:
        display(highest_score(all_words=dico_tot(directory)[0], mat=mat_tf_idf(directory)), "", message1="Most important word(s) in the corpus: ")

    elif choice == 3:
        # Look for the most frequent word of a president
        name = 'Chirac'
        lowest_score_TF_IDF = vector_research(all_words=dico_tot(directory)[0], mat=mat_tf_idf(directory), vector=sum(min(mat_tf_idf(directory))))
        display(frequent_word_for_a_president(name, dico_tot(directory)[1], lowest_score_TF_IDF), ", ", f"Most repeated word(s) by President {name}: ")

    elif choice == 4:
        # Look for who said "nation" and who repeated it the most
        word = 'nation'
        # Call the function fill_dico to create a dictionary as : { 'name of file' : 'president full name'}
        dico_presidents = fill_dico(list_of_names(list_of_files(directory, "txt")), list_of_files(directory, "txt"), name_of_presidents(list_of_files(directory, "txt")))
        # Look for who repeated 'nation' the most
        president = max_occurrence_word(term_research(word, dico_tot(directory)[1], dico_presidents))
        display(term_research(word, dico_tot(directory)[1], dico_presidents), ", ", message1=f"The word '{word}' is repeated by: ",
                message2=f"{president} is the one who repeated '{word}' the most.\n")

    elif choice == 5:
        # Look for who said "climat" or "écologie" and who repeated it the most
        word1, word2 = 'climat', 'écologie'

        # Call the function fill_dico to create a dictionary as : { 'name of file' : 'president full name'}
        dico_presidents = fill_dico(list_of_names(list_of_files(directory, "txt")), list_of_files(directory, "txt"), name_of_presidents(list_of_files(directory, "txt")))

        # Call the function term_research for word1 and word2 and do the intersection of the two sets
        repeated = term_research(word1, dico_tot(directory)[1], dico_presidents) | term_research(word2, dico_tot(directory)[1], dico_presidents)
        display([], message1=f'{oldest_president(repeated)} is the first president to talk about "{word1}" or "{word2}".')

    elif choice == 6:
        # Call vector research to have the less important words
        lowest_score_TF_IDF = vector_research(all_words=dico_tot(directory)[0], mat=mat_tf_idf(directory),
                                              vector=sum(min(mat_tf_idf(directory))))
        # Look for the words said by all presidents
        common = dict()
        common = common_words(dico_tot(directory)[1], lowest_score_TF_IDF)
        if common != set():
            message = "The common words to all presidents are: "
        else:
            message = "There are no common words to all presidents.\n"

        display(common, ", ", message)


# Treat the question of the user to give him an answer
def question(directory, first_directory):
    """
    :param directory: string as "./name of the repertory"
    :param first_directory: string as "./name of the repertory"
    :return: nothing, just allow to call the right functions to display the answer to user's question
    """
    question, intersection_question_corpus, can_treat = str(), [], False

    while can_treat != True:
        try:
            question = input("Enter your question: ")
            # Convert the set intersection between the corpus and the question into a list
            intersection_question_corpus = [*set(dico_tot(directory)[0]) & set(question_treatment([question]))]
            # Call the function vector_question
            vect_of_question = vector_question(dico_idf(directory), intersection_question_corpus, question_treatment([question]), dico_tot(directory)[0])
            # Call the function higher_similarity
            similar = higher_similarity(transpose_matrix(mat_tf_idf(directory)), vect_of_question, list_of_files(directory, "txt"))

            can_treat = True
        except:
            print("Sorry, this question can not be treated, enter something else.")

    print()
    begin = str()

    # Search the word with the highest tf_idf of the question in the list of all words of the corpus
    highest_TF_IDF = dico_tot(directory)[0][vect_of_question.index(max(vect_of_question))]
    # Shape the answer
    response, begin = answer(highest_TF_IDF, similar, directory, first_directory, begin_answer(" ".join(question_treatment([question]))))

    display([response], message1=begin)


# Ask the user what he wants to do
def play(directory, first_directory):
    """
    :param directory: string as "./name of the repertory"
    :param first_directory:  string as "./name of the repertory"
    :return: nothing, just allow to call the right function depending on user's choices
    """

    action, choice = 0, -1
    while action != 1 and action != 2:
        try:
            action = int(input("What do you want to do ? Enter the number of an available action :   "))
        except:
            print("Enter something else.\n")

    if action == 1:
        while 0 > choice or choice > 7:
            try:
                choice = int(input("Choose a feature in the menu, enter it's number: "))
                features(choice, directory)
            except:
                print("Enter something else.\n")

    elif action == 2:
        # Call the function question
        question(directory, first_directory)
