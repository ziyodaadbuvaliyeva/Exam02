def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide (a,b):
    if b==0:
        return "0ga bolish mumkin emas!"
        return a/bolish

son1=8
amal="*"
son2=5

if amal=="+":
     natija=add(son1,son2)
elif amal=="-":
    natija=subtract(son1,son2)
elif amal=="*":
    natija=multiply(son1,son2)
elif amal=="/":
    natija=divide(son1,son2)
else:
    natija="notogri amal kiritilgan!"

print('natija:',natija)




