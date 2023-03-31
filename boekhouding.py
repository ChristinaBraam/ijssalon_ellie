import csv 

from presentatie import *
from helper import *


inkomsten = {
"Aardbeien-ijs-totaal" : 1000,
"Vanille-ijs-totaal" : 2000,
"Chocolade-ijs-totaal" : 1500,
"Waterijsjes-totaal" :750
}

def som(inkomsten):
    totaal = inkomsten["Aardbeien-ijs-totaal"] + inkomsten["Vanille-ijs-totaal"] + inkomsten["Chocolade-ijs-totaal"] + inkomsten["Waterijsjes-totaal"]
    return totaal

totaal_inkomsten = som()
presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv,, 'w',newline='') as csvfile:
          for key, value in inkomsten.items():
          writer = csv.writer(csvfile, delimter=';')
          writer.writerow([key,value])
          