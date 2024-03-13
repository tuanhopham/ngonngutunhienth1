import re
with open("th2/data.txt", "r",encoding="utf-8") as f:
    string = f.read()
#ý 1
    result1= re.sub('[^A-Za-z0-9À-ỹ ]+', '', string)
print("result1",result1)
#ý 2
result2 = result1.lower()
print("result2",result2)
# y4 
result4 = result2.split()
#y3 
with open("th2/vietnamese-stopwords.txt", "r",encoding="utf-8") as sw:
    stopword = sw.read().splitlines()
result3 = ' '.join([word for word in result4 if word not in stopword])
print("result3",result3)
print("result4",result4)
# y5
result5 = [word for word in result4 if len(word) > 1]
print("result5",result5)