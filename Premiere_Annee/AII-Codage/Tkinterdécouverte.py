from tkinter import *
from tkinter import font


# création fenetre colorée
fenetre = Tk()
fenetre.title("Exemple 1")
fenetre.geometry("1800x800")
fenetre.configure(bg="deepskyblue3")


# placement d'une étiquette (label)

texte1 = Label(fenetre, text="Exemple de texte")
texte1.place (x=50, y=50)

my_font1 = font.Font(fenetre, ("comic sans ms", 18, "bold italic"))
my_font2 = font.Font(fenetre, ("calibri", 14))

texte2 = Label(fenetre, text="Exemple de font 1", font=my_font1)
texte2.place (x=50, y=150)

texte3 = Label(fenetre, text="Exemple de font 2", font=my_font2)
texte3.place (x=250, y=250)

fen1 = Canvas(fenetre, width=250, height=150, bg="ivory",relief="ridge",borderwidth="8")
fen1.place(x=1, y=200)

# Ici, l'étiquette de texte se fait dans la fenetre nouvellement créée
texte4 = Label(fen1, text="autre texte", font=my_font2)
texte4.place (x=50, y=50)

# Mise en place boutons

def action():
    a=1
Test = Button(fen1, text="Tester", command=action(),font=my_font2,relief="raised",borderwidth="8")
Test.place(height=45, width=100,x=20, y=80)

saisienom=Entry(fenetre,font=my_font1,bg="aquamarine1",fg="goldenrod")
saisienom.place(x=50,y=50)


def affichernom():
    contenu=saisienom.get()
    texte5 = Label(fenetre, text="Votre prénom est : "+contenu,font=my_font2)
    texte5.place (x=50, y=700)

informer = Button(fenetre, text="Quel est votre prénom ?", command=affichernom,font=my_font2,relief="raised",borderwidth="8")
informer.place(height=45, width=200, x=50, y=500)


def effacer():
    saisienom.delete(0,END)

effacer = Button(fenetre, text="Effacer la zone", command=effacer,font=my_font2,relief="raised",borderwidth="8")
effacer.place(height=45, width=200,x=50, y=550)


coche1 = BooleanVar()
coche1.set(True)
coche2 = BooleanVar()
coche2.set(False)

caseacocher1 = Checkbutton(fenetre, text="Case 1", var=coche1)
caseacocher2 = Checkbutton(fenetre, text="Case 2", var=coche2)

caseacocher1.place(x=50, y=600)
caseacocher2.place(x=50, y=620)

def fairebilan():

    message="La premiere case est: "
    if coche1.get==1:
        message=message+" cochée"
    else:
        message=message+" décochée"
    message="La deuxieme case est: "
    if coche2.get==1:
        message=message+" cochée"
    else:
        message=message+" décochée"
    
    texte6 = Label(fenetre, text=message,font=my_font2)
    texte6.place(x=350, y=710)

bilan = Button(fenetre, text="Bilan des cases à cocher", command=fairebilan,font=my_font2,relief="raised",borderwidth="8")
bilan.place(height=45, width=300, x=50, y=700)

fenetre.mainloop()