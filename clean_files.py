# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 07:08:35 2023

@author: Aube
"""
from main import files_names
from functions import *
import string
import os


# Replace all uppercase by lowercase one by one
def turn_file_in_lowercase(file_list):
    
    lowercase_file_list = []
    for line in file_list:
        for char in line:
            if char.isupper():
                line = line.replace(char, chr(ord(char) + 32))
        lowercase_file_list.append(line)
    return lowercase_file_list


# Remove punctuation and put space instead of "'" and "-"
def clean_file(file):
    
    ponctuation = string.punctuation # list of all punctuation
    cleaned_file = []
    for line in file :
        for char in line:
            if char in ponctuation:
                if char != "'" or char != "-" :
                    line = line.replace(char," ")
                else :
                    line = line.replace(char, "")
        cleaned_file.append(line)
    return cleaned_file

# create a directory to save the cleaned files
os.mkdir("cleaned")

# Open files in the directory 'spechees' and build a list of lines for each files
for name in files_names :
    with open("speeches/"+ name, "r", encoding='utf-8') as f: # Encoding to avoid problems with accents
        lines = f.readlines()

    # Call the function turn_file_in_lowercase
    file_list_lowercase = turn_file_in_lowercase(lines)

    # Call function clean_file to remove punctuation, '-' and "'"
    cleaned_file = clean_file(file_list_lowercase)
    
    # Write the text in lower case on a new file
    with open("cleaned/" + name, "a", encoding='utf-8') as f :
        for line in cleaned_file:
            f.write(line)
