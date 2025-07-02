numbers=[
    {'value':2},
    {'value':3},
    {'value':4}
]

natija=[]

for element in numbers:
    qiymat=element['value']
    kvadrat=qiymat**2
    natija.append({'value':kvadrat})

print(natija)