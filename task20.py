students=[
    {'name':'Ali','age':18},
    {'name':'Jasurbek','age':20},
    {'name':'Diyor','age':19},
    {'name':'Muhammad','age':21}
]
eng_qisqa=min(students,key=lambda x:
len(x['name']))
print(eng_qisqa['name'])