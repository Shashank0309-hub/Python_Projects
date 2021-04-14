from tkinter import *
from PIL import Image,ImageTk
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Dice Simulator')

Blankline = Label(root,text = '')
Blankline.pack()

dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = Label(root, image = DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack(expand = True)

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image = DiceImage)
    ImageLabel.image = DiceImage

button = Button(root, text = 'Roll the Dice', fg = 'Blue', command = rolling_dice)
button.pack(expand = True)



root.mainloop()