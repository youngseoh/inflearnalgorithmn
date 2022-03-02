import sys
#sys.stdin= open("input.txt","rt")
T= int(input())
for t in range (1, T+1):
    n,s,e,k= map( int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t, a[k-1]))
    
