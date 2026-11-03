# #Job 1
# def fruit():
#     return ["pomme", "cerise", "orange"]

# print(fruit())


# #Job 2
# def afficher_deuxieme():
#     print(fruit()[1])
# afficher_deuxieme()


# #Job 3
# def ajouter_fruit():
#     liste = fruit()
#     liste.append("melon")
#     return liste
# print(ajouter_fruit())


# #Job 4
# def inserer_fruit():
#     insfruit = ajouter_fruit()
#     insfruit.insert(2, "mangue")
#     print(insfruit)
# inserer_fruit()











# #Job 5
# l=[5,6,8,2,9]

# print(l)
# print(l[1])

# l[3] = l[2]+l[4]
# print(l)

# print(l[-1])












# #Job 6
# liste=[1,2,3,4,5]
# print(liste)
# print(liste[::-1])

# liste[0],liste[4]=liste[4],liste[0]
# print(liste)







# #Job 7
# liste=[8,24,48,2,16]

# compteur = 0
# for i in liste:
#     if i % 3==0:
#         compteur += 1

# print(compteur)








# #Job 8
# liste =[8,24,27,48,2,16,9,7,84,91]


# somme = 0
# for i in liste :
#     if i % 2 ==0:
#         somme +=i
#         print(i)
# print(somme)






# #Job 9
# liste = [8,24,27,48,2,16,9,102,7,84,91]

# print("La valeur max est :",max(liste))
# print("La valeur min est :",min(liste))





# #Job 10
# liste = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# produit=1
# for i in liste:
#     if 25<i<90:
#         produit *=i
# print(produit)










# #Job 11
# liste = [7, 11, 42, 39, 2]


# liste = [x+1 for x in liste]
# print(liste)  # ici on a bien modifier completement la liste



# for i in liste:
#     i+=1
#     print(i)  #on affiche juste la boucle mais on a pas modifier la liste 



# liste = [7, 11, 42, 39, 2]

# for i in range(len(liste)):
#     liste[i] += 1

# print(liste)  # ici on a bien modifier completement la liste 










# #Job 12
# l = [5,9,48,26,45,74,52,0,3,7,12,15,62,47,54,6,8,10,11,13]


# # 1. Calcul de la taille
# n = 0
# for x in l:
#     n += 1

# # 2. Tri à bulles (sans sort, sans len)
# for j in range(n):
#     for i in range(n - 1):  # n - 1 évite que l[i+1] sortent de la liste !
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]

# print(l)










# #Job 13 
# liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# print(liste)

# liste = list(set(liste)) # suprime les doublons en convertissant la liste en ensemble puis en liste
# print("Suppression des doublons :",liste)

# liste.sort() # trie la liste en ordre croissant
# print("Ordre croissant :",liste)








# #Job 14
# def my_long_word(n,char):
#     resultat=""
#     for mot in char.split():
#         compteur = 0
#         for lettre in mot:
#             compteur += 1
#         if compteur > n:
#             resultat += mot + " "
#     return resultat

# print(my_long_word(3,"La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))















# #Job 15

# liste = [22.6, 4.0, 16.22, 9.55, 11.00, 12.22, 14.70, 5.20, 17.50]
# print("Liste originale :", liste)

# liste.sort()
# print("Liste triée :", liste)

# liste_arrondie = [int(nombre + 0.5) for nombre in liste]
# print(liste_arrondie)

