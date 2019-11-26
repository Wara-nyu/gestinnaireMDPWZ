#!/usr/bin/python

import csv

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


   
