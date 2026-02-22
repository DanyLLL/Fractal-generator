#Programme réalisé par LIM Dany

########################################################################################################################

#Création de la fenêtre

from tkinter import*
from math import*
fenetre=Tk()
Canevas=Canvas(fenetre,width=650,height=620,bg='#00D5FB')
Canevas.place(x=25,y=55)
fenetre.config(width=700, height=750, bg="#0063C4")

########################################################################################################################

#Création des class :

class Pile:
    def __init__(self):
        self.valeurs=[]
    def est_vide(self):
        return self.valeurs==[]
    def empile(self,valeur):
        self.valeurs.append(valeur)
    def depile(self):
        if self.valeurs:
            return self.valeurs.pop()
    def __str__(self):
        ch= ''
        for x in self.valeurs:
            ch = "|"+ str(x)+"|"+"\n"+ch
        return ch + "---\n"

class File:
    def __init__(self):
        self.valeurs=[]
    def enfile(self,valeur):
        self.valeurs.append(valeur)
    def defile(self):
        if self.valeurs:
            return self.valeurs.pop(0)
    def est_vide(self):
        return self.valeurs==[]
    def longueur(self):
        return len(self.valeurs)
    def __str__(self):
        ch=""
        for x in self.valeurs:
            ch=ch+" <- "+str(x)
        return ch

class coord:
     def __init__(self,i,j):
        self.x = i
        self.y = j
     def __add__(self, other):
        return coord(self.x+ other.x, self.y+other.y)
     def __sub__(self, other):
        return coord(self.x - other.x, self.y - other.y)
     def __mul__(self, other:int):
        return coord( self.x * other, self.y * other)
     def __eq__(self, other):
        return self.x == other.x and self.y == other.y
     def __str__(self):
        return "( "+str(self.x)+" ; "+str(self.y)+" )"
class crayon:
     def __init__(self, xx, yy, couleur ):
         self.pos = coord(xx , yy )
         self.couleur = couleur
         self.ang = 0
         self.dir = coord(1,0)
     def tourne(self, angle):
         self.ang = self.ang + angle
         self.dir = coord(cos((self.ang/180)*pi), sin((self.ang/180)*pi))
     def avance(self,distance):
         p = self.pos
         self.pos = self.pos + self.dir * distance
         return Canevas.create_line(p.x,p.y,self.pos.x,self.pos.y,fill=self.couleur)

########################################################################################################################

def retour():
    "retour permet le retour à la page d'accueil avec les 3 différents modes de génération"
    #Fontion associée au bouton "Retour"
    #On place_forget et place tous les boutons/textes qui permettent le retour à la page d'accueil
    Canevas.delete('all')
    Canevas.config(width=650,height=620)
    Canevas.place(x=25,y=55)
    texte_fractales.place(x=52,y=30)
    bouton_koch_recursif.place_forget()
    bouton_menger_recursif.place_forget()
    bouton_sierpinski_recursif.place_forget()
    bouton_hilbert_l_sys.place_forget()
    bouton_koch_l_sys.place_forget()
    bouton_gosper_l_sys.place_forget()
    bouton_dragon_pliage.place_forget()
    bouton_dragon_rainbow_pliage.place_forget()
    bouton_fractale_personnalisee_l_sys.place_forget()
    bouton_valider.place_forget()
    texte_nbr_iterations.place_forget()
    texte_fractales_personnalisees.place_forget()
    entree_nbr_iterations.place_forget()
    entree_fractales_personnalisees_A.place_forget()
    entree_fractales_personnalisees_B.place_forget()
    entree_fractales_personnalisees_G.place_forget()
    entree_fractales_personnalisees_D.place_forget()
    entree_fractales_personnalisees_A_avance.place_forget()
    entree_fractales_personnalisees_B_avance.place_forget()
    entree_fractales_personnalisees_G_tourne.place_forget()
    entree_fractales_personnalisees_D_tourne.place_forget()
    entree_fractales_personnalisees_mot.place_forget()
    texte_fractales_personnalisees_A.place_forget()
    texte_fractales_personnalisees_B.place_forget()
    texte_fractales_personnalisees_G.place_forget()
    texte_fractales_personnalisees_D.place_forget()
    texte_fractales_personnalisees_A_avance.place_forget()
    texte_fractales_personnalisees_B_avance.place_forget()
    texte_fractales_personnalisees_G_tourne.place_forget()
    texte_fractales_personnalisees_D_tourne.place_forget()
    texte_fractales_personnalisees_mot.place_forget()
    bouton_choix_fractales_recursif.place(x=110,y=160)
    bouton_choix_fractales_l_sys.place(x=110,y=340)
    bouton_choix_fractales_pliage.place(x=110,y=520)
    bouton_retour.place_forget()

########################################################################################################################

#Création de toutes les fonctions qui concercent le récursif

