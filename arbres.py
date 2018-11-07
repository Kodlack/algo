#coding: UTF-8
from affiche_arbre import *
from saisie import *


def Noeuds_simples(A):#retourne true si il y a un noeud simple
	if(A==None)or (A.G == None and A.D==None):
		return False
	elif(A.G!=None)and A.D != None:
		return Noeuds_simples(A.G)or Noeuds_simples(A.D)
	else:
		return True
	
def etiquetage(A):
	oper = ["+", "-", "*", "/", "^"]
	if(A== None):
		return False
	elif(A.val in oper):
		return etiquetage(A.G) and etiquetage(A.D)
	elif(A.G ==None)and(A.D == None):
		return True
	else:
		return False
	
def check(A):#vérifie que l'arbre donne une expression correcte a faire avec le parcours préfixe
	if(A!=None):
		if( Noeuds_simples(A))or (not etiquetage(A)):
			return False
		else:
			return True
	else:
		return False
		
		
arbre = entrerArbre(1)
print check(arbre)
		
