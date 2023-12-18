# My first Chatbot


## Authors

* Ariel WANTOU - [@Savratis56](https://github.com/Savratis56)
* Aube RAMASSAMY - [@auberamas](https://github.com/auberamas)
 
[***➜ Link of our project : pychatbot-wantou-ramassamy-int3***](https://github.com/auberamas/pychatbot-wantou-ramassamy-int3)

## Description of the project

We work on a corpus of speeches by French presidents.
The program give the list of the presidents from the corpus, by default.

### Programs
- main.py
- function.py
- clean_files.py

### Functionalities 
- Features : you can choose one feature between the following

1. Least important(s) words of the corpus 
2. Most important(s) words of the corpus 
3. The most repeated word by Chirac 
4. Who spoke about 'nation' and who repeated it the most 
5. Who spoke about 'climate' or 'ecology' for the first time 
6. Words that all presidents said 

- Ask a question: you can ask a question and the Chatbot will give you an answer.

### Instructions to execute the code

#### Executing clean_files
First execute "clean_file" to clean all texts (saved in "spechees") from punctuation. 
Those cleaned files are saved in a new directory named "cleaned".

#### Executing the main
Then execute the main.
When you execute the program, the menu of all the features and the available actions are displayed.
You can choose to : 
* Execute a feature : input 1, then enter the integer linked to chosen feature : a number between 1 and 6
* Ask a question : input 2, then asks your question

Then the program ask you if you want to execute another action : 
* Input the integer 0 to stop the program
* Input the integer 1 to continue : the menu and the choice of actions is displayed again, you can enter your feature choice as the beginning
