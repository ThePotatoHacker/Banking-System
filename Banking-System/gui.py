# All visual elements using Tkinter/PyQt:
#   - Welcome screen with kawaii ASCII art
#   - Login window (account # + PIN fields)
#   - User dashboard (balance, buttons for actions)
#   - Admin control panel
#   - Avatar selection popup
#   - Transaction confirmation dialogs

# Import time to pause program
import time
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk

# tkinter is pythons built in library for creating windows and bttons
# importing fonts will allow me to use cutom fonts ----> I want to use Chewy
# PIL will allow me to add images ----> I want to add the bee logo

# Front Page

def front_page():
    window =tk.Tk() # This should create the main window
    window.title("Honeybee Bank") # Will set the window title
    window.geometry("400x300") # My width and height
    window.configure(bg="#fdffb6") # Should make the backrgound pastel yellow

    # try and except will try to load the bee.png, however if it fails it will load a bee emoji instead

    try: 
        bee_img = Image.open("bee.png")
        bee_img = bee_img.resize((90, 100))
        bee_photo = ImageTk. PhotoImage(bee_img) #Converting image for Tkinter
        bee_label = tk.Label(window, image=bee_photo, bg="#fdffb6") 
        bee_label.image = bee_photo
        bee_label.place(x=150, y=20)
    except:
        print("Bee image not found!")
        tk.Label(window, text="🐝", font=("Arial", 40), bg="#fdffb6").place(x=180, y=30)

        # Getting the Chewy font
    try: 
        chewy_font = tkfont.Font(family = "Chewy" , size=16)
    except: 
        chewy_font = ("Arial" , 16)
    
    window.mainloop()  # open window 



#Check in Terminal if loaded
print("✅ gui.py loaded")

