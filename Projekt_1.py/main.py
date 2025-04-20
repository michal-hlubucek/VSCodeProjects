"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Hlubůček
email: hlubucek.michal@centrum.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#users = ("bob", "ann", "mike", "liz")
#passwords = ("123", "pass123", "password123", "pass123")
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
line = "-" * 40

user = input("username:")
password = input("password:")

print(line)

# vyhodnocení zadaného jména a hesla
if user in users.keys() and users.get(user) == password:
    print("Welcome to the app,", user)
else:
    print("unregistered user, terminating the program..")
    quit()
pocet_textu = len(TEXTS)
print(f"We have {pocet_textu} texts to be analyzed.")
print(line)

# vybrání textu z listu
select_number = input(f"Enter a number btw. 1 and {pocet_textu} to select:")
print(line)

# vyhodnocení zadání od uživatele
if not select_number.isdigit():
    print("Zadaný parametr není číslo. Ukončuji program..")
elif int(select_number) > pocet_textu:
    print("Zadané číslo není v zadání textů. Ukončuji program..")
else:
    vyber_textu = TEXTS[int(select_number) - 1]


# spočítání statistik
vycistena_slova = []
pocet_slov_s_velkym_pismenem = 0
pocet_velkych_slov = 0
pocet_malych_slov = 0
pocet_cisel = 0
suma = []


for slovo in vyber_textu.split():
    ciste_slovo = slovo.strip(",.;:'")
    if ciste_slovo.istitle():
        pocet_slov_s_velkym_pismenem += 1
    elif ciste_slovo.isupper():
        pocet_velkych_slov += 1
    elif ciste_slovo.islower():
        pocet_malych_slov += 1
    elif ciste_slovo.isnumeric():
        pocet_cisel += 1
        suma.append(int(ciste_slovo))
        soucet = sum(suma)
    vycistena_slova.append(ciste_slovo)
    pocet_slov = len(vycistena_slova)
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_slov_s_velkym_pismenem} titlecase words.")
print(f"There are {pocet_velkych_slov} uppercase words.")
print(f"There are {pocet_malych_slov} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {soucet}")
print(line)

# sloupcový graf délek slov
cetnosti = {}

for ciste_slovo in vycistena_slova:
    delka = len(ciste_slovo)
    cetnosti[delka] = cetnosti.get(delka, 0) + 1

print("LEN|", "OCURRENCES", "|NR.\t")
print(line)
for delka in sorted(cetnosti):
    hvezdicky = '*' * cetnosti[delka]
    print(f"{delka}  |{hvezdicky} |{cetnosti[delka]}")
    

