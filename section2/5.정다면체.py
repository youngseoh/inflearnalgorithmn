import sys
#sys.stdin= open("input.txt","rt")
'''
a=[]
N,M=map(int, input().split())
for i in range(1,M+1):
    for j in range(1,N+1):
        k=i+j
        a.append(k)
        a.sort()
        
print(a)
'''

N,M=map(int, input().split())
a=[0]*(N+M+1)
for i in range(1,M+1):
    for j in range(1,N+1):
        k=i+j
        a[k]=a[k]+1
max=0
for i in range(N+M+1):
    if a[i]>=max:
        max=a[i]
        

for i in range(N+M+1):
    if a[i]==max:
        print(i, end="")
