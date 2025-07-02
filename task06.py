students={'Ali':5,'Vali':4,'Hasan':5,'Husan':3}

baho=list(students.values())
ortacha=sum(baho)/len(baho)

for ism in students:
    if students[ism]>ortacha:
        print(ism)

print('ortacha baho:',ortacha)