from Stack import *

def divibeByany(decNumber,numCnt):
    arr=Stack()
    n=decNumber
    while decNumber > 0:
        n=decNumber % numCnt
        arr.push(n)
        decNumber//=2

    binString= ""
    while not arr.isEmpty():
        binString+=str(arr.pop())

    print("十进制的数{}转换成{}进制的数为：{}".format(n,numCnt,binString))

divibeByany(11,8)