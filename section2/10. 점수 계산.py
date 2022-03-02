import sys
#sys.stdin= open("input.txt","rt")
n= int(input())
a=list(map( int, input().split()))

if a[0]==1:
    score=1
else:
    score=0
    
for i in range( 1, n ):
    if a[i]==0:
       score= score
    else:
        while a[i]==1:
            score=score+1
            i= i-1
            if i<0:
                break

print(score)

'''
for x in a:
if x==1:
    cnt+=1
    sum+=cnt

else:
    cnt=0

print(score)

