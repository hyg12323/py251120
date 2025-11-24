a = [1,2,3,4]
b = a   

print( b )

a[0]  = 10     

print( b )

c = 20
d = c
c = 30
print('d',d )

e = '글씨'
f = e 
e = '글씨2'
print(f)


b = a[:] #깊은복사
b = a.copy() #이것도 리스트한정 깊은복사

a = 10
b = 20

a,b = 10,20
print(a,b)

a = '컵'
b = '볼펜'
### 
a, b  =b, a
print(a, b) # 볼펜,컵