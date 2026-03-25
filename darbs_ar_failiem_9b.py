aa = open("darbs_ar_failiem_9b.txt", "a", encoding="utf-8")
aa.write("Trešais teksts\n")
aa.close()

aa = open("darbs_ar_failiem_9b.txt", "r", encoding="utf-8")
print(aa.read())
aa.close()