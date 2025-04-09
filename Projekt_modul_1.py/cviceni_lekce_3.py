# Movies
from pprint import pprint
# vstupní údaje
oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", "reziseri", "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

# Spojíme všechny slovníky filmů do jednoho slovníku jménem filmy
filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}

# Uvítání a výpis nabídky
uzivatel = input("Zadej jméno:")

if uzivatel in uzivatele:
    print("V pořádku", oddelovac, sep="\n")
    print("Vítejte v našem filmovém slovníku!".upper().center(62), oddelovac, sep="\n")
    print(("| " + " | ".join(sluzby) + " |").center(62), oddelovac, sep="\n")
else:
    print("Neplatný uživatel, ukončuji program!")
    quit()

# Výběr filmu a výpis všech dostupných filmů
vyber = input("Vyber službu:")

if vyber in sluzby and vyber == "dostupne filmy":
    print("Dostupné filmy:", ", ".join(filmy), oddelovac, sep="\n")
# Detaily vybraného filmu
elif vyber in sluzby and vyber == "detaily filmu":     
    print("Dostupné filmy:", ", ".join(filmy))
    nazev_filmu = input("Vyber film:")
    if nazev_filmu == "Shawshank Redemption":
        print("Detaily filmu:", film_1, oddelovac, sep="\n")
    elif nazev_filmu == "The Godfather":
        print("Detaily filmu:", film_2, oddelovac, sep="\n")
    elif nazev_filmu == "The Dark Knight":
        print("Detaily filmu:", film_3, oddelovac, sep="\n")
    elif nazev_filmu == "The Prestige":
        print("Detaily filmu:", film_4, oddelovac, sep="\n")
    else:
        print("Neplatný film...")
# Přiřazení jména režiséra k názvu filmu
elif vyber in sluzby and vyber == "reziseri":   
    reziseri = {filmy["Shawshank Redemption"]["REZISER"],
                filmy["The Godfather"]["REZISER"],
                filmy["The Dark Knight"]["REZISER"],
                filmy["The Prestige"]["REZISER"]
    }
    print(", ".join(reziseri), oddelovac, sep="\n")
# Doporučí uživateli film(y), které nemá ve svém slovníku
elif vyber in sluzby and vyber == "doporuc film":  
    set_filmy = set(filmy)
    set_uzivatel = set(uzivatele.get(uzivatel))
    print(oddelovac)
    print("Zkus film:", ", ".join(set_filmy.difference(set_uzivatel)), oddelovac, sep="\n")
else:
    print("Neplatná volba, ukončuji program...", oddelovac, sep="\n")


