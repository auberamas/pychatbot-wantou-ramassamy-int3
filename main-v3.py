# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:33:02 2023

@author: Ariel WANTOU, Aube RAMASSAMY
"""
from functions import *
from customtkinter import *
import PIL
    
# Call of the function list_of_files
directory = "./speeches"
files_names = list_of_files(directory, "txt")

if __name__ == '__main__':

    # Call of the function name_of_presidents
    presidents_name = name_of_presidents(files_names) # Return a list of president's name

    # Create a list of full names with the concatenation of first name and name
    presidents_first_name = ["Jacques", "Valéry", "François", "Emmanuel", "François", "Nicolas"]
    presidents_full_name = [presidents_first_name [i] + " " + presidents_name[i] for i in range(len(presidents_first_name ))]

    print("-" * 40)
    print("President's name of the corpus: ")
    # Call the function display_full_name to display president name
    display(presidents_full_name)
    print("-" * 40)
    print()

    # Call the function fill_dico to create a dictionary as : { 'name of file' : 'president full name'}
    dico_presidents = fill_dico(presidents_full_name, files_names, presidents_name)
    date_president = {"Valéry Giscard d'Estaing": 1974, "François Mitterrand": 1981,
                      "Jacques Chirac": 1995, "Nicolas Sarkozy": 2007, "François Hollande": 2012,
                      "Emmanuel Macron": 2017}

# ----Creation of dictionaries---------------------------------------------------------------------

    directory = "./cleaned"
    dictionary_of_files, total_dictionary = dict(), dict() 
    total_string = str()
    
    # Creation of a dictionary of the occurrence of words for each file saved in dictionary_of_files
    # Open each file of the directory
    for file in files_names :
        dico_of_file, string_of_file = {}, str()  # Start with empty dico and string for each file
        with open(directory + "/" + file , "r", encoding = 'utf-8') as opened_file:
            for line in opened_file : # Run over line of the file
                # Word run over a list of words from a line of the file without the '\n'
                for word in (line.strip()).split(' ') : 
                    # Create a string of all words in a file
                    string_of_file = string_of_file + " " + word

        # Call the function count_words which returns a dico as : {"word" : occurrence} for each file
        dico_of_file = count_words(string_of_file)
        # Fill the dico dictionary_of_files as : {"file name" : dico of the file }
        dictionary_of_files[file] = dico_of_file

        # Create a string which is the concatenation of the string of all the corpus
        total_string += string_of_file
    
    # Creation of a dictionary of words occurrence for the corpus
    # Call the function count_words
    total_dictionary = count_words(total_string)

    # Create a list with keys(words) of total_dictionary : it's the list of words of all the corpus
    all_words = []
    for key in total_dictionary.keys():
        all_words.append(key)
    all_words.sort()
    
# ----Creation of the TF-IDF matrix ------------------------------------------------------------
    
    # Call the functions dico_IDF
    IDF = dico_IDF(all_words, dictionary_of_files)
    # Call the functions mat_TF_IDF
    mat = mat_TF_IDF(all_words, dictionary_of_files, IDF)

# ----Features---------------------------------------------------------------------------------

    menu = ["Least important word(s) of the corpus",
            "Most important word(s) of the corpus",
            "The most repeated word by Chirac",
            "Who spoke about 'nation' and who repeated it the most",
            "Who spoke about 'climate' or 'ecology' for the first time",
            "Words that all presidents said"]

# ----Interface------------------------------------------------------------------------------------
    # Colors
    colors = {"blue": "#48dbfb", "aqua": "#01a3a4", "apple": "#ea8685",
              "creamy": "#f3a683", "pink": "#f8a5c2", "grey": "#c8d6e5",
              "biscay": "#303952"}

    # Config
    window = CTk()
    window.title("Chatbot")
    window.geometry("600x600+50+10")
    window.resizable(width=False, height=False)
    window.iconbitmap("Image/star.ico")
    set_appearance_mode("dark")


    head = CTkLabel(window, width=100, height=20, text= "MENU",font=('Arial', 30, "bold"),
        text_color=colors['pink'], fg_color="transparent" )
    head.place(relx=0.5, rely=0.1, anchor=CENTER)

    message = CTkLabel(window, width=100, height=20, text="What do you whant to know ?", font=('Arial', 16),
                    text_color="white", fg_color="transparent")
    message.place(relx=0.5, rely=0.2, anchor=CENTER)

    #Button
    button1 = CTkButton(window, width=380, text= menu[0],font=('Arial', 14),
        border_width = 2, border_color= colors['pink'],border_spacing = 3,
        fg_color=colors['apple'], hover_color=colors['creamy'], corner_radius= 10,
        command=lambda: display(lowest_score_TF_IDF, ", ", "Least important word(s) in the corpus: "),
    )
    button1.place(relx=0.5, rely=0.45, anchor=CENTER)

    button2 = CTkButton(window, width=380, text=menu[1], font=('Arial', 14),
        fg_color=colors['apple'], hover_color=colors['creamy'], corner_radius= 10,
        command=lambda: display(biggest_score_TF_IDF, ", ", "Most important word(s) in the corpus: ")
        )
    button2.place(relx=0.5, rely=0.52, anchor=CENTER)

    button3 = CTkButton(window, width=380, text=menu[2], font=('Arial', 14),
        fg_color=colors['apple'], hover_color=colors['creamy'], corner_radius= 10,
        command=lambda: display(frequent_words, ", ", "Most repeated word(s) by President Chirac: ")
        )
    button3.place(relx=0.5, rely=0.59, anchor=CENTER)

    button4 = CTkButton(window, width=380, text=menu[3], font=('Arial', 14),
        fg_color=colors['apple'], hover_color=colors['creamy'], corner_radius= 10,
        command=lambda: display(nation_repeated, ", ", "The word 'nation' is repeated by: ",nation_repeated_most)
        )
    button4.place(relx=0.5, rely=0.66, anchor=CENTER)

    button5 = CTkButton(window, width=380, text=menu[4], font=('Arial', 14),
        fg_color=colors['apple'], hover_color=colors['creamy'], corner_radius= 10,
        command=lambda: display([], "","", climat_oldest)
        )
    button5.place(relx=0.5, rely=0.73, anchor=CENTER)

    button6 = CTkButton(window, width=380, text=menu[5], font=('Arial', 14),
        fg_color=colors['apple'], hover_color=colors['creamy'], corner_radius= 10,
        command=lambda: display(common_words, ", ", "The common words to all presidents are: ")
        )
    button6.place(relx=0.5, rely=0.80, anchor=CENTER)

# --- Choice1 ---------------------------------------------------------------------------------------
    # Looking for the less important words (lowest TD-IDF score)
    min_vector = sum(min(mat))  # Calculate the sum of the lowest vector's values in the TF-IDF matrix

    # Call the function vector_research to search all the vectors equal to the lowest one
    lowest_score_TF_IDF = vector_research(all_words, total_dictionary, mat, min_vector)

# --- Choice2 --------------------------------------------------------------------------------------
    # Looking for the most important words (highest TD-IDF score)
    max_vector = sum(max(mat))  # Calculate the sum of the highest vector's values in the TF-IDF matrix

    # Call the function vector_research to search all the vectors equal to the highest one
    biggest_score_TF_IDF = vector_research(all_words, total_dictionary, mat, max_vector)

# --- Choice3 --------------------------------------------------------------------------------------
    # Look for the most frequent word of a president
    name = 'Chirac'
    # Call the function frequent_word_for_a_president : display the most repeated word(s) by a President
    frequent_words = frequent_word_for_a_president(name, dictionary_of_files)

# --- Choice4 ---------------------------------------------------------------------------------------
    # Look for who said "nation" and who repeated it the most
    word = 'nation'
    # Call the function term_research
    repeated = term_research(word, dictionary_of_files, dico_presidents)
    nation_repeated= []
    for key in repeated.keys():
        nation_repeated.append(key)

    # Look for who repeated 'nation' the most
    max_word = max(repeated.values()) # keep the occurrence of the most repeated word
    for name in repeated:
        if repeated[name] == max_word:
            president = name
    nation_repeated_most = president + " is the one who repeated "+word + " the most."

# --- Choice5 ---------------------------------------------------------------------------------------
    # Look for who said "climat" or "écologie" and who repeated it the most
    word1 = 'climat'
    word2 = 'écologie'

    # Call the function term_research for word1 and word2
    # Return a dico as : {president : occurrence of the word}
    repeated1 = term_research(word1, dictionary_of_files, dico_presidents)
    repeated2 = term_research(word2, dictionary_of_files, dico_presidents)

    # Comparing the values of date_president for names in repeated to know who is the oldest
    repeated = repeated1 | repeated2
    oldest = 2023
    for name in repeated.keys():
        if date_president[name] < oldest:
            name_oldest = name
            oldest = date_president[name]
    climat_oldest = name_oldest+ " is the first president to talk about "+ "'climat' or 'écologie'."

# --- Choice6 --------------------------------------------------------------------------------------
    # Look for the words said by all presidents
    common_words = []
    word_occurrence = dict()

    for word in all_words:
        # Call the function term_research : give the presidents who said the word and how much
        word_occurrence = term_research(word, dictionary_of_files, dico_presidents)

        # Verify if all presidents are in word_occurrence
        if len(word_occurrence) == len(presidents_full_name):
            common_words.append(word)

    window.mainloop()