import csv

with open('input/grades.csv', 'r') as
 fayl:
    oquvchi=csv.reader(fayl)
    next(oquvchi)
    beshlar_soni=sum(1 for qator in
     oquvchi if qator[-1]=='5')

with open('Output/output16.txt',"w")as
chiqish:
    chiqish.write(f"5 baho olganlar soni:{beshlar_soni}")