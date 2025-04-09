
vyska = 1.75
vaha = 80
jmeno = "Martin"
bmi = int(vaha / vyska ** 2)
kategorie = None

if bmi > 40:
  kategorie = "Těžká obezita"
elif 39 >= bmi >= 30:
  kategorie = "Obezita"
elif 29 >= bmi >= 25:
  kategorie = "Mírná nadváha"
elif 24 >= bmi >= 18.5:
  kategorie = "Zdravá váha"
else:
  kategorie = "Podvýživa"

print("Jméno:", jmeno, ", kategorie:", kategorie)