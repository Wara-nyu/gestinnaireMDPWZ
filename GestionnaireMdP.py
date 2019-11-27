#!/usr/bin/python3

start = input("recherche/entrer : ")

if start == entrer :
    URL = input("entrez le site web : ")
    Id = input("entrez votre identifiant : ")
    mdp = input("entrez votre mot de passe : ")

    with open('personal', 'a') as personal:
        personal.write(URL + ", " + Id + ", " + mdp)

elif start == recherche :
    liste = input("nom du site : ")
    with open("personal", "r") as fichier:
        for ligne in fichier:
            if liste in ligne :
                print(ligne)
else 
    print("error")
