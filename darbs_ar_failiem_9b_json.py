import json
aa = {"vards": "Jānis", "uzvards": "Bērziņš"}
bb = {"vards": "Anna", "uzvards": "Kalniņa"}
cc = {"vards": "Pēteris", "uzvards": "Ozoliņš"}
dd = {"vards": "Līga", "uzvards": "Liepiņa"}


with open("darbs_ar_failiem_9b.json", "w", encoding="utf-8") as f:
    json.dump([aa, bb, cc, dd], f)
    
with open("darbs_ar_failiem_9b.json", "r", encoding="utf-8") as f:
    dati = json.load(f)
    for ieraksts in dati:
        print(ieraksts["vards"], ieraksts["uzvards"])