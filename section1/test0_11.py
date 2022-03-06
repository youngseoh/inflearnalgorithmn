#함수 만들기

'''
def add (a,b):
    c=a+b
    print(c)

add(3,2)
'''
'''
def add(a,b):
    c=a+b
    return c #값을 리턴하고 함수 종료

print (add(3,2))

x=add(3,2)
print(x)
'''
'''
def add(a,b):
    c=a+b
    d=a-b
    return c,d

print(add(3,2)) #튜플 자료 구조
'''

#소수 출력하는 함수

def isPrime (x):
    for i in range(2,x):
        if x%i==0:
            return False #함수 종료 
    return True #함수 종료 

a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print( y, end="")


