from Deque import Deque

def palchecker(aString):
    chardeque=Deque()

    for i in aString:
        chardeque.addRear(i)

    stillEqual=True

    while chardeque.size()>1 and stillEqual:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            stillEqual=False

    return stillEqual

print(palchecker("我爱我"))
print(palchecker("what are you doing ?"))