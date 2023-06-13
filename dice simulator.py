import tkinter as tk
from PIL import Image, ImageTk
import random

window=tk.Tk()
window.geometry("1200x1000")
window.title("Dice simulator")

dice=["dice.png","dice (1).png","dice (2).png","dice (3).png","dice (4).png","dice (5).png"]

image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)

label1.image=image1
label2.image=image2

label1.place(x=50,y=100)
label2.place(x=650,y=100)

def roll_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1
    
    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2
    
button= tk.Button(window,text="ROLL DICE",bg="white",fg="red",font="Times 20 bold",command=roll_dice())
button.pack()

window.mainloop()