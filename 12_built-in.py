# 내장 함수
# 정수를 문자 하나로 형 변환
# chr(65) #캐릭터타입
print('chr(65) :',chr(65) )
# 문자 하나를 아스키 또는 유니코드로 변환
print("ord('A') :", ord('A') )
print("ord('z') :", ord('Z') )
print("ord('한') :", ord('한') )

print("int('123') :", int('123')) #문자를 숫자로 바꿔줌

print("int('f',16) :", int('f',16)) #문자를 숫자로바꿔줌 16진수로 

print("int('f',16) :", int('1010',2)) #문자를 숫자로바꿔줌 2진수로


# 함수를이용해서 배열에 있는숫자 전부 적용시켜줌
def pp(x) :
    return x +1
n = [1,2,3,4]
a = map(pp,n)
print('a :',a)
print('list(a) :',list(a) )

def key(x) :
    print(x)
d = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
# c = dict(map(key, d))
# print(c)

def over3(x) :
    return x >=3
b = filter(over3, n)
print('b', b)
print('list(b)',list(b))

print( format(1234, ',') )

print ('max(n)',max(n))
print ('min(n)',min(n))

income = -100
print(str(income)+'원 입금 되었습니다')
if income < 0 : 
    income = 0
print(str(income)+'원 입금 되었습니다')
# print(max ([ income,0] )+ '원 입금 되었습니다')

users = [
    {
        'id' : 'a',
        'level' : 12
    },
    {
        'id' : 'b',
        'level' : 20
    }
]
def get_level(user) :
    return user['level']
print( max(users, key=get_level))
print( max(users, key=lambda data : data['level']))

print('sum(n)', sum(n) )

print( sorted(n, reverse=True))
print('-'*20)
print( sorted(n))
n.sort()
print(n)

print(list(reversed(n)))