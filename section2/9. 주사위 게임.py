import sys
#sys.stdin= open("input.txt","rt")
n= int(input())
res=0
for i in range(n):
    tmp= input().split()
    tmp.sort()
    a,b,c= map(int, tmp)
    if a==b and b==c:
        money= 10000+1000*a
    elif a==b or b==c:
        money= 1000+100*b
    else:
        money= c*100
    if money>res:
        res= money

print(res)
