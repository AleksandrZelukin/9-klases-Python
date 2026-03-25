import json

aa = {"name": "Janis", "age": 40, "city": "Rezekne"}
bb = {"name": "Anna", "age": 35, "city": "Riga"}
cc = {"name": "Petrs", "age": 25, "city": "Daugavpils"}
dd = {"name": "Lina", "age": 30, "city": "Liepaja"}
ee = {"pieci": (5,"five"), "desmit": (10,"ten"), "divdesmit": (20,"twenty")}

with open("darbs_ar_failiem_9c.json", "w", encoding="utf-8") as f:
    json.dump([aa, bb, cc, dd, ee], f)
    
with open("darbs_ar_failiem_9c.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)

f.close()