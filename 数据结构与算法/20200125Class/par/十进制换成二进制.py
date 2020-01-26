from Stack import *

"""
def deToEr(n):
    arr=Stack()
    cnt=int(n)
    while(cnt):
        arr.push(int(cnt%2))
        cnt=cnt/2
    result=0
    while(arr.size()!=0):
        result=result*10+arr.pop()
        print(result)
    print("十进制："+str(n)+"转换成"+str(2)+"进制为："+str(result))

deToEr(11)
"""

def divideBy2(decNumber):
    remstack=Stack()

    while decNumber>0:
        rem=decNumber %2
        remstack.push(rem)
        decNumber=decNumber//2

    binString=""
    while not remstack.isEmpty():
        n=remstack.pop()
        binString=binString+str(n)
        print(n)
    return  binString

print(divideBy2(11))

