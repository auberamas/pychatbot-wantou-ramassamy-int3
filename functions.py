# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:58:30 2023

@authors: Ariel WANTOU, Aube RAMASSAMY
"""
import os
from math import *
import string


# Create a list of files name from a given directory and extension of the files
def list_of_files(directory, extension):

    files_names = []
    for filename in os.listdir(directory):  # scan the list of file in the directory
        if filename.endswith(extension):  # verify the extension of the file
            files_names.append(filename)
            
    return files_names


# Replace all uppercase by lowercase one by one
def turn_text_in_lowercase(file_list):
    lowercase_file_list = []
    for line in file_list:
        for char in line:
            if char.isupper():
                line = line.replace(char, chr(ord(char) + 32))
        lowercase_file_list.append(line)
    return lowercase_file_list


# Remove punctuation and put space instead of "'" and "-"
def clean_text(file):
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


# Create a list of presidents name from a list of file's name
def name_of_presidents(files_name):
    
    presidents_name = []
    for name in files_name :
        name = name.split('_')  # Create a list : [nomination, name.txt]
        name[1] = name[1].strip('.txt')  # Clean the name from extension
        
        # Clean the name from numbers
        if name[1][-1].isdigit() :
            name[1] = name[1].replace(name[1][-1],"")
        
        # Add "'"
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


# Create a dictionary as : {"file_name" : "name"}
# Take three lists as parameters
def fill_dico(full_name, file_list, name_list):

    president_file = {}
    for file in range(len(file_list)):
        for name in range(len(name_list)):
            if (name_list[name].split(" "))[0] in file_list[file]:
                president_file[file_list[file]] = full_name[name]

    return president_file


# Display a list in two different ways
# "choice" allows to display a list either one element by line or in one line with comma
def display(liste, choice="\n", message1="", message2=""):
    count= 0

    if message1 != "":
        print()
        print(message1, end = "")

    for name in liste :
        if count == len(liste)-1 and choice != '\n':
            choice = "\n"
        print(name, end=choice)
        count += 1

    if message2!= "":
        print(message2)


# Computation of the occurrence of words in a text
def count_words(string):  # create a dico : {"word" : occurrence of the word }
    
    list_words = string.split(" ")
    words_dico = dict()
    for word in list_words :
        if word not in words_dico and word != "" and word != "\n":
            words_dico[word] = list_words.count(word)
    return words_dico


# Calcul the IDF (Inverse Document Frequency)
# return a dico as : {"word": IDF of the word"}
def dico_IDF(all_words : list, dico_files : dict):
    
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
def mat_TF_IDF(all_words, dico_files, IDF):

    mat = []    
    for word in all_words :
        line = []
        for file in dico_files :
            if word in dico_files[file] :
                # TF = occurrence of the word in the file / number of word in the file
                TF = dico_files[file][word]
                line.append(TF * IDF[word])
            else :
                line.append(0.0)
        mat.append(line)   
    return mat


# Create a list of the highest or lowest TF-IDF vector
def vector_research(all_words, mat, vector: list):

    vect_word = tuple()
    same_vect = []

    # Search all vectors equals to the vector
    for line in range(len(mat)):
        vect_word = (sum(mat[line]),line)
        if vector == vect_word[0] :
            same_vect.append(all_words[line])

    return same_vect


# Return the word with the highest TF-IDF score
def score_research(all_words, mat):

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


# Create a dico to know the occurrence of a word in each president's speech
# Shape of the dico : {"president" : occurrence of the word}
def term_research(term, dico_files, dico_name ):
    term_in = dict()
    for file in dico_files :
        if term in dico_files[file] :
            if dico_name[file] in term_in :
                term_in[dico_name[file]] += dico_files[file][term]
            else :
                term_in[dico_name[file]]= dico_files[file][term]
    return term_in

def question_treatment(list_text):

    list_text = turn_text_in_lowercase(list_text)
    list_text = clean_text(list_text)
    list_text = list_text[0].split(" ")
    for char in list_text :
        if char == " ":
            del list_text[char]

    return list_text