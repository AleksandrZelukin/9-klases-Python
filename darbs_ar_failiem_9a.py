aa = open("darbs_ar_failiem_9a.txt", "a",encoding="utf-8")
aa.write("Sveiki, šis ir mans tre'sais darbs ar failiem!\n")
aa.close()

aa = open("darbs_ar_failiem_9a.txt", "r",encoding="utf-8")
print(aa.read())
aa.close()