import json

aa = {"vards": "Jānis", "uzvards": "Bērziņš", "vecums": 25}
bb = {"vards": "Anna", "uzvards": "Kalniņa", "vecums": 30}
cc = {"vards": "Pēteris", "uzvards": "Ozoliņš", "vecums": 22}


ff = open("darbs_ar_failiem_9a.json", "w", encoding="utf-8")
json.dump([aa, bb, cc], ff, ensure_ascii=False)
ff.close()


ff = open("darbs_ar_failiem_9a.json", "r", encoding="utf-8")
data = json.load(ff)
for person in data:
    print(f"Vārds: {person['vards']}, Uzvārds: {person['uzvards']}, Vecums: {person['vecums']}")
ff.close()