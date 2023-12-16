# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:33:02 2023

Name of the Project : My first chatbot
@author: Ariel WANTOU, Aube RAMASSAMY

role of the file :
- The file display the list of presidents names of the corpus
- Display the menu and the available actions and ask the user to choose between them
"""

from functions_new import *

directory = "./cleaned"
first_directory = "./speeches"
# Call of the function list_of_files
files_names = list_of_files(directory, "txt")

if __name__ == '__main__':

    # Call the function display, list_of_names and list_of_files to display the list of presidents
    display(list_of_names(list_of_files(directory, "txt")), message1="President's name of the corpus: \n")

# --- Available choices for the user ---------------------------------------------------------------

    menu = ["1- Least important word(s) of the corpus",
            "2- Most important word(s) of the corpus",
            "3- The most repeated word(s) by Chirac",
            "4- Who spoke about 'nation' and who repeated it the most",
            "5- Who spoke about 'climate' or 'ecology' for the first time",
            "6- Words that all presidents said"]

    actions = [" 1- To choose an action from the menu",
               " 2- To ask a question"]

# --- Launch the program ------------------------------------------------------------------------

    launch, stop = 1, -1
    while launch == 1:
        # Call the function display twice to show the menu and the available actions
        display(menu, message1="-" * 60+"\n" + "Menu of features: \n", message2="-" * 60)
        display(actions, message1="Available actions:\n")

        # Call the function play to ask the user to choose what he wants to do
        play(directory, first_directory)
        stop = -1
        while stop != 0 and stop != 1:
            try:
                stop = int(input("Enter 1 to continue, 0 to stop : "))
            except:
                # Displayed if there is an error with the input
                print("You must enter 0 or 1.")
        launch = stop