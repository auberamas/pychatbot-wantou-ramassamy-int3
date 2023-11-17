# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 07:08:35 2023

@author: Aube
"""
from main import files_names

def turn_file_in_lowercase(file_list):
    
    lowercase_file_list = []
    for line in file_list :
        for char in line :
            if char.isupper() :
                line = line.replace(char, chr (ord(char) + 32 ))
        lowercase_file_list.append(line)
    return(lowercase_file_list)
            
        
# Open files in the directory 'spechees' and build a list of lines for each files
for name in files_names :
    with open("speeches/"+ name, "r", encoding='utf-8') as f: #encoding to avoid problems with accents
        lines = f.readlines()

    # Call the function turn-file_in_lowercase
    file_list_lowercase = turn_file_in_lowercase(lines)
    
    # Write the text in lower case on a new file
    with open("cleaned/" + name, "a", encoding='utf-8') as f :
        for line in file_list_lowercase:
            f.write(line)