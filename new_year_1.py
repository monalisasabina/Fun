import tkinter as tk, random
#Tkinter: Python built in library for creating graphical interface

messages = [
    "🌟 Happy New Year 2026  🌟\nWishing you joy and success!",
    "🎆 New beginnings, new dreams!",
    "🌟 May your year shine bright!"
]

#Create the main window
r=tk.Tk()                  #creating main application window
r.title("Greeting Card")   #sets the window title
r.geometry("350x450")      #defines width and height
r.configure(bg="#111")     #background colour

# Creating the label card with a random message
card=tk.Label(
    r,
    text=random.choice(messages),     #picks one message at a time
    font=("Arial",20),
    fg="white",                       #white text
    bg="#222",                        #grey background
    wraplength=250,                   #wraps lines at 250px
    justify="center"
    )

card.pack(expand=True,padx=20,pady=40)      #places the label with padding

# Function to change the label text
def change():
    card.config(text=random.choice(messages))

# Creating a button that triggers the change function
tk.Button(r,text="New Wish", command=change).pack(pady=10)

# Starting the Tkinter event loop
r.mainloop()
