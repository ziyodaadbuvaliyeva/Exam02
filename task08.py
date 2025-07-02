a=open('input/numbers.txt')
nums=[int(i)for i in a]
a.close

b=open('output/output08.txt',"w")
b.write(f"yigindi:{sum(nums)}\n")
for i in nums:
    b.write(f"{i}\n")
b.close()
