f=open('input/numbers.txt','r')
nums=[int(i.strip())for i in f]
f.close()

nums.sort()

f=open('output/output10.txt','w')
for i in nums:
    f.write(str(i)+'\n')
    
f.close