def choix_generation_recursif():
    "choix_generation_recursif permet d'afficher à l'utilisateur l'interface pour les figures récursives proposées"
    #Fonction associée au bouton "Génération en récursif"
    bouton_choix_fractales_recursif.place_forget()
    bouton_choix_fractales_l_sys.place_forget()
    bouton_choix_fractales_pliage.place_forget()
    bouton_sierpinski_recursif.place(x=110,y=160)
    bouton_koch_recursif.place(x=110,y=340)
    bouton_menger_recursif.place(x=110,y=520)
    bouton_retour.place(x=220,y=640)

def choix_nbr_iterations_sierpinski_recursif():
    "choix_nbr_iterations_sierpinski_recursif permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités du triangle Sierpinski en récursif"
    #Fontion associée au bouton "Triangle de Sierpinski" dans la section récursif
    bouton_koch_recursif.place_forget()
    bouton_menger_recursif.place_forget()
    bouton_sierpinski_recursif.place_forget()
    texte_nbr_iterations.place(x=70,y=170)
    entree_nbr_iterations.place(x=160,y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de Sierpinski
    bouton_valider.config(command=valider_sierpinski_recursif)
    bouton_valider.place(x=270,y=320)

def valider_sierpinski_recursif():
    "valider_sierpinski_recursif permet de valider la génération du triangle de Sierpinski en récursif avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700,height=665)
    Canevas.place(x=0,y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    #Dans le triangle A,B,C, B est donc le sommet ici
    A, B, C = {'x': 25, 'y': 490}, {'x': 350, 'y': 25}, {'x': 675, 'y': 490}
    Sierpinski(A,B,C,n)

def Sierpinski(A,B,C,n):
    "Sierpinski permet de créer un triangle de Sierpinski de points A,B,C et de sommet B"
    if n==0:
        Canevas.create_polygon(A["x"],A["y"],B["x"],B["y"],C["x"],C["y"],fill='red')
    else:
        A1 = { 'x': (C['x']+B['x'])//2, 'y': (C['y']+B['y']) //2 }
        B1 = { 'x': (C['x']+A['x'])//2, 'y': (C['y']+A['y']) //2 }
        C1 = { 'x': (A['x']+B['x'])//2, 'y': (A['y']+B['y']) //2 }
        Sierpinski(A,B1,C1,n-1)
        Sierpinski(A1,B,C1,n-1)
        Sierpinski(A1,B1,C,n-1)


def choix_nbr_iterations_koch_recursif():
    "choix_nbr_iterations_koch_recursif permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités du flocon de Koch en récursif"
    #Fontion associée au bouton "Flocon de Koch" dans la section récursif
    bouton_koch_recursif.place_forget()
    bouton_menger_recursif.place_forget()
    bouton_sierpinski_recursif.place_forget()
    texte_nbr_iterations.place(x=70,y=170)
    entree_nbr_iterations.place(x=160,y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de Koch
    bouton_valider.config(command=valider_koch_recursif)
    bouton_valider.place(x=270,y=320)

def valider_koch_recursif():
    "valider_koch_recursif permet de valider la génération du flocon de Koch en récursif avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    # Dans le triangle A1,A2,A3, A2 est donc le sommet ici
    A1, A2, A3 = {'x': 25, 'y': 490}, {'x': 350, 'y': 25}, {'x': 675, 'y': 490}
    Koch(A1,A2,A3,n)

def Segment(A1,A2,n):
    "Segment permet de créer les segments du flocon de Koch de points A1,A2,A3 et de sommet A2"
    if n==0:
        Canevas.create_line(A1["x"],A1["y"],A2["x"],A2["y"],fill="yellow",width=3)
    else:
        x,y=A2["x"]-A1["x"],A2["y"]-A1["y"]
        A4 = { "x" : A1["x"] + x//3, "y" : A1["y"]+ y//3}
        A5 = { "x" : A1["x"] + 2 * x // 3, "y" : A1["y"] + 2 * y //3}
        A3 = { "x" : A4["x"] + int(((cos(pi/3) * x - sin(pi/3) * y))/3), "y" : A4["y"] + int(((sin(pi/3) * x + cos(pi/3) * y))/3)}
        Segment(A1,A4,n-1)
        Segment(A4,A3,n-1)
        Segment(A3,A5,n-1)
        Segment(A5,A2,n-1)

def Koch(A1,A2,A3,n):
    "Koch permet de créer les 3 segments, formant (à n=0) un triangle,selon les n itérations avec A1,A2 et A3 dont A2 est le sommet du triangle"
    Segment(A2, A1, n)
    Segment(A1, A3, n)
    Segment(A3, A2, n)


def choix_nbr_iterations_meger_recursif():
    "choix_nbr_iterations_meger_recursif permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités de l'éponge de Meger en récursif"
    #Fontion associée au bouton "Eponge de Meger" dans la section récursif
    bouton_koch_recursif.place_forget()
    bouton_menger_recursif.place_forget()
    bouton_sierpinski_recursif.place_forget()
    texte_nbr_iterations.place(x=70, y=170)
    entree_nbr_iterations.place(x=160, y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de Meger
    bouton_valider.config(command=valider_meger_recursif)
    bouton_valider.place(x=270, y=320)

def valider_meger_recursif():
    "valider_koch_recursif permet de valider la génération de l'éponge de Meger en récursif avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    A = {'x': 58, 'y': 30}
    Eponge(A, 580, n)

def Eponge(A,taille,n):
    "Eponge permet de créer une éponge de Meger de taille ici égale à 580, avec n itérations et à une position A(x,y)"
    if n == 0 :
        Canevas.create_rectangle(A['x'],A['y'],A['x']+taille,A['y']+taille,fill='green')
    else :
        taille = taille // 3
        E = {'x': A['x'] , 'y': A['y'] + taille }
        F = {'x': A['x'] + taille , 'y': A['y'] }
        G = {'x': A['x'] + 2* taille , 'y': A['y'] + taille }
        H = {'x': A['x'] + taille , 'y': A['y'] + 2* taille }
        Eponge(E, taille, n - 1)
        Eponge(F, taille, n - 1)
        Eponge(G, taille, n - 1)
        Eponge(H, taille, n - 1)

########################################################################################################################

#Création de toutes les fonctions qui concercent les L-Système

def iter_L_systeme(F1, regle, n):
    "iter_L_systeme renvoie un L-Système basé sur une regle (un dico) à l'aide de F1 (une file) et du nombre d'itérations n souhaitées"
    if n == 0: return F1
    F2 = File()
    while not F1.est_vide():
        alpha = F1.defile()
        for c in regle[alpha]:
            F2.enfile(c)
    return iter_L_systeme(F2, regle, n - 1)


def choix_generation_l_sys():
    "choix_generation_l_sys permet d'afficher à l'utilisateur l'interface pour les figures en L-Système proposées"
    #Fontion associée au bouton "Génération en l-système"
    bouton_choix_fractales_recursif.place_forget()
    bouton_choix_fractales_l_sys.place_forget()
    bouton_choix_fractales_pliage.place_forget()
    bouton_hilbert_l_sys.place(x=110, y=110)
    bouton_koch_l_sys.place(x=110, y=250)
    bouton_gosper_l_sys.place(x=110, y=390)
    bouton_fractale_personnalisee_l_sys.place(x=110, y=530)
    bouton_retour.place(x=220, y=640)


def choix_nbr_iterations_koch_l_sys():
    "choix_nbr_iterations_koch_l_sys permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités du flocon de Koch en L-Système"
    #Fontion associée au bouton "Flocon de Koch" dans la section l-système
    bouton_koch_l_sys.place_forget()
    bouton_gosper_l_sys.place_forget()
    bouton_hilbert_l_sys.place_forget()
    bouton_fractale_personnalisee_l_sys.place_forget()
    texte_nbr_iterations.place(x=70, y=170)
    entree_nbr_iterations.place(x=160, y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de Koch
    bouton_valider.config(command=valider_koch_l_sys)
    bouton_valider.place(x=270, y=320)

def valider_koch_l_sys():
    "valider_koch_l_sys permet de valider la génération du flocon de Koch en L-Système avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    # entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    #Création de la règle de Koch
    regle_koch = {"début": "A", "A": "AGADADAGA", "G": "G", "D": "D"}
    Schema=File()
    #On enfile le début de la règle
    for c in regle_koch['début']:
        Schema.enfile(c)
    chemin_koch = iter_L_systeme(Schema,regle_koch,n)
    MonCrayon = crayon(270,400,"orange")
    #Les conditions ci-dessous permettent de replacer le crayon pour que la figure soit à peu près au centre du cadre
    if n < 5:
        MonCrayon.pos.x = MonCrayon.pos.x - 60
        MonCrayon.pos.y = MonCrayon.pos.y + 80
    elif 7 > n >= 5:
        MonCrayon.pos.x = MonCrayon.pos.x - 240
        MonCrayon.pos.y = MonCrayon.pos.y + 80
    else:
        MonCrayon.pos.x = MonCrayon.pos.x - 240
        MonCrayon.pos.y = MonCrayon.pos.y + 150

    while not chemin_koch.est_vide():
        l = chemin_koch.defile()
        #Les conditions ci-dessous permettent de réduire l'avancée notée x du crayon pour éviter que la figure ne sorte du cadre
        if n < 5:
            if l == "A":
                x = 40 - (12 * (n - 1))
                MonCrayon.avance(x)
            elif l == "D":
                MonCrayon.tourne(90)
            elif l == "G":
                MonCrayon.tourne(-90)
        elif 7 > n >= 5:
            if l == "A":
                x = 40 / (9 * (n - 1))
                MonCrayon.avance(x)
            elif l == "D":
                MonCrayon.tourne(90)
            elif l == "G":
                MonCrayon.tourne(-90)
        else:
            if l == "A":
                x = 40 / (22 * (n - 1))
                MonCrayon.avance(x)
            elif l == "D":
                MonCrayon.tourne(90)
            elif l == "G":
                MonCrayon.tourne(-90)


def choix_nbr_iterations_gosper_l_sys():
    "choix_nbr_iterations_gosper_l_sys permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités de la courbe de Gosper en L-Système"
    # Fontion associée au bouton "Courbe de Gosper" dans la section l-système
    bouton_koch_l_sys.place_forget()
    bouton_gosper_l_sys.place_forget()
    bouton_hilbert_l_sys.place_forget()
    bouton_fractale_personnalisee_l_sys.place_forget()
    texte_nbr_iterations.place(x=70, y=170)
    entree_nbr_iterations.place(x=160, y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de Gosper
    bouton_valider.config(command=valider_gosper_l_sys)
    bouton_valider.place(x=270, y=320)

def valider_gosper_l_sys():
    "valider_gosper_l_sys permet de valider la génération de la courbe de Gosper en L-Système avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    #Création de la règle de Gosper
    regle_gosper = {"début" : "A","A":"ADBDDBGAGGAAGBD","B":"GADBBDDBDAGGAGB","D":"D","G":"G"}
    Schema = File()
    #On enfile le début de la règle
    for c in regle_gosper['début']:
        Schema.enfile(c)
    chemin_gosper = iter_L_systeme(Schema, regle_gosper, n)
    MonCrayon = crayon(500, 90, "white")
    #Les conditions ci-dessous permettent de replacer le crayon pour que la figure soit à peu près au centre du cadre
    if n < 4:
        MonCrayon.pos.x = MonCrayon.pos.x - 120
        MonCrayon.pos.y = MonCrayon.pos.y + 80
    elif 6 > n >= 4:
        MonCrayon.pos.x = MonCrayon.pos.x + 30
        MonCrayon.pos.y = MonCrayon.pos.y + 80
    else:
        MonCrayon.pos.x = MonCrayon.pos.x + 100
        MonCrayon.pos.y = MonCrayon.pos.y + 150
    while not chemin_gosper.est_vide():
        l = chemin_gosper.defile()
        #Les conditions ci-dessous permettent de réduire l'avancée notée x du crayon pour éviter que la figure ne sorte du cadre
        if n < 4:
            if l == "A":
                x = 40 - (10 * (n - 1))
                MonCrayon.avance(x)
            elif l == "B":
                x = 40 - (10 * (n - 1))
                MonCrayon.avance(x)
            elif l == "G":
                MonCrayon.tourne(-60)
            elif l == "D":
                MonCrayon.tourne(60)
        elif 6 > n >= 4:
            if l == "A":
                x = 40 / (4 * (n - 1))
                MonCrayon.avance(x)
            elif l == "B":
                x = 40 / (4 * (n - 1))
                MonCrayon.avance(x)
            elif l == "G":
                MonCrayon.tourne(-60)
            elif l == "D":
                MonCrayon.tourne(60)
        else:
            if l == "A":
                x = 40 / (6 * (n - 1))
                MonCrayon.avance(x)
            if l == "B":
                x = 40 / (6 * (n - 1))
                MonCrayon.avance(x)
            if l == "G":
                MonCrayon.tourne(-60)
            if l == "D":
                MonCrayon.tourne(60)

def choix_nbr_iterations_hilbert_l_sys():
    "choix_nbr_iterations_hilbert_l_sys permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités de la courbe de Hilbert en L-Système"
    #Fontion associée au bouton "Courbe de Hilbert" dans la section l-système
    bouton_koch_l_sys.place_forget()
    bouton_gosper_l_sys.place_forget()
    bouton_hilbert_l_sys.place_forget()
    bouton_fractale_personnalisee_l_sys.place_forget()
    texte_nbr_iterations.place(x=70, y=170)
    entree_nbr_iterations.place(x=160, y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de Gosper
    bouton_valider.config(command=valider_hilbert_l_sys)
    bouton_valider.place(x=270, y=320)

def valider_hilbert_l_sys():
    "valider_hilbert_l_sys permet de valider la génération de la courbe de Hilbert en L-Système avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    #Création de la règle de Hilbert
    regle_hilbert = {"début": "B", "B": "GCADBABDACG", "C": "DBAGCACGABD", "A": "A", "G": "G", "D": "D"}
    Schema = File()
    #On enfile le début de la règle
    for c in regle_hilbert['début']:
        Schema.enfile(c)
    chemin_hilbert = iter_L_systeme(Schema, regle_hilbert, n)
    MonCrayon = crayon(200, 400, "purple")
    #Les conditions ci-dessous permettent de replacer le crayon pour que la figure soit à peu près au centre du cadre
    if n < 5:
        MonCrayon.pos.x = MonCrayon.pos.x - 60
        MonCrayon.pos.y = MonCrayon.pos.y + 80
    elif 7 > n >= 5:
        MonCrayon.pos.x = MonCrayon.pos.x + 30
        MonCrayon.pos.y = MonCrayon.pos.y + 80
    else:
        MonCrayon.pos.x = MonCrayon.pos.x - 120
        MonCrayon.pos.y = MonCrayon.pos.y + 150
    while not chemin_hilbert.est_vide():
        l = chemin_hilbert.defile()
        #Les conditions ci-dessous permettent de réduire l'avancée notée x du crayon pour éviter que la figure ne sorte du cadre
        if n < 5:
            if l == "A":
                x = 40 - (5 * (n - 1))
                MonCrayon.avance(x)
            elif l == "D":
                MonCrayon.tourne(90)
            elif l == "G":
                MonCrayon.tourne(-90)
        elif 7 > n >= 5:
            if l == "A":
                x = 40 - (6.5 * (n - 1))
                MonCrayon.avance(x)
            elif l == "D":
                MonCrayon.tourne(90)
            elif l == "G":
                MonCrayon.tourne(-90)
        else:
            if l == "A":
                x = 40 / (2.7 * (n - 1))
                MonCrayon.avance(x)
            elif l == "D":
                MonCrayon.tourne(90)
            elif l == "G":
                MonCrayon.tourne(-90)

def choix_nbr_iterations_fractale_personnalisee_l_sys():
    "choix_nbr_iterations_fractale_personnalisee_l_sys permet d'afficher à l'utilisateur l'interface pour entrer sa propre règle et le mot initial,son propre"
    "L-Système avec les n itérations souhaitées"
    #Fontion associée au bouton "Fractale personnalisée" dans la section l-système
    #On place_forget et place tous les boutons et toutes les entrées nécessaires
    bouton_koch_l_sys.place_forget()
    bouton_gosper_l_sys.place_forget()
    bouton_hilbert_l_sys.place_forget()
    bouton_fractale_personnalisee_l_sys.place_forget()
    texte_nbr_iterations.place(x=70, y=130)
    entree_nbr_iterations.place(x=160, y=170)
    texte_fractales_personnalisees.place(x= 70,y=250)
    texte_fractales_personnalisees_A.place(x=120,y=310)
    texte_fractales_personnalisees_A_avance.place(x=370, y=310)
    texte_fractales_personnalisees_B.place(x=120, y=370)
    texte_fractales_personnalisees_B_avance.place(x=370, y=370)
    texte_fractales_personnalisees_D.place(x=120,y=430)
    texte_fractales_personnalisees_D_tourne.place(x=370,y=430)
    texte_fractales_personnalisees_G.place(x=120,y=490)
    texte_fractales_personnalisees_G_tourne.place(x=370,y=490)
    texte_fractales_personnalisees_mot.place(x=120, y=550)
    entree_fractales_personnalisees_A.place(x=190,y=310)
    entree_fractales_personnalisees_B.place(x=190,y=370)
    entree_fractales_personnalisees_D.place(x=190,y=430)
    entree_fractales_personnalisees_G.place(x=190,y=490)
    entree_fractales_personnalisees_A_avance.place(x=500,y=310)
    entree_fractales_personnalisees_B_avance.place(x=500,y=370)
    entree_fractales_personnalisees_G_tourne.place(x=500, y=430)
    entree_fractales_personnalisees_D_tourne.place(x=500, y=490)
    entree_fractales_personnalisees_mot.place(x=190,y=550)
    #On change ici la commande de bouton_valider pour la validation de la génération de la fractale personnalisée
    bouton_valider.config(command=valider_fractale_personnalisee_l_sys)
    bouton_valider.place(x=270, y=570)

def valider_fractale_personnalisee_l_sys():
    "valider_fractale_personnalisee_l_sys permet de valider la génération du fractale de l'utlisateur (règle et mot initial) en L-Système avec "
    "le nombre d'itérations n rentrées par l'utilisateur"
    global n
    #On place_forget toute l'interface de création personnalisée
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    texte_fractales_personnalisees_A.place_forget()
    texte_fractales_personnalisees_B.place_forget()
    texte_fractales_personnalisees_G.place_forget()
    texte_fractales_personnalisees_D.place_forget()
    texte_fractales_personnalisees_A_avance.place_forget()
    texte_fractales_personnalisees_B_avance.place_forget()
    texte_fractales_personnalisees_G_tourne.place_forget()
    texte_fractales_personnalisees_D_tourne.place_forget()
    texte_fractales_personnalisees.place_forget()
    texte_fractales_personnalisees_mot.place_forget()
    entree_fractales_personnalisees_A.place_forget()
    entree_fractales_personnalisees_B.place_forget()
    entree_fractales_personnalisees_G.place_forget()
    entree_fractales_personnalisees_D.place_forget()
    entree_fractales_personnalisees_A_avance.place_forget()
    entree_fractales_personnalisees_B_avance.place_forget()
    entree_fractales_personnalisees_G_tourne.place_forget()
    entree_fractales_personnalisees_D_tourne.place_forget()
    entree_fractales_personnalisees_mot.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    #Création de la règle de l'utilisateur
    #entry.get() pour avoir les valeurs rentrées par l'utilsateur, qu'on met ensuite dans un dictionnaire pour former la règle
    regle_perso = {"début": str(entree_fractales_personnalisees_mot.get()), "A": str(entree_fractales_personnalisees_A.get()),"B": str(entree_fractales_personnalisees_B.get()), "G": str(entree_fractales_personnalisees_G.get()),"D": str(entree_fractales_personnalisees_D.get())}
    Schema = File()
    #On enfile le début de la règle
    for c in regle_perso['début']:
        Schema.enfile(c)
    chemin_perso = iter_L_systeme(Schema, regle_perso, n)
    MonCrayon = crayon(300, 400, "red")
    while not chemin_perso.est_vide():
        l = chemin_perso.defile()
        if l == "A":
            #On recupère avec entry.get() les valeurs pour tourner et avancer de + ou -
            MonCrayon.avance(int(entree_fractales_personnalisees_A_avance.get()))
        elif l == "B":
            MonCrayon.avance(int(entree_fractales_personnalisees_A_avance.get()))
        elif l == "D":
            MonCrayon.tourne(int(entree_fractales_personnalisees_D_tourne.get()))
        elif l == "G":
            MonCrayon.tourne(int(entree_fractales_personnalisees_G_tourne.get()))

########################################################################################################################


def choix_generation_pliage():
    "choix_generation_pliage permet d'afficher à l'utilisateur l'interface pour les figures en pliage proposées"
    #Fontion associée au bouton "Génération en pliages"
    bouton_choix_fractales_recursif.place_forget()
    bouton_choix_fractales_l_sys.place_forget()
    bouton_choix_fractales_pliage.place_forget()
    bouton_dragon_pliage.place(x=110, y=160)
    bouton_dragon_rainbow_pliage.place(x=110, y=340)
    bouton_retour.place(x=220, y=640)

def choix_nbr_iterations_dragon_pliage():
    "choix_nbr_iterations_dragon_pliage permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités de la courbe du Dragon en pliage"
    #Fontion associée au bouton "Dragon" dans la section pliage
    bouton_dragon_pliage.place_forget()
    bouton_dragon_rainbow_pliage.place_forget()
    texte_nbr_iterations.place(x=70, y=170)
    entree_nbr_iterations.place(x=160, y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de la courbe du Dragon
    bouton_valider.config(command=valider_dragon_pliage)
    bouton_valider.place(x=270, y=320)

def pliage_dragon(chemin,n):
    "pliage_dragon permet de créer une courbe du Dragon à l'aide d'un chemin (une file) avec n itérations"
    if n == 0 : return chemin
    else:
        F = File()
        P = Pile()
        while not chemin.est_vide():
            c = chemin.defile()
            F.enfile(c)
            P.empile(c)
        F.enfile("G")
        while not P.est_vide():
            c = P.depile()
            if c == "G" :
                F.enfile("D")
            if c == "D":
                F.enfile("G")
        return pliage_dragon(F,n-1)

def valider_dragon_pliage():
    "valider_dragon_pliage permet de valider la génération de la courbe du Dragon en pliage avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    chemin_dragon = File()
    chemin_dragon = pliage_dragon(chemin_dragon,n)
    MonCrayon = crayon(340, 350, "black")
    #Les conditions ci-dessous permettent de replacer le crayon pour que la figure soit à peu près au centre du cadre
    if 10 > n >= 8:
        MonCrayon.pos.x = MonCrayon.pos.x - 100
        MonCrayon.pos.y = MonCrayon.pos.y - 80
    elif 12 > n >= 10:
        MonCrayon.pos.x = MonCrayon.pos.x + 100
        MonCrayon.pos.y = MonCrayon.pos.y - 200
    elif 14 > n >= 12:
        MonCrayon.pos.x = MonCrayon.pos.x + 200
        MonCrayon.pos.y = MonCrayon.pos.y
    else:
        MonCrayon.pos.x = MonCrayon.pos.x - 100
        MonCrayon.pos.y = MonCrayon.pos.y - 100
    while not chemin_dragon.est_vide():
        l = chemin_dragon.defile()
        #Les conditions ci-dessous permettent de réduire l'avancée notée x du crayon pour éviter que la figure ne sorte du cadre
        if n <= 8:
            if l == "G":
                x = 40 - (2.7 * (n - 1))
                MonCrayon.tourne(90)
                MonCrayon.avance(x)
            if l == "D":
                x = 40 - (2.7 * (n - 1))
                MonCrayon.tourne(-90)
                MonCrayon.avance(x)
        elif 12 >= n >= 8:
            if l == "G":
                x = 40 - (3.1 * (n - 1))
                MonCrayon.tourne(90)
                MonCrayon.avance(x)
            if l == "D":
                x = 40 - (3.1 * (n - 1))
                MonCrayon.tourne(-90)
                MonCrayon.avance(x)
        else:
            if l == "G":
                x = 40 / (n * 2.7)
                MonCrayon.tourne(90)
                MonCrayon.avance(x)
            if l == "D":
                x = 40 / (n * 2.7)
                MonCrayon.tourne(-90)
                MonCrayon.avance(x)

def choix_nbr_iterations_dragon_rainbow_pliage():
    "choix_nbr_iterations_dragon_rainbow_pliage permet d'afficher à l'utilisateur l'interface pour entrer le nombre d'itérations souhaités "
    "de la courbe du Dragon de couleur arc-en-ciel en pliage"
    #Fontion associée au bouton "Figure libre" dans la section pliage
    bouton_dragon_pliage.place_forget()
    bouton_dragon_rainbow_pliage.place_forget()
    texte_nbr_iterations.place(x=70, y=170)
    entree_nbr_iterations.place(x=160, y=210)
    #On change ici la commande de bouton_valider pour la validation de la génération de la courbe du Dragon
    bouton_valider.config(command=valider_dragon_rainbow_pliage)
    bouton_valider.place(x=270, y=320)


def pliage_dragon_rainbow(chemin, n):
    "pliage_dragon permet de créer une courbe du Dragon à l'aide d'un chemin (une file) avec n itérations"
    if n == 0:
        return chemin
    else:
        F = File()
        P = Pile()
        while not chemin.est_vide():
            c = chemin.defile()
            F.enfile(c)
            P.empile(c)
        F.enfile("G")
        while not P.est_vide():
            c = P.depile()
            if c == "G":
                F.enfile("D")
            if c == "D":
                F.enfile("G")
        return pliage_dragon_rainbow(F, n - 1)


def valider_dragon_rainbow_pliage():
    "valider_dragon_rainbow_pliage permet de valider la génération de la courbe du Dragon de couleur arc-en-ciel en pliage avec le nombre d'itérations n rentrées par l'utilisateur"
    global n
    texte_nbr_iterations.place_forget()
    bouton_valider.place_forget()
    entree_nbr_iterations.place_forget()
    texte_fractales.place_forget()
    Canevas.config(width=700, height=665)
    Canevas.place(x=0, y=0)
    #entree_nbr_iterations correspond à l'entrée du nombre d'itérations souhaitées par l'utilisateur
    n = int(entree_nbr_iterations.get())
    compteur = 0
    #Liste de toutes les couleurs qui composent l'arc en ciel
    liste_arc_en_ciel = ['#f54542','#f56f42','#f59642','#f5bf42','#f5ec42','#cef542','#42f542','#42f572','#42f593','#42f5c5','#42f5ef','#42c2f5','#4290f5','#4257f5','#6942f5','#8d42f5','#bc42f5','#f242f5','#f542ce','#f5429c','#f54272']
    chemin_dragon_rainbow = File()
    chemin_dragon_rainbow = pliage_dragon_rainbow(chemin_dragon_rainbow, n)
    MonCrayon = crayon(340, 350,"red")
    #Les conditions ci-dessous permettent de replacer le crayon pour que la figure soit à peu près au centre du cadre
    if 10 > n >= 8:
        MonCrayon.pos.x = MonCrayon.pos.x - 100
        MonCrayon.pos.y = MonCrayon.pos.y - 80
    elif 12 > n >=10:
        MonCrayon.pos.x = MonCrayon.pos.x + 100
        MonCrayon.pos.y = MonCrayon.pos.y - 200
    elif 14 > n >=12:
        MonCrayon.pos.x = MonCrayon.pos.x + 200
        MonCrayon.pos.y = MonCrayon.pos.y
    else:
        MonCrayon.pos.x = MonCrayon.pos.x - 100
        MonCrayon.pos.y = MonCrayon.pos.y - 100
    while not chemin_dragon_rainbow.est_vide():
        #L'incrémentation du compteur permet de parcourir la liste des couleurs de l'arc en ciel et d'appliquer une couleur à un trait, dans l'ordre de l'arc ciel
        compteur = compteur + 1
        if compteur >= 21:
            compteur = 0
        l = chemin_dragon_rainbow.defile()
        #Les conditions ci-dessous permettent de réduire l'avancée notée x du crayon pour éviter que la figure ne sorte du cadre
        if n <= 8:
            if l == "G":
                x = 40 - (2.7 * (n - 1))
                #On change la couleur du crayon
                MonCrayon.couleur = liste_arc_en_ciel[compteur]
                MonCrayon.tourne(90)
                MonCrayon.avance(x)
            if l == "D":
                x = 40 - (2.7 * (n - 1))
                #On change la couleur du crayon
                MonCrayon.couleur = liste_arc_en_ciel[compteur]
                MonCrayon.tourne(-90)
                MonCrayon.avance(x)
        elif 12 >=n >= 8:
            if l == "G":
                x = 40 - (3.1 * (n - 1))
                #On change la couleur du crayon
                MonCrayon.couleur = liste_arc_en_ciel[compteur]
                MonCrayon.tourne(90)
                MonCrayon.avance(x)
            if l == "D":
                x = 40 - (3.1 * (n - 1))
                #On change la couleur du crayon
                MonCrayon.couleur = liste_arc_en_ciel[compteur]
                MonCrayon.tourne(-90)
                MonCrayon.avance(x)
        else:
            if l == "G":
                x = 40 / (n * 2.7)
                #On change la couleur du crayon
                MonCrayon.couleur = liste_arc_en_ciel[compteur]
                MonCrayon.tourne(90)
                MonCrayon.avance(x)
            if l == "D":
                x = 40 / (n * 2.7)
                #On change la couleur du crayon
                MonCrayon.couleur = liste_arc_en_ciel[compteur]
                MonCrayon.tourne(-90)
                MonCrayon.avance(x)

########################################################################################################################

#Création des textes et entrées nécessaires :

texte_fractales = Label(fenetre,text = "Génération de fractales",font = ("Courier",32,"underline"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees = Label(fenetre,text = "Créer votre propre fractale via votre propre L-système : ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_A = Label(fenetre,text = "A => ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_B = Label(fenetre,text = "B => ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_G = Label(fenetre,text = "G => ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_D = Label(fenetre,text = "D => ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_A_avance = Label(fenetre,text = "Avance de  ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_B_avance = Label(fenetre,text = "Avance de  ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_G_tourne = Label(fenetre,text = "Tourne de  ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_D_tourne = Label(fenetre,text = "Tourne de  ",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_fractales_personnalisees_mot = Label(fenetre,text = "Mot :",font = ("Courier",12,"bold"),fg="white",bg ='#009DE4')

texte_nbr_iterations = Label(fenetre,text = "Choississez le nombre d'itérations souhaités : ",font = ("Courier",15,"bold"),fg="white",bg ='#009DE4')

entree_nbr_iterations = Entry(fenetre,font=("",25,""))

entree_fractales_personnalisees_A = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_B = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_G = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_D = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_A_avance = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_B_avance = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_G_tourne = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_D_tourne = Entry(fenetre,font=("",12,""),width=8)

entree_fractales_personnalisees_mot = Entry(fenetre,font=("",12,""),width=8)

########################################################################################################################

#Création des boutons nécessaires :

bouton_retour = Button(fenetre,text = "Retour",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=20,command=retour)

bouton_valider = Button(fenetre,text = "Valider",font=("Courier",15,""),bg='#009DE4',fg="white",height=1,width=12,command=valider_sierpinski_recursif)

bouton_choix_fractales_recursif = Button(fenetre,text = "Génération en récursif",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_generation_recursif)

bouton_choix_fractales_l_sys = Button(fenetre,text = "Génération en l-système",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_generation_l_sys)

bouton_choix_fractales_pliage = Button(fenetre,text = "Génération en pliages",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_generation_pliage)

bouton_sierpinski_recursif = Button(fenetre,text ="Triangle de Sierpinski",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_sierpinski_recursif)

bouton_koch_recursif = Button(fenetre,text ="Flocon de Koch",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_koch_recursif)

bouton_menger_recursif = Button(fenetre,text ="Eponge de Menger",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_meger_recursif)

bouton_hilbert_l_sys = Button(fenetre,text ="Courbe de Hilbert",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_hilbert_l_sys)

bouton_koch_l_sys = Button(fenetre,text ="Flocon de Koch",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_koch_l_sys)

bouton_gosper_l_sys = Button(fenetre,text ="Courbe de Gosper",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_gosper_l_sys)

bouton_dragon_pliage = Button(fenetre,text ="Dragon",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_dragon_pliage)

bouton_dragon_rainbow_pliage = Button(fenetre,text ="Figure libre",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_dragon_rainbow_pliage)

bouton_fractale_personnalisee_l_sys = Button(fenetre,text ="Fractale personnalisée",font=("Courier",15,""),bg='#009DE4',fg="white",height=2,width=40,command=choix_nbr_iterations_fractale_personnalisee_l_sys)

########################################################################################################################

#Mise en place de la page d'accueil pour créer les fractales :
texte_fractales.place(x=52,y=30)
bouton_choix_fractales_recursif.place(x=110,y=160)
bouton_choix_fractales_l_sys.place(x=110,y=340)
bouton_choix_fractales_pliage.place(x=110,y=520)

########################################################################################################################



fenetre.mainloop()