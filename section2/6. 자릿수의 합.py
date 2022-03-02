import sys
#sys.stdin= open("input.txt","rt")
n= int(input())
a=list(map(int, input().split()))
b=0
def digit_sum(x):
    if x<10:
        return x
    else:
        return (x%10)+ digit_sum(x//10)

for i in range(n):
    if digit_sum(a[i])>b:
        b=digit_sum(a[i])
        res=a[i]

print(res) 
