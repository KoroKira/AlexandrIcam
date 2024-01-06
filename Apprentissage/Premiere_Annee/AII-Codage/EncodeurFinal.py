#Importation des librairies

# import matplotlib
# import numpy
import tkinter

#Création de la fenêtre
fenetre = tkinter.Tk()
fenetre.title("Encodeur")
fenetre.geometry("400x1000")

#Création des éléments d'interface utilisateur
text_frame = tkinter.Frame(fenetre)
text_frame.pack()

input_text = tkinter.Entry(text_frame)
input_text.pack()

#Création de la TextBox
result_text = tkinter.Text(text_frame)
result_text.pack()

def encode_binaire_base10():
    binaire = input_text.get()
    base10 = int(binaire, 2)
    result_text.delete('1.0', tkinter.END)
    result_text.insert(tkinter.END, base10)

def encode_binaire_hexadecimal():
    binaire = input_text.get()
    hexadecimal = hex(int(binaire, 2))
    result_text.delete('1.0', tkinter.END)
    result_text.insert(tkinter.END, hexadecimal)


#Création des modules supplémentaires
def encode_hexadecimal_base10():
    hexadecimal = input_text.get()
    base10 = int(hexadecimal, 16)
    result_text.delete('1.0', tkinter.END)
    result_text.insert(tkinter.END, base10)

def encode_hexadecimal_binaire():
    hexadecimal = input_text.get()
    binaire = bin(int(hexadecimal, 16))
    result_text.delete('1.0', tkinter.END)
    result_text.insert(tkinter.END, binaire)

def encode_base10_binaire():
    base10 = int(input_text.get())
    binaire = bin(base10)
    result_text.delete('1.0', tkinter.END)
    result_text.insert(tkinter.END, binaire)

def encode_base10_hexadecimal():
    base10 = int(input_text.get())
    hexadecimal = hex(base10)
    result_text.delete('1.0', tkinter.END)
    result_text.insert(tkinter.END, hexadecimal)

#Création des boutons de codage

convert_hex10 = tkinter.Button(text_frame, text="Hexadecimal à Base 10", command=encode_hexadecimal_base10)
convert_hex10.pack()

convert_hexbin = tkinter.Button(text_frame, text="Hexadecimal à Binaire", command=encode_hexadecimal_binaire)
convert_hexbin.pack()

convert_10bin = tkinter.Button(text_frame, text="Base 10 à Binaire", command=encode_base10_binaire)
convert_10bin.pack()

convert_10hex = tkinter.Button(text_frame, text="Base 10 à Hexadecimal", command=encode_base10_hexadecimal)
convert_10hex.pack()

convert_bin10 = tkinter.Button(text_frame, text="Binaire à Base 10", command=encode_binaire_base10)
convert_bin10.pack()

convert_binhex = tkinter.Button(text_frame, text="Binaire à Hexadécimal", command=encode_binaire_hexadecimal)
convert_binhex.pack()

fenetre.mainloop()