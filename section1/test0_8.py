#리스트와 내장함수
import random as r
a=[]
#print(a)
b=list()
#print(b)


a=[1,2,3,4,5]
#print(a)
#print(a[0])

b=list(range(1,11))
#print(b)

c= a+b
#print(c)

a.append(6)#추가하기
print(a)

a.insert(3,7) # 3번인덱스에 7이 틀어간다
print(a)

a.pop() #맨뒤에있는 것을 없앤다
print(a)

a.pop(3)#3번 인덱스에 있는 값을 제거한다
print(a)

a.remove(4)#'4'의 값을 제거한다
print(a)

print(a.index(5))#'5'라는 값이 인덱스 번호

a= list(range(1,11))
print(a)
print(sum(a))#a에 있는list의 값을 합해준다
print(max(a))#a에 있는list의 값중 가장 큰 값
print(min(a))
print(min(7,5))#인자들 중에서 최솟값->5



r.shuffle(a)#a를 섞어라
print(a)
a.sort()# 오름차순
print(a)
a.sort(reverse=True)#내림차순
print(a)
a.clear()#모든 값 삭제->빈리스트
print(a)

