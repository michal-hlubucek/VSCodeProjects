'''# list, indexování

zamestnanci = [
    "František", "Bruno",
    "Anna", "Jakub",
    "Klára", "Anežka",
    "Anežka", "Anežka"
]
posledni_index = len(zamestnanci) - 1
print("Na indexu 2 je:", zamestnanci[2])
print("Na", posledni_index, "indexu je:", zamestnanci[posledni_index])
print("V intervalu od 2 do 5 je:", zamestnanci[2:6])
print("každý třetí prvek je:", zamestnanci[::3])'''

# BMI kalkulačka

jmeno = "Martin"
vaha = 80
vyska = 1.8
bmi = int(vaha / vyska ** 2)
kategorie = ""
if bmi > 40:
    kategorie = "těžká obezita"
elif bmi > 30:
    kategorie = "obezita"
elif bmi > 25:
    kategorie = "mírná nadváha"
elif bmi > 18.5:
    kategorie = "zdravá váha"
else:
    kategorie = "podvýživa"

print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie, ".")

'''# list, přidávání hodnot

zamestnanci = ["František", "Anna", "Jakub", "Klára"]
print("Zaměstnanci na začátku:", zamestnanci)
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anežka")
print("Nová jména přidána:", zamestnanci_a)
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")
print("Nová jména vložená:", zamestnanci_b)'''

'''# První písmeno

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "u", "s", "č", "p", "s", "n"]
tyden = ("pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota", "neděle")
cislo_dne = 3
if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota!")
    den_tydne = tyden[cislo_dne - 1]
    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        print("Správné písmeno!")
    else:
        print("Špatné písmeno!")
else:
    print("Špatná vstupní hodnota!")'''


'''# Destinatio 2 - rezervace jízdenek

# Vstupní data
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
slevy = ("Olomouc", "Svitavy", "Ostrava")
domeny = ("gmail.com", "seznam.cz", "email.cz")
dvojita_cara = "=" * 35
cara = "-" * 35

nabidka = """ 
1 - Praha      | 150,- Kč 
2 - Viden      | 200,- Kč 
3 - Olomouc    | 120,- Kč 
4 - Svitavy    | 120,- Kč 
5 - Zlin       | 100,- Kč 
6 - Ostrava    | 180,- Kč 
"""

AKT_ROK = 2025

# Pozdrav a nabídka
print("Vítejte u naší aplikace Destinatio!")
print(dvojita_cara)

print(nabidka)
print(dvojita_cara)

# Výběr čisla destinace
destinace_cislo = int(input("Vyber číslo destinace: "))
if destinace_cislo >= 1 and destinace_cislo <= 6:
    destinace_nazev = mesta[destinace_cislo - 1]
    print("Destinace:", destinace_nazev.upper())
else:
    print("Destinace číslo", destinace_cislo, "NEEXISTUJE!")
    quit()
print(cara)

# Přepočet po slevě
if destinace_nazev in slevy:
    vysledna_cena = ceny[destinace_cislo - 1] * 0.75
    print("Získáváte slevu 25%! Nová cena:", vysledna_cena, ",-")
else:
    vysledna_cena = ceny[destinace_cislo - 1]
    print("Jízdenka beze slevy. Cena:", vysledna_cena, ",-")
print(cara)

# Zadání jména
cele_jmeno = input("Zadejte celé jméno: ")
krestni_jmeno = cele_jmeno.split()[0]
if krestni_jmeno.isalpha():
    print("Křestní jméno:", krestni_jmeno)
else:
    print("Neplatné jméno!")
print(cara)

# Zjištění věku
rok_narozeni = int(input("Váš rok narození:"))
zjisteni_pristupu = AKT_ROK - rok_narozeni
if zjisteni_pristupu >= 18:
    print("Přístup povolen...")
else:
    print("Jste příliš mladý na nákup jízdenek! \nUkončuji program")
    quit()
print(cara)

# Kontrola e-mailu
email = input("Zapište vaši e-mailovou adresu: ")
if "@" in email and email.split("@")[1] in domeny:
    print("Ověření e-mailu proběhlo v pořádku.")
else:
    print("Tento e-mail je neplatný! \nUkončuji program")
    quit()
print(cara)

# Závěrečná zpráva
print("Děkuji", krestni_jmeno, "za objednávku jízdenky.")
print("Cílová destinace:", destinace_nazev, ", cena jízdného:", vysledna_cena, ",-")
print("Na váš e-mail:", email, "jsme odeslali e-jízdenku.")
print(dvojita_cara)'''
    



