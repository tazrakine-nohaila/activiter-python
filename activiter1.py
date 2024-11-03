Tableau1=[4,8,7,9,1,5,4,6]
Tableau2=[7,6,5,2,1,3,7,4]
tableau3=[]
if len(Tableau1)!=len(Tableau2):
    print("les tableaux doivent avoir la meme longeur.")
else:
    for i in range(len(Tableau1)):
      somme = Tableau1[i] + Tableau2[i]
      tableau3.append(somme)
print(tableau3)