# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:33:02 2023

Name of the Project : My first chatbot

@author: Ariel WANTOU, Aube RAMASSAMY

role of the file : main file
"""
from functions_new import *
    
# Call of the function list_of_files
directory = "./cleaned"
files_names = list_of_files(directory, "txt")

if __name__ == '__main__':

    # Call the function display, list_of_names and list_of_files
    display(list_of_names(list_of_files(directory, "txt")), message1="President's name of the corpus: \n", message2="-" * 60)

    menu = ["1- Least important word(s) of the corpus",
            "2- Most important word(s) of the corpus",
            "3- The most repeated word by Chirac",
            "4- Who spoke about 'nation' and who repeated it the most",
            "5- Who spoke about 'climate' or 'ecology' for the first time",
            "6- Words that all presidents said"]

    actions =[" 1- To choose an action from the menu",
              " 2- To ask a question"]

    # Call the function display twice to show the menu and the available actions
    display(menu,message1="Menu of features: \n", message2="-"*60)
    display(actions, message1="Available actions:\n")


    launch = 1
    while launch == 1:
        # Ask the user to choose what he wants to do
        play(launch, directory)
        try:
            launch = int(input("Enter 1 to continue, 0 to stop : "))
        except:
            print("Enter somthing else")
