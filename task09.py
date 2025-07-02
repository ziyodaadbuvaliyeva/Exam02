f=open('input/numbers.txt')
sonlar=[int(x)for x in f]
f.close()

max_son=max(sonlar)

f=open('Output/output09.txt','w')
f.write(f'Eng katta son:{max_son}\n')
for son in sonlar:
    f.write(f'{son}\n')
f.close()