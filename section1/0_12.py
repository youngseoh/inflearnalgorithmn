#람다 함수

'''
def plus_one(x):
    return x+1

print( plus_one(1))
'''

plus_two= lambda x: x+2 # x가 매개 변수, x+2 함수 내용 , plus_two 변수
print(plus_two(1))

def plus_one(x):
    return x+1

a=[1,2,3]
print(list(map(plus_one,a))) # map 함수는 a라는 리스트라는 객체이다가 plus_one 을 모두 작동 시킨다 
print(list(map(lambda x:x+1,a))) #a 라는 리스트가  x에 ㄷ 적용됨 
