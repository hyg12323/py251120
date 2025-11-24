a = 'abc'
print(type(a))

print(1,a.strip())


a =[] # 배열로 만들겠다
a =list() #이것도 가능
print(type(a))
#print(2,a.strip())

a = [1,2,3]
print(a)
print(a[-1])

a = [1,2,3,[1,2,3]]
print(a[3])


# 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])

b = 'abcde'
print(b[1:4])

print(a[:2])
print(a[1:])
print(a[1:100])

c = [1,2,3,4,5,6,7,8,9]
print(c[5:2])  #에러안남 조심해야함


# c[0:2] = 2
print(c[:])

a = a + c
a += c

a = a * 3
a *= 3

a = [1,2,3]
del a[1]
print(a)

b = [1,2,3,4,5]
del b[1:4]
print(b)
c = [1,2,3]
c.append(40) # 마지막에 추가
print(c)
c.append([100, 200])
print(c)

d = [78,3,4,6,31]  
d.sort() # 오름차순 정렬하기 
print(d)

d.reverse()
print(d)

# e = 'diwohwef'
# list(e.split()).sort()
# # e.sort()
# print(e)

list1 = d.sort()
print(list1)

e = [1,2,3,4,6]
print( e.index(3) ) # 몇번째 있는지 
# print(e.index(30))
# print(e.find(3))

print(3 in e)  # 3이 있는지 없는지 확인

e.insert(2,50) # 원하는곳에 끼워넣을수 있다
print(e)


# print(e.index(50)) # 없으면 에러

f = [1,2,3,4,3]
f.remove(3) # 왼쪽부터 해당 값 하나만 삭제
# f.remove(32) #없으면 에러 
print(f)

g = [1,2,3,4]
h = g.pop() #마지막꺼 꺼내오기 및 지우기
print(h,g)

i = [1,2,3,3]
j = i.count(3) # 3이 몇개인지 새주는거 

print( j )

i.extend([10,20]) # 마지막에 값 더해줌
print(i)
i +=[100,200] # 
print(i)

# i.sort().reverse()
