#Coding UTF-8

def Tri_inser(tab):
	i =0
	j =0
	for (i=2; i < n ; i++):
		j=i-1
		x = tab[i]
		while (tab[j]< x):
			tab[j+1]=tab[j]
			j = j-1
		tab[j+1]=x
	return tab

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
nouveau_tableau, compteur = tri_inser(tableau, 0, len(tableau)-1, 0)
afficher_tableau(nouveau_tableau)
print compteur






