#coding: UTF-8
from affiche_arbre import *
import os



def recherche(x, a):
	if(a== None):
		return None
	if(a.val < x):
		return recherche(x, a.D)
	else:
		return recherche(x, a.G)
	print a.val
		
		
def insertionfeuille(x, a):
	if(a==None):
		return creerfeuille(x)
	else:
		if(a.val >= x):
			a.G = insertionfeuille(x,a.G)
		else:
			a.D = insertionfeuille(x, a.D)
	return a
	
	
def creerfeuille(x):
	a = Arbre(None, None, None)
	a.val = x
	a.G = None
	a.D = None
	return a
	
	
def supression(x, a):
	if(a==None):
		return a
	elif(a.val == x):
		return supressionracine(a)
	else:
		if(a.val > x):
			a.G = supressionx(a.G)
			return a
		else:
			a.D = supression(a.D)
			return a
			
			
def supressionracine(a):
	if(a.G == None):
		a=a.D
		return a
	else:
		b = a.G
		if(a.D == None):
			a.val = b.val
			a.G=b.g
			return a
		else:
			temp=b.droit
			while(temp.d != None):
				b=temp
				temp=temp.d
			a.val=temp.val
			b.d=temp.g
			return a

def creation_arbre():#utilise insertionfeuille en boucle sur une ABR initialisé dans cette fonction, on utilise pas la fonction saisie ABR
	clef = input("Entrez une clef pour l'arbre, 0 pour arreter")
	a = Arbre(clef, None, None)
	while(clef != 0):
		clef = input("Entrez une clef pour l'arbre, 0 pour arreter")
		insertionfeuille(clef, a)
	return a

def afficheordrecroissant(a):
	if (a != None):
		afficheordrecroissant(a.G)
		print "[", a.val, "]"
		afficheordrecroissant(a.D)

os.system('clear')


arbre = creation_arbre()


treeDrawer = TreeDrawer()
treeDrawer.dessiner_arbre(arbre)
treeDrawer.wait()


afficheordrecroissant(arbre)
print "Recherchez un nombre dans l'arbre A"
x = input()
recherche(x, arbre)
print "Inserez une valeur dans l'arbre A"
z = input()
insertionfeuille(z, arbre)
print "Inserez une valeur a supprimer dans l'arbre"
y = input()
supression(y, arbre)















