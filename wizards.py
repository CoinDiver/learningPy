wizards = sorted(["Raistlin", "Merlin", "Dumbledore", "Voldemort", "Fizban"])

wizards_total = 0
for wizard in wizards:
    if wizard != "Fizban":
        print(wizard + " rocks!")
    wizards_total = wizards_total +1
    if wizard == "Fizban":
        print("Verreck, " + wizard)
print("Magic roxxors!")
print(wizards_total)
