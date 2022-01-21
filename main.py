import tkinter as tk
import os
import random

# --- functions ---
directory = r'pngcards/'
Deck = []
for card in os.listdir(directory):
    if card.endswith('.png'):
        Deck.append(directory+str(card))
Decksize = len(Deck)-1

class Deal:
    def __init__(self):
        self.Newcards()

    def Newcards(self):
        image1 = tk.PhotoImage(file=Deck[random.randint(0, Decksize)])
        topcard = tk.Button(root, image=image1)
        topcard.bind('<Button-1>', self.Usedcard)
        image = tk.PhotoImage(file=Deck[random.randint(0, Decksize)])
        bottomcard = tk.Button(root, image=image)
        bottomcard.bind('<Button-1>', self.Usedcard)
        topcard.pack(side='left')
        bottomcard.pack(side='right')
        root.mainloop()

    def Usedcard(self, event):
        btn= event.widget
        image = tk.PhotoImage(file=directory + 'astronaut.png')
        btn.config(image = image)
        root.mainloop()

root = tk.Tk()
gui= Deal()

