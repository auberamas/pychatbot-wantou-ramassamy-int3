from tkinter import *

# Colors
colors = {"blue": "#48dbfb", "aqua": "#01a3a4", "apple": "#ea8685",
          "creamy": "#f3a683", "pink": "#f8a5c2", "grey": "#c8d6e5",
          "biscay": "#303952"}

# Config
window = Tk()
window.title("Chatbot")
window.geometry("600x600+50+10")
window.resizable(width=False, height=False)
window.iconbitmap("Image/star.ico")
window.config(bg=colors["biscay"])

head = Label(window, width=100, height=5, text="MENU", font=('Arial', 20, "bold"),
             bg=colors['biscay'], fg=colors['pink'])

def test():
    text["text"] = "How are you ?"

text = Label(window, text="Hello")

button = Button(window, width=50, height=1, text="Click me !", font=('Arial', 12),
                    bg=colors['aqua'], activebackground=colors['biscay'], activeforeground=colors['grey'],
                    relief=RIDGE,
                    borderwidth=6,
                    command=test
                    )

# Display texts
head.pack()
text.pack()

# Display button
button.pack()

window.mainloop()
