#!/usr/bin/python3

start = input("recherche/entrer : ")

<<<<<<< HEAD
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
=======
with open('persons.csv', 'w') as csvfile:


    filewriter = csv.writer(csvfile, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["URL", "Identifiant", "Mot de pass"])
    filewriter.writerow(["Amazon.com", "Florian", "Florianestfou"])
    filewriter.writerow(["facebook.com", "Flo", "jaimelaguitare" ])
    filewriter.writerow(["instagram", "Fl0R1an", "nem"])

with open('persons.csv', 'r') as csvfile: 
    reader = csvfile.read()
    print(reader)


   
>>>>>>> 543e840f7a6f2f6d4519828dfb15d6df65c3f4f5
