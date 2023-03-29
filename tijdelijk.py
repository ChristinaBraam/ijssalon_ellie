prijzen = {
"aardbei" : 3,
"vanille" : 4,
"chocolade" : 5
}
aanbieding = prijzen["aardbei"] * 0.8

reclame_tekst = f"Vandaag in de aanbieding: Vanille-ijs, 1 Liter – slechts € {aanbieding}"
print(reclame_tekst)
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3
for el in reclame_tekst4:
    print(el.lower())
if el>=5:
    print(el.upper())
else:
    print(el.lower())






      


