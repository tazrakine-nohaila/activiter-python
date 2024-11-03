T1 = [4, 8, 7, 12]
T2 = [3, 6, 2, -1]
T = []
# Récupération de la longueur des tableaux
n1 = len(T1)
n2 = len(T2)
n = n1 + n2

# Boucle pour alterner les valeurs de T1 et T2
i = 0
j = 0
for h in range(n):
    if h % 2 == 0:
        if i < n1:
            T.append(T1[i])
            i += 1
    else:
        if j < n2:
            T.append(T2[j])
            j += 1
print("T:", T)