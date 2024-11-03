#Dimension des tableaux
n = 10
#Remplissage du tableau U1
print("Remplissage du tableau U1 :")
U1 = []
for i in range(n):
    while True:
        try:
            valeur = int(input(f"Saisir l'élément {i + 1}/{n} : "))
            U1.append(valeur)
            break
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")

# Remplissage du tableau U2
print("Remplissage du tableau U2 :")
U2 = []
for i in range(n):
    while True:
        try:
            valeur = int(input(f"Saisir l'élément {i + 1}/{n} : "))
            U2.append(valeur)
            break
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")
#Création du tableau U2
L = []
for i in range(n):
    if U2[i] == 1:
        L.append(U1[i])
    else:
        L.append(0)

# Affichage des résultats
print("Tableau U1 :", U1)
print("Tableau U2 :", U2)
print("Tableau L :", L)
