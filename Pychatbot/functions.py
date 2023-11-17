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
        if filename.endswith(extension):# verify the extention of the file
            files_names.append(filename)
            
    return (files_names)


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
            
    return(presidents_name)

def fill_dico(name, first_name): # create a dico : {"first name" : "name"}
    
    Presidents = {}
    for i in range(len(name)):
        Presidents[name[i]] = first_name[i]
        
    return(Presidents)

def display_full_name(dico_full_names): # display a dico as : key value
    
    for name in dico_full_names :
        print(dico_full_names[name], name)

# Create a list of lines of a file
def list_lines_in_file(file) :
    with open("cleaned2/"+ file, "r", encoding='utf-8') as f : 
        lines = f.readlines()
    return(lines)

# Computation of Term Frequency
def count_words(string): # create a dico : {"word" : occurence of the word }
    
    list_words = string.split(" ")
    words_dico = dict()
    for word in list_words :
        if word not in words_dico and word != "" and word != "\n":
            words_dico[word] = list_words.count(word)
    return(words_dico)

    
# Calcul of the IDF (Inverse Document Frequency)  
def dico_IDF(dico_tot, dico_files):
    
    IDF_score_dico = dict()
    for word in dico_tot :
        word_in_file, IDF = 0, 0
        for file in dico_files :
            if word in dico_files[file] :
                word_in_file += 1 # To count the nb of file where is the word
                
        IDF = log(len(dico_files)/word_in_file)
        IDF_score_dico[word] = IDF
    return(IDF_score_dico)

# Calculate the TF-IDF matrix
def mat_TF_IDF(dico_tot, dico_files, IDF):
    
    mat = []    
    for word in dico_tot :
        line = []
        for file in dico_files :
            if word in dico_files[file] : 
                line.append(dico_files[file][word] * IDF[word])
            else :
                line.append(0)
        mat.append(line)   
    return(mat)

def less_important_words(dico_tot, mat):
    
    # Create a list with keys of dico_tot
    dico_words = []
    for key in dico_tot.keys():
        dico_words.append(key) 
    
    # Create a list of less important words: with a TF-IDF vector equal to 0
    nonimportant_words = []
    for line in range(len(mat)) :
        if sum(mat[line])== 0 :
            nonimportant_words.append(dico_words[line])
    
    return(nonimportant_words)

def higher_TF_IDF(dico_tot, mat):

    dico_words = []
    for key in dico_tot.keys():
        dico_words.append(key)

    couple, biggest_vector = tuple(), float()
    list_words_biggest_vect = []
    for line in range(len(mat)):
        couple = (sum(mat[line]),line)
        if biggest_vector < couple[0] :
            biggest_vector = couple[0]

    for line in range(len(mat)):
        couple = (sum(mat[line]),line)
        if biggest_vector == couple[0] :
            list_words_biggest_vect.append(dico_words[line])

    return(list_words_biggest_vect)



            
            
    
    

