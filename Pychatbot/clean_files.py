# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 07:08:35 2023

@author: Aube
"""
from main import files_names
from functions import *
import string 


def turn_file_in_lowercase(file_list):
    
    lowercase_file_list = []
    for line in file_list :
        for char in line :
            if char.isupper() :
                line = line.replace(char, chr (ord(char) + 32 ))
        lowercase_file_list.append(line)
    return(lowercase_file_list)

def clean_file(file): #remove ponctuation and put space instead of "'" and "-"
    
    ponctuation = string.punctuation
    cleaned_file = []
    for line in file :
        for char in line :
            if char in ponctuation :
                if char != "'" or char != "-" :
                    line = line.replace(char," ")
                else :
                    line = line.replace(char, "")
        cleaned_file.append(line)
    return(cleaned_file)
              
        
# Open files in the directory 'spechees'and build a list of lines for each files
for name in files_names :
    with open("speeches/"+ name, "r", encoding='utf-8') as f: #encoding to avoid problems with accents
        lines = f.readlines()

    # Call the function turn_file_in_lowercase
    file_list_lowercase = turn_file_in_lowercase(lines)
    
    # Write the text in lower case on a new file
    with open("cleaned/" + name, "a", encoding='utf-8') as f :
        for line in file_list_lowercase:
            f.write(line)

# Open files in directory 'cleaned' and build a list of lines for each files
for file in files_names :
    with open("cleaned/"+ file, "r", encoding='utf-8') as f : 
        lines = f.readlines()

    # Call function clean_file to remove ponctuation, '-' and "'"
    cleaned_file = clean_file(lines)
    
    # Rewrite the cleaned text 
    with open("cleaned/" + file, "w", encoding='utf-8') as f :
        for line in cleaned_file :
            f.write(line)
    
# changer les partie pour avoir les listes des lignes dans les fichiers par la fonction