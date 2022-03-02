import sys
#sys.stdin= open("input.txt","rt")
n= int(input())
'''
a=[]
b=0
for i in range (2, n+1):
    for j in range(2, i):
        if i%j==0:
            b=1
    if b==0:
        a.append(i)
    b=0
            
print(len(a))
'''

ch=[0]*(n+1)
print(ch)
cnt =0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1,i):
            ch[j]=1
print(cnt)
