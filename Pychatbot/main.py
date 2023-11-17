# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:33:02 2023

@author: Aube
"""

from functions import *
    
# Call of the function list_of_files
directory = "./speeches"
files_names = list_of_files(directory, "txt")

if __name__ == '__main__':
    # Call of the function name_of_presidents
    presidents_name = name_of_presidents(files_names)
    
    # Create a dictionnary with name as key and first name as value
    # Call the function fill_dico
    presidents_first_name = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    dico_presidents = fill_dico(presidents_name, presidents_first_name)
    
    # Call the function display_full_name to diplay president name
    display_full_name(dico_presidents)

#----DICTIONARY------------------------------------------------------------------------------
    directory = "./cleaned"
    dictionary_of_files, total_dictionary = dict(), dict() 
    string_of_file, total_string = str(), str()
    
    #Creation of a dico of words occurency for each file saved in dictionary_of_files
    for file in files_names :
        
        with open(directory + "/" + file , "r", encoding = 'utf-8') as f:
            for line in f :
                for word in (line.strip()).split(' ') :
                    string_of_file = string_of_file + " " + word
        # Call the function count_words
        dico_of_file = count_words(string_of_file)
        # Fill the dico dictionary_of_files as : {"name file" : dico of the file }
        dictionary_of_files[file] = dico_of_file
        
        total_string += string_of_file
    
    #Calcul of TF(term Frequency) : creation a dico of words occurency for all files 
    # Call the function count_words
    total_dictionary = count_words(total_string)
#--------------------------------------------------------------------------------------------
    
    # Call the functions dico_IDF and mat_TF_IDF
    IDF = dico_IDF(total_dictionary, dictionary_of_files)
    mat = mat_TF_IDF(total_dictionary, dictionary_of_files, IDF)
    
    # Call the function less_important_words
    list_less_imp = less_important_words(total_dictionary, mat)
    print(list_less_imp)

    #Call the function higher_TF_IDF
    biggest_score_TF_IDF = higher_TF_IDF(total_dictionary, mat)
    print(biggest_score_TF_IDF)


