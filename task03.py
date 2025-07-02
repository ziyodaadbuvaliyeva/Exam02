def calculate_tax(salary):

    if salary>5_000_000:
        tax=salary*0.20
    else:
        tax=salary*0.13
    return tax

def calculate_sof_maosh(salary):

    tax=calculate_tax(salary)
    sof_maosh=salary-tax
    return sof_maosh

maosh=6_000_000
soliq=int(calculate_tax(maosh))
sof_maosh=int(calculate_sof_maosh(maosh))

print('kiritilgan maosh:',maosh)
print('soliq:,soliq')
print('sof maosh:',sof_maosh)