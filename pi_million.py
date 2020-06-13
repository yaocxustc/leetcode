import re
with open("C://Users//yaocx//Documents//python//pi_million.txt") as file_object:
    lines=file_object.readlines()
stringcontent=''
for line in lines:
    stringcontent += line.strip()
newstring=re.sub(r"([\u4e00-\u9fa5][\u4e00-\u9fa5][\u4e00-\u9fa5][0-9]{1,}[\u4e00-\u9fa5])","",stringcontent)
newstring1=re.sub(r"[|]","",newstring)
newstring2=re.sub(r"\s+",'',newstring1)
#print(newstring2)
mybirthday=input("please input your birthday!")
if mybirthday in newstring2:
    print("your birthday is in pi1000000")
else:
    print("your birthday is not in pi1000000")
num=newstring2.find(mybirthday)
print(num)

