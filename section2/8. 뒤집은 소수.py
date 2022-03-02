import sys
#sys.stdin= open("input.txt","rt")
n= int(input())
a=list(map(int,input().split()))
b=[]

def reverse(x):
    re=0
    while x>0:
        t=x%10
        re=re*10+t
        x=x//10
    return re
   



def isPrime(x):
    if x==1:
        return False
    for i in range (2,x):
        if x%i==0:
            return False
    return True




for i in range(n):
    res=reverse(a[i])
    b.append(res)
for i in range(n):
    ress=isPrime(b[i])
    if ress==True:
            print(b[i])
