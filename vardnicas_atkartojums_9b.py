talruna_gramata = {}
print("Vārdu un tālruņu ievades programma:")
while True:
    izvelne = input("""
============================================
        1 - Ievadīt jaunu ierakstu
        2 - Parādīt visus ierakstus
        3 - Beigt darbu
============================================
          \n""")
    if izvelne == "1":
        vards = input("Ievadiet vārdu: ")
        numurs = input("Ievadiet tālruņu numuru: ")
        f = open("talruna_gramata_9b.txt", "a", encoding="utf-8")
        f.write(f"{vards}: {numurs}\n")
        f.close()
        talruna_gramata[vards] = numurs
    elif izvelne == "2":
        f = open("talruna_gramata_9b.txt", "r", encoding="utf-8")
        print(f.read())
        f.close()
    elif izvelne == "3":
        for key in talruna_gramata:
            print(key, talruna_gramata[key])
        break