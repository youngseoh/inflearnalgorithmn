# 1)
n= input() #문자형 
for i in range(1, int(n)+1):
    if i%2==1:
        print(i)

#2)
n= input()
i=0
for k in range(1, int(n)+1):
    i=i+k

print(i)


#3)
n= input()
for m in range(1, int(n)+1):
    if int(n)%m==0:
        print(m, end=" ")

'''
n= int (input())
'''
