def presenteer(dictionary, totaal):
    dictionary = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
    }
    totaal = dictionary["Aardbeien-ijs-totaal"] + dictionary["Vanille-ijs-totaal"] + dictionary["Chocolade-ijs-totaal"] + dictionary["Waterijsjes-totaal"]
    uitvoer = dictionary , "=" * 25, totaal, " "
    return uitvoer

