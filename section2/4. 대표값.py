import sys
#sys.stdin= open("input.txt","rt")
N=int(input())
s=list(map(int, input().split()))
ave=round(sum(s)/N)

listMin=float('inf')

for idx,x in enumerate(s):# idx 에는 인덱스 번호 x 에는 값
    tmp=abs(x-ave)
    if tmp<listMin:
        listMin=tmp
        score=x
        res=idx+1
        
    elif tmp==listMin:
            if x>score:
                score=x
                res= idx+1
        
    

print(ave, res)
