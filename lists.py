# Aufgabe: Barcode eingeben, Prüfziffer eingeben
# Regel: Barcode hat 13 Ziffern, wir nehmen jede ungerade Ziffer *3, jede gerade Ziffer *1
# Die Prüfziffer ist die Summe aller modifizierten Ziffer in der Zahl
# 123
# 14
# 1*3 2*1 3*3 14
# Ergebnis 123 = 14

print("Bitte gebe den barcode ein")
barcode = input() # STRING!
print("Bitte gebe die Prüfziffer ein")
pruefziffer = int(input()) # STRING zu INT

summe = 0

for i, i = 13, i--