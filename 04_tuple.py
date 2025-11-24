a = ()
g = [1,2,3,4]
a = tuple(g) #리스트를 형변환 가능 튜플로
print (type(a))



b = (1,2,3)  #tuple 값이 절대변하지않는 리스트
print(b)
print(b[0])

# b[0] = 5 값바꾸기는 불가능

c = (1,) # 단 하나의 값을 가지는 튜플의 경우 (값,)로 선언해야 한다

d = 1,2,3,4,5
print(type(d)) #튜플타입 가로 생략가능

len(d) # 개수새주는거
print(len(d))
