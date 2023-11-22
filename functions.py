# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:58:30 2023

@author: Aube
"""
import os
from math import *


def list_of_files(directory, extension): # create a list of files name

    files_names = []
    for filename in os.listdir(directory): # scan the list of file in the directory
        if filename.endswith(extension): # verify the extention of the file
            files_names.append(filename)
            
    return files_names


def name_of_presidents(files_name): # create a list of presidents name
    
    presidents_name = []
    for name in files_name :
        name = name.split('_') # create a list : [nomination, name.txt]
        name[1] = name[1].strip('.txt')# clean the name from extension
        
        # clean the name from numbers
        if name[1][-1].isdigit() :
            name[1] = name[1].replace(name[1][-1],"")
        
        #add "'" 
        if " " in name[1] :
            sub_name = name[1].split(' ') # we work on the part after the space
            for char in range(len(sub_name[1])-1) :
               if sub_name[1][char].islower() and sub_name[1][char+1].isupper() :
                    sub_name[1] = "'".join(sub_name[1][char:char+2]) + sub_name[1][char+2:]
            name[1] = sub_name[0]+" " +sub_name[1]
            
        # verify if the name is already in the list of names          
        if name[1] not in presidents_name : 
            presidents_name.append(name[1])
            
    return presidents_name


def fill_dico(full_name, file_list, name_list):  # create a dico : {"file_name" : "name"}

    president_file = {}
    for file in range(len(file_list)):
        for name in range(len(name_list)):
            if (name_list[name].split(" "))[0] in file_list[file]:
                president_file[file_list[file]] = full_name[name]

    return president_file


def display(liste, choice="\n"):  # display a list
    count = 0

    for name in liste :
        if count == len(liste)-1 and choice != '\n':
            choice = "\n"
        print(name, end=choice)
        count += 1


# Computation of Term Frequency
def count_words(string): # create a dico : {"word" : occurence of the word }
    
    list_words = string.split(" ")
    words_dico = dict()
    for word in list_words :
        if word not in words_dico and word != "" and word != "\n":
            words_dico[word] = list_words.count(word)
    return words_dico


# Calcul of the IDF (Inverse Document Frequency)  
def dico_IDF(all_words, dico_files):
    
    IDF_score_dico = dict()
    for word in all_words :
        word_in_file, IDF = 0, 0
        for file in dico_files :
            if word in dico_files[file] :
                word_in_file += 1 # To count the nb of file where is the word
                
        IDF = log(len(dico_files)/word_in_file)
        IDF_score_dico[word] = IDF
    return IDF_score_dico


# Calculate the TF-IDF matrix of the shape : line = word ; column = file
def mat_TF_IDF(all_words, dico_files, IDF):
    
    mat = []    
    for word in all_words :
        line = []
        for file in dico_files :
            if word in dico_files[file] :
                TF = (dico_files[file][word]/len(dico_files[file]))
                line.append(TF * IDF[word])
            else :
                line.append(0)
        mat.append(line)   
    return mat


# Create a list of less important words: with a TF-IDF vector equal to 0
def less_important_words(all_words, dico_tot, mat):

    nonimportant_words = []
    for line in range(len(mat)) :
        if sum(mat[line])== 0 :
            nonimportant_words.append(all_words[line])
    
    return nonimportant_words


# Create a list of the highest TF-IDF vector
def higher_TF_IDF(all_words, dico_tot, mat):

    couple, biggest_vector = tuple(), float()
    list_words_biggest_vect = []
    for line in range(len(mat)):
        couple = (sum(mat[line]),line)
        if biggest_vector < couple[0] :
            biggest_vector = couple[0]

    for line in range(len(mat)):
        couple = (sum(mat[line]),line)
        if biggest_vector == couple[0] :
            list_words_biggest_vect.append(all_words[line])

    return list_words_biggest_vect


# Create a list with the most repeated word(s) by a president
def frequent_word_for_a_president(name, dico_of_files):
    frequent_words = []
    for file in dico_of_files :
        if name in file :
            most_frequent = max(dico_of_files[file].values())
            for word in dico_of_files[file]:
                if dico_of_files[file][word] == most_frequent and word not in frequent_words :
                    frequent_words.append(word)

    return frequent_words


# Create a dico to know the occurrence of a word in each president's speech
def term_research(term, dico_files, dico_name ):
    term_in = dict()
    for file in dico_files :
        if term in dico_files[file] :
            if dico_name[file] in term_in :
                term_in[dico_name[file]] += dico_files[file][term]
            else :
                term_in[dico_name[file]]= dico_files[file][term]
    return term_in




            
            
    
    
