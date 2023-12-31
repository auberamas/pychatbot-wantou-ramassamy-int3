# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 07:08:35 2023

@authors: Ariel WANTOU, Aube RAMASSAMY

role of the file :
- clean txt files (remove punctuation and uppercase)
- store the new files in the new repertory "cleaned"
"""

from functions import *
import os

# Call of the function list_of_files
directory = "./speeches"
files_names = list_of_files(directory, "txt")

# create a directory to save the cleaned files
os.mkdir("cleaned")

# Open files in the directory 'speeches' and build a list of lines for each files
for name in files_names:
    # Call the function open_file which returns the list of file's lines
    lines = open_file("speeches", name)

    # Call the function turn_file_in_lowercase
    file_list_lowercase = turn_text_in_lowercase(lines)

    # Call function clean_file to remove punctuation, '-' and "'"
    cleaned_file = clean_text(file_list_lowercase)

    # Write the text in lower case on a new file
    with open("cleaned/" + name, "a", encoding='utf-8') as f:
        for line in cleaned_file:
            f.write(line)
