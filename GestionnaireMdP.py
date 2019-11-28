 #!/usr/bin/python

import csv
import sys 

with open('persons.csv', 'w') as csvfile:


    filewriter = csv.writer(csvfile, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["URL", "Identifiant", "Mot de pass"])
    filewriter.writerow(["Amazon.com", "Florian", "Florianestfou"])
    filewriter.writerow(["facebook.com", "Flo", "jaimelaguitare" ])
    filewriter.writerow(["instagram", "Fl0R1an", "nem"])

#with open ("persons.csv", "r") as csvfile:
  
 #   liste = ["URL", "Identifiant", "Mot de pass"]
  #     for f in sorted(set(liste)):
   #      print f 

#for arg in sys.argv:
 #   print arg

with open("persons.csv") as csvfile:
    
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["URL"], row["Identifiant"])
       	print(row)

for arg in sys.argv:
    print arg
  
recherche = input("Veuillez entre votre recherche: ") 

with open("persons.csv","r") as csvfile:

	for row in csvfile:
		if recherche in row: 
			print(row) 
