# json이랑 동일 딕셔너리 타입
a= {}
a= dict()
print (type(a))

b = {
    '이름':'하용군',
    '주소': '천안',
    '오늘': 21,
    '스킬': {
        'java':'상',
        'python':'하'
    }
}
print(b)
print(b['이름'])

# print(b[나이]) # key가 없으면 에러
b['나이'] = 20  # 추가할대 이렇게 쓸수있다
print(b)

c = {
    1 :'일',
    2 :'이'
}
print(c[1])
 
del c[1]
print(c)

# 슬라이싱 불가

d = {
    '이름': '용군',
    '이름': '하용군'
}
print(d) # 키가 중복이면 덮어씀


e = b.keys()
print(e)

print(b.values())

print(b.items())  # key랑 value가 tuple로 나옴

d.clear()
print(d)
d ={}

print(b.get('이름') )  
print(b['이름'] )     # 둘다 똑같은데
print(b.get('이름2') ) #있는지 애매할데 쓰는거 나쁘지않음

print(b.get('이름','값없음') ) #값이 있으면 이름뜸
print(b.get('이름2','값없음') ) #값이 없으면 값없음뜸

print ('이름'in b )  #in은 key가 있는지 여부를 판단 


e = b.pop('이름') # 이름만 불러오고 원본에서 삭제
print(e,b)