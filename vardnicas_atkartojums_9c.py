talruna_gramata = {}
print("Vārdu un numuru ievade:")
# print("Lai pabeigtu ievadi, ierakstiet 'stop' kā vārdu.")
while True:
    print("""Ko gribam darīt? 
          1 - Ievadīt jaunu ierakstu, 
          2 - Skatīt visus ierakstus, 
          3 - dzest ierakstu,
          4 - iziet no programmas""")
    izvelne = input("Izvēlieties darbību (1/2/3/4): ")
    if izvelne == "1":
        while True:
            vards = input("Ievadiet vārdu: ")
            # if vards == "stop":
            #     break
            numurs = input("Ievadiet numuru: ")
            talruna_gramata[vards] = numurs
            print(f"Ieraksts '{vards}: {numurs}' ir pievienots.")
            f = open("talruna_gramata.txt", "a", encoding="utf-8")
            f.write(f"{vards}: {numurs}\n")
            f.close()
            izvelne = input("Ja vēlaties ievadīt vēl vienu ierakstu? (1 - Jā, 2 - Skatīt visus ierakstus un talak): ")
            if izvelne != "1":
                break
    if izvelne == "2":
        # for key in talruna_gramata:
        #     print(key, talruna_gramata[key])
        # for vards, numurs in talruna_gramata.items():
        #     print(f"{vards}: {numurs}")
        f = open("talruna_gramata.txt", "r", encoding="utf-8")
        print(f.read())
        f.close()

    if izvelne == "3":
        vards = input("Ievadiet vārdu, kuru dzēst: ")
        if vards in talruna_gramata:
            del talruna_gramata[vards]
    if izvelne == "4":
        print("Programma beidz darbību.")
        break