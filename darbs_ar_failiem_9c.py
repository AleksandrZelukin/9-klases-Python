aa = open("darbs_ar_failiem_9c.txt", "a", encoding="utf-8")
# aa.write("Sveiki, šis ir mans trešais darbs ar failiem Pythonā!")
aa = print("Sveiki, šis ir mans trešais darbs ar failiem Pythonā!", file=aa)
# aa.close()


aa = open("darbs_ar_failiem_9c.txt", "r", encoding="utf-8")
content = aa.read()
print(content)
aa.close()