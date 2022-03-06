#리스트와 내장함수

a=[23,12,36,53,19]
print(a[:3]) #slice 기능 (0부터 2까지)
print(a[1:4])
print(len(a))#리스트에 몇개의 값이 있는지

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=" ")
print()

for x in a:
    if x%2==1:
        print(x, end='')
print()




# 인덱스 번호와 value값으로 묶어서 () 출력함 -> 튜플이라는 자료구조
#[]리스트 ()튜플: 안의 값 변경 불가
for x in enumerate(a):
    print(x)
b=(1,2,3,4,5)
print(b[0])
# b[0]=7 -> 변경불가


for x in enumerate(a):
    print(x[0],x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()





# 60>x 가 모두 참이면 true, 하나라도 거짓이면 false -> all
if all(60>x for x in a):
    print("YES")
else:
    print("NO")

#하나라도 참이면 true, 모두 거짓이면 false ->any
if any(11>x for x in a):
    print("YES")
else:
    print("NO")


    
