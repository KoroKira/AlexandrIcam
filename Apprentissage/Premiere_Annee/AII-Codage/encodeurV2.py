import decimal
from tkinter import *
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt

# création fenetre colorée
fenetre = Tk()
fenetre.title("Encodeur")
fenetre.geometry("1800x800")
fenetre.configure(bg="deepskyblue3")

# définition de la font de tout
my_font1 = font.Font(fenetre, ("comic sans ms", 18, "bold italic"))
my_font2 = font.Font(fenetre, ("calibri", 14))

# création zone de texte où l'utilisateur entrera quelque chose à encoder 

saisie_texte_encoder=Entry(fenetre,font=my_font1,bg="grey89",fg="black")
saisie_texte_encoder.place(x=50,y=50)



def bin_to_dec(binary):
    dec = 0
    power = len(binary) - 1
    for digit in binary:
        dec += int(digit) * 2**power
        power -= 1
    return dec
    texte1 = Label(fenetre, text="Le binaire donné converti en base 10 donne : "+str(dec),font=my_font2)
    texte1.place (x=50, y=700)

dec=int(input()) 

base10 = Button(fenetre, text="Convertir en Base 10", command=bin_to_dec,font=my_font2,relief="raised",borderwidth="8")
base10.place(height=45, width=200, x=50, y=500)



fenetre.mainloop()
