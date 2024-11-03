stagiaires = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
notes = [10, 8, 16, 5, 10, 14, 10, 10, 8, 6, 7, 12, 6, 8, 10]
# Calcul de la fréquence des notes
frequence = [0] * 21
for note in notes:
    frequence[note] += 1
# Affichage des notes et de leurs fréquences
print("Notes et fréquences :")
for i in range(len(frequence)):

    print(f"{i}: {frequence[i]}")

# Calcul de la moyenne
somme_notes = 0
nombre_stagiaires = len(notes)

for note in notes:
    somme_notes += note

moyenne = somme_notes / nombre_stagiaires
print("Moyenne de la classe:", moyenne)

# Affichage du diagramme de fréquence
max_frequence = max(frequence)
# Affichage du diagramme
for niveau in range(max_frequence, 0, -1):
    ligne = ""
    for freq in frequence:
        if freq >= niveau:
            ligne += "#     "
        else:
            ligne += "      "
    print(ligne)

# Affichage de l'axe des x
axe_x = ""
for i in range(len(frequence)):
    axe_x += str(i) + "  "
print(axe_x)