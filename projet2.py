# !python3
# Nikita Servais
# Projet2.py : le pendu
# 30/10/17


from turtle import *
from random import randint

# functions
def dmot():
    """
    prend tout les mots du fichier mots.txt et les ajouts dans une liste
    """
    fichier=open("mots.txt", "r")
    liste=[]
    for line in fichier:
        liste.append(line.strip())
    nb=randint(-len(liste),len(liste))
    mot=liste[nb]
    fichier.close()
    return mot 
def erreur_1():
    """
    dessine la 1er erreur, support+poteau de pendaison
    """
    #support du poteau 
    penup()
    setpos(-8*30,30)
    pendown()
    forward(16*30)
    seth(0)
    #poteau de pendaison
    penup()
    setpos(0,7*30)
    pendown()
    left(90)
    forward(30)
    left(90)    
    forward(3*30)
    left(90)
    forward(7*30)
    seth(0)
def erreur_2():
    """
    dessine la 2eme erreur, la tete du pendu
    """
    #tete du pendu
    penup()
    setpos(0,7*30)
    seth(180)
    pendown()
    circle(15,None,30)
    seth(0)
def erreur_3():
    """
    dessine la 3eme erreur, le corps du pendu
    """
    #corps du pendu
    penup()
    setpos(0,6*30)
    seth(270)
    pendown()
    forward(2*30)
def erreur_4():
    """
    dessine la 4eme erreur, le bras droit du pendu
    """
    #bras droit du pendu
    penup()
    setpos(0,5.5*30)
    pendown()
    setpos(30,4.5*30)
def erreur_5():
    """
    dessine la 5eme erreur, le bras gauche du pendu
    """
    #bras gauche du pendu
    penup()
    setpos(0,5.5*30)
    pendown()
    setpos(-30,4.5*30)
def erreur_6():
    """
    dessine la 6eme erreur, la jambe droite du pendu
    """
    #jambe droite du pendu
    penup()
    setpos(0,4*30)
    pendown()
    setpos(30,3*30)
def erreur_7():
    """
    dessine la derniere erreur, la jambe gauche du pendu+ecran rouge
    """
    #la jambe gauche du pendu
    penup()
    setpos(0,4*30)
    pendown()
    setpos(-30,3*30)
    #affiche l'ecran en rouge
    bgcolor("red")
def draw_():
    """
    dessine les traits_ representant le nb de lettre du mot selectioner
    """
    penup()
    setpos((-len(mot)*30)/2,-50)
    pendown()
    for i in range (len(mot)) :
        pendown
        forward(15)
        penup()
        forward(15)
        pendown()

hideturtle()
mot=dmot()
draw_()
erreur=0
f=0
restart = True
while restart :
        
    #main_loop(no restart)
    while erreur<7 and f<len(mot):
        l=textinput("Input","Lettre :")
        #check input is good
        if l==None :
            done()
        while len(l)!=1 :
            l=textinput("Input","Lettre :")
        #check if lettre in mot

        e=0
        for i in range (len(mot)):
            if mot[i]==l:
                penup()
                setpos((-len(mot)*30)/2+30*(i)+5,-45)
                pendown()
                write(l)
                f+=1
                e+=1
        #if lettre not in word draw next erreur
        if e==0 :
            penup()
            setpos((-len(mot)*30)/2+15*(erreur),-100)
            pendown()
            write(l)
            erreur+=1
            if erreur==1 :
                erreur_1()
            elif erreur==2 :
                erreur_2()
            elif erreur==3 :
                erreur_3()
            elif erreur==4 :
                erreur_4()
            elif erreur==5 :
                erreur_5()
            elif erreur==6 :
                erreur_6()
            elif erreur==7 :
                erreur_7()
        
    
        

    
    
    
    
