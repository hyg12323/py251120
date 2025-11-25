test_list = ['a','b','c']
for letter in test_list :
    print(letter)

for letter in 'hello' :
    print(letter)
print(letter)

d = {
    'a': 'aa',
    'b': 'bb',
    'c': 'cc',
}
# 딗셔너리는 key로 반복 가능
for key in d :
    print(key)

d.keys()
d.values()
d.items()
    # for (k, v) in d.items()
for k, v in d.items() :
         print('k :',k,'v:',v)

r = range(5)
print('range(5) :',r)
r = range(0,5)
print('range(0,5) :',r)
print(list(r))
# range (시작숫자, 종료숫자-1, 건너뛰기)

for i in range(0,5) :
     print(i)

print('-'*20)
for i in range(2,5) :
     print(i)

print('-'*20)
for i in range(2, 10, 3) :
     print(i)

print('-'*20)
for i in range(10,2,-1) :
     print(i)

print('-'*20)
j = 0
for i in range(1,101) :
   j = j+i 
print(j)

for i in range(1,10) :
     for c in range(1,10) :
          print(i,'x',c,'=',i*c)
# 1~100까지 3또는 5의 배수는 제외하고 모두 더하기
print('-'*20)
result = 0
for i in range(1,101) :
     if (i % 3 == 0) or (i % 5 == 0) :
          continue
     result += i 
     print(result)

  
arr = [51,52,53,54,55]
idx = 0
for value in arr :
     print(idx, value)
     idx += 1
     
# for i in range(1,100,5):
#      print(i)
print('-'*20)
for i in range(len(arr)) :
     print(i, arr[i])


for i in range(5) :
     print(i, end='\n') 


a1 = 9
for i in range(1,10) :
     for c in range(1,10) :
          print(i,'x',c,'=',i*c,end='/  ')
          if(c == a1) : 
               print( i,'단')
               print()
          
print('#' * 20)   
################################
# 리스트 컴프리헨션 comprehension

for i in range(1,10) :
    print(i)

    '''
        리스트 선언 a
        반복 1~9 만큼
            a에 하나씩 추가
        a 출력해서 확인
    '''
# 1,2,...,9 값을 가지는 리스트를 쉽게 만들어보자
a = []
for i in range(1,10) :
    a.append(i)
print(a)
print('-' * 20)
a = [i for i in range(1,10)]       
print(a)

# 17의 배수 5개
b = []

for i in range(1,6) :
    b.append(17 * i)
    
b = [(17 * i) for  i in range(1,6)]

for i in range(17,17*5+1,17) :
    b.append(i)
    
b = [i for i in range(17, (17*5)+1, 17)] # 느낌점 : 뭔가 합리적인듯 하지만 마음이 편치 않음
print(b)



print('-' * 20)
c = []
for i in range(1, 10) :
    if i % 3 == 0 :
     c.append(i)

for i in range(3, 10, 3) :
     c.append(i)
     
c = [i for i in range(1, 10) if i % 3 == 0 ]

print(c)

c = []
for i in range(1, 10) :
    if i % 3 == 0 or i % 5 ==0 :
     c.append(i)

# c = [ i for i in range(1, 10) if  i % 3 == 0 or i % 5 ==0 :]

# 1~9까지에서
# 홀수는 그대로
# 짝수는 2배 인 배열을 만들자

print('-' * 20) 

c = []
for i in range(1, 10) :
 if (i % 2 == 0) :
    c.append(i * 2)
else :
    c.append(i)

c = [i*2 if i % 2 == 0 else i for i in range(1, 10) ]
print(c)


print('-' * 20) 
## 구구단
d = []
for i in range(2, 10) :
    for j in range(1, 10) :
        d.append(f'({i}x{j}={i*j})')
        print(d)

#안쪽부터
e = [ [ f'{i}x{j}={i*j}' for j in range(1, 10) for i in range(2, 10) ] ]

# 이건 의도와 다르게 2차원 배열이 된다
print('--- e ---')
print(e)

#그렇다면 
f = [ f'{i}x{j}={i*j}' for i in range(2, 10) for j in range(1, 10)]

print('-' * 20) 
print(f)

# 딕셔너리 컴프리헨션
a = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 16,
}
a = {}
for i in range(5) :
   if i%2 == 0 :
     a[i] = 1 ** 2      

a = { i:i**2 for i in range(5) }
print(a)

print('-' * 20) 
a = [11,12,13,14]
for i, data in  enumerate(a) :
     print(i, data)

print('-' * 20) 
for i, data in enumerate(a, 2) :
     print(i, data)

a = [10,20,30]
b = [7,8,9]
c = zip(a, b)
print(c)
d = list(zip(a, b))
print(d)

lang = 'kor'
kr = ['소개','채용']
en = ['About','Recruit']
a1 = list(zip(kr, en))
print(a1)


if lang == 'kor' :
    print(kr[0])
elif lang == 'Eng' :
     print(en[0])



i18n = []
if lang == 'kor' :
    i18n = kr
elif lang == 'Eng' :
      i18n = en


html = f'''
       <span>소개</span> <span>채용</span>
'''

d_kr = {
    'comon.header.about' : '소개'
}

d_en = {
    'comon.header.about' : 'about'
}

il8n = d_kr

# if를 통해서
html = f'''
       <span>{il8n['comon.header.about']}</span>
'''

'''
문제 1 
1~n 까지 짝수의 합을 구하기
문제 2 
1~n 까지 숫자를 3개씩 옆으로 찍기
문제 3 
+++*---
++***--
+*****-
문제4
주사위 2개를 굴려서 중복을 제거한 경우의 수 
문제5
키오스크 처럼
'1: 아아, 2:라떼, x: 종료
'x'가 입력되기 전까지 무한 반복
'''

f1 = 0 
for i in range(1,21) :
    if i%2 == 0 :
       f1 += i
       print(f1)
 
print('--' )
for i in range(1, 10,3) :
 if (i == i*3) :
    print()
    print(i)

print('ㅡㅡㅡㅡㅡㅡㅡㅡ')
# a1 = 1
for i in range(1,10) :
          # f = 3%0 == i
          print(i,end='')
          if(i%3 == 0) : 
               print()
          # print(i,end='')

print('ㅡㅡㅡㅡㅡㅡㅡㅡ')
a = '+'
b = '*'
c = '-'
for i in range(1,2) :

      print(a*3+b*1+c*3)
      print(a*2+b*3+c*2)
      print(a*1+b*5+c*1)
      print(b*7)
      c= 5

n = 4
for i in range(i,n+1) :
         print(i)
     #     for e in range(1,6) :
          #    print('+')
     #     for i in range(1,4) :
          #  print(i,end='')
          
# if(i%3 == 0) :







n = 4
for i in range(i,n+1) :
    print('+'*(n-i), end ='')
print()


#     for c in range(1,6) :
          # print(i,end='')
              
          #     print(a*2) 
#     print(a)

    

 
for i in range(1, 6+1) :
    for j in range(i, 6+1) :
        print(f'[{i},{j}]',end ='')
    print()

c = 9
for i in range(1,c+1) :
         print()
     #     for e in range()
         print('+'*(c-i)+'*'*(i*2-1)+'-'*(c-i),end='')
# 문제4
# 주사위 2개를 굴려서 중복을 제거한 경우의 수 


for i in range(1,6+1) :
    for e in range(i,6+1) :
     print(f'[{i},{e}]',end='')
print()


# 문제5
# 키오스크 처럼
# '1: 아아, 2:라떼, x: 종료
# 'x'가 입력되기 전까지 무한 반복
# '''