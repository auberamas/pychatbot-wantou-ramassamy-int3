from customtkinter import *

window = CTk()

window.geometry('350x200')
colors = {"blue": "#48dbfb", "aqua": "#01a3a4", "apple": "#ea8685",
          "creamy": "#f3a683", "pink": "#f8a5c2", "grey": "#c8d6e5",
          "biscay": "#303952"}

button = CTkButton(window, text="Click here !", width = 200)
button.pack()
window.mainloop()
