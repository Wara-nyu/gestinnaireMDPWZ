#!/usr/bin/python3

start = input("Recherche/Entrer : ")
start = start.capitalize()
if start == "Entrer" :
    URL = input("entrez le site web : ")
    Id = input("entrez votre identifiant : ")
    mdp = input("entrez votre mot de passe : ")
    URL = URL.capitalize()
    with open('personal', 'a') as personal:
        personal.write(URL + ", " + Id + ", " + mdp + "\n")

elif start == "Recherche" :
    liste = input("nom du site : ")
    with open("personal", "r") as fichier:
        for ligne in fichier:
            if liste in ligne :
                print(ligne)
            else :
                print("Désolé, je n'ai pas trouvé")
else :
    print ("Je n'ai pas compris votre requête")
