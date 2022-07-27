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

if(len(barcode)) == 13:
    for (i = 1; i <= 13; i++) in barcode:
        if i % 2 != 0:
            summe + int(ziffer) *3
        else:
            summe + int(ziffer)

elif(len(barcode)) > 13:
    print("Barcode zu lang!")

print("Zu kleiner Barcode")

# barcode "12345"
# 1 Zähler=1, wenn zählernummer / 2 ,5 ergibt, dann, wenn es ,0 ergebit, dann was anderes
# wenn ,5 dann ist es ungerade, dann addieren wir (ziffer * 3) zu Summe
# Wenn nicht, dann ist gerade, dann addieren wir (ziffer) zu summe
