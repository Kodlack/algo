#coding: UTF-8


import random
import os



os.system('clear')

def placer(tab, gauche, droite, compteur):
	bas = gauche + 1
	haut = droite
	if gauche >= 0 and droite <= len(tab):
		while bas <= haut:
			while tab[bas] <= tab[gauche]:
				bas += 1
			while tab[haut] > tab[gauche]:
				haut -= 1
			compteur +=1
			if bas < haut:
				echanger(tab, bas, haut)
				bas += 1
				haut -= 1
		echanger(tab, gauche, haut)
		k = haut
		return tab, k, compteur

def tri_rapide(tab, gauche, droite, compteur):
	k = 0
	compteur = 0 + compteur
	if gauche < droite:
		tab, k, compteur = placer(tab, gauche, droite, compteur)
		tab, compteur= tri_rapide(tab, gauche, k-1, compteur)
		tab, compteur = tri_rapide(tab, k+1, droite, compteur)
	return tab, compteur
		
		
def echanger(tab, a, b):
	tempo = tab[a]
	tab[a] = tab[b]
	tab[b] = tempo

def afficher_tableau(tab):
	print ""
	for i in tab:
		if i is tab[0]:
			print "["+str(i)+",",
			continue
		if i is tab[len(tab)-1]:
			print str(i)+"]"
			break
		print str(i)+",",



def alea_tableau(*n):
	tableau = []
	try:
		n = int(n[0])
		taille = n
		for i in range(taille):
			tableau.append(random.randint(-999, 1000))
		tableau.append(max(tableau)+(random.randint(0, 413)))
		return tableau
	except:
		taille = random.randint(1, 1000)
		for i in range(taille):
			tableau.append(random.randint(-999, 1000))
		tableau.append(max(tableau)+(random.randint(0, 413)))
		return tableau


tableau = alea_tableau(raw_input())
#tableau1 = entrée_tab(raw_input())
nouveau_tableau, compteur = tri_rapide(tableau, 0, len(tableau)-1, 0)
afficher_tableau(nouveau_tableau)
print compteur












