import sys
#sys.stdin= open("input.txt","rt")
N,K= map(int, input().split())
a=list(map(int, input().split()))
b=[]
for i in range(0,N):
    for j in range(0,N):
        for k in range(0,N):
            if i<j:
                if j<k:
                     c=a[i]+a[j]+a[k]
                     b.append(c)
                
            
b.sort()
print(b[-K])

'''
res= set() # 중복을 제거하는 자료구조 set()
for i in range (n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res= list(res)
res.sort(reverse=True)
print(res[K-1])
'''
