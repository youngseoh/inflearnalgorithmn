# 문자열과 내장함수
msg="It is Time"
print(msg.upper())# 모든 문자를 대문자로 해서 만듬
print(msg.lower())# 모든 문자를 소문자로 해서 만듬
print(msg)
tmp=msg.upper()
print(tmp)
print(tmp.find('T'))# T를 찾아서 인덱스로 나타냄(띄어쓰기도 포함)
print(tmp.count('T'))# T가 몇개인지 찾는 것
print(msg[:2]) #처음부터 2번전까지
print(msg[3:5])#3과 4만 출력


print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=" ")
print()

for x in msg:
    print(x, end=" ")
print()

for x in msg:
    if x.isupper():#x가 대문자이면 참을 리턴
        print( x, end=" ")
print()

for x in msg:
    if x.isalpha():#공백없이 알파벳말 출력
        print(x, end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x))# 아스키 넘버를 출력해줌

tmp='az'
for x in tmp:
    print(ord(x))# 아스키 넘버를 출력해줌

tmp=65
print(chr(tmp))# 대응되는 문자를 출력해줌


