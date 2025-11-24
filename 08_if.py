a = 10
b = 5 < a < 20
print(b)

# if 와 else 차이
# 만족하면 그만돌아감
# if score >= 90 :
#     print('A')
# elif 80 <= score and score < 90 :
#     print('B')
# elif 70 <= score < 80 :
#     print('C')
# else :
#     print('F')   


# # 계속 돌아감
# if score >= 90 :
#     print('A')
# if 80 <= score and score < 90 :
#     print('B')
# if 70 <= score < 80 :
#     print('C')
# else :
#     print('F')   


if True :
    print(1) #들여쓰기 -INTENT
    print(2)
if False : 
       print(3)
else : 
    pass  #아무것도 없으면 안됨

if a < 5 :
    print(1)
elif a :
    print(2)
else :
    print(3)  
if not(a > 3 ) :
    print(a)

a = True
b = False
if a and b :
    print('and')
elif a or b :
    print('or')   
c = False

if not c :
    print('false')

if 1 != 0 :
    print('같지않다')

money = 2000 
#만약에 money가 3000 이상이면 "택시타자" 출력
#그렇지 않으면 "걸어가자" 출력

if money >= 3000 :
    print('택시타자')
else :
    print('걸어가자')

card = False
# 3000원 이상이거나 카드가 있다면 택시타자

if money >= 3000 or card == True :
    print("택시타자")
else :
    print('걸어가자')

# 24일에 출석한 학생 명부
student_24 = ['상명','민서','우영','용군','덕인']
# 24일에 '동현'이 있다면 복습 출력 
#없다면 '진도나감'출력

if '동현' in student_24  :
    print('복습')
else :
    print('진도나감')

money = -100
if money < 0 :
    money = 0

if money < 0 : money = 0

score = input()
print('>>>',score)

# score = input('정수를 입력하세요:')
# print('>>>',score, type(score))

# 정수에 따라
# 90 이상이면 'A'
# 80 이상, 90미만이면 'B'
# 70 이상, 80미만이면 'C'
#그 외 'F' 출력

# if '90' <= score :
#     print('A',score) 
# elif '80' <= score :
#     print('B',score) 
# elif '70' <= score :
#     print('C',score)
# else : 
#     print('F') 

score = int(score)

if  90 <= score  :
    print('A')
elif 80 <= score and score < 90 :
    print('B')
elif 70 <= score < 80 :
    print('C')
else :
    print('F')   

# else가 있다는건 하나 이상은 꼭 실행된다
if 60 <= score :
    result = '합격'
else : 
    result = '불합격' 
print(result)
# 위 코드는 아래와 같이 많이 쓴다
result = '불합격'
if 60 <= score :
  result = '합격'
print(result)

#한줄로 코드
result = '합격' if score >= 60 else '불합격'



# # 24일에 출석한 학생 명부
# student_24 = ['상명','민서','우영','용군','덕인']
# # 24일에 '동현'이 있다면 복습 출력 
# #없다면 '진도나감'출력

# if '동현' in student_24  :
#     print('복습')
# else :
#     print('진도나감')


result = '복습' if '동현' in student_24 else '진도나감'
print(result)


result = 123 if 10 < 20 else '바보'
print(result)

'''
if  90 <= score  :
    print('A')
elif 80 <= score and score < 90 :
    print('B')
elif 70 <= score < 80 :
    print('C')
else :
    print('F')   
'''

# 다른 두방식
result = 'A' if 90 <= score else 'B' if 80 <= score and score < 90 else 'C' if 70<= score < 80 else 'F'
print(result)

# result = (
#     'A' if() 90 <= score else
#     'B' if 90 <= score and score < 90 else
#     'C' if 90 <= score <80 else
# )
print(result)

# 입력 받은 월에 해당하는 계절 출력하기
# score = input('정수를 입력하세요:')
score = int(score)
if 3 < score and 6 >score:
    print('봄')
elif 6 < score  and 9 > score:
    print('여름')
elif 9 < score  and 12 > score :
    print('가을')
else :
    print ('겨울')


# 가위바위보 게임 만들기 
# # '가위' '바위' '보' 입력
# 컴퓨터는 항상 '바위'만 낸다
# '졌다', '비겼다, '이겼다' 출력


result = '바위'
score = input('가위바위보게임 :')
if '보' == score :
 print(result,'이김')
elif '바위' == score :
 print(result,'비김')
else : 
 print(result,'짐')


 # 입력받은 값이 '홀수'인지 '짝수'인지 출력
 # 단 조건부 표현식 사용
 num = input('숫자입력 :')
 num = int(num)
 result = '홀수' if num % 2 !=0 else '짝수'
 print(result)

 # a, b중에 큰 값 출력하기
 # 같은 경우 '같다' 출력
 
 
 a = 10
 b = 10
#  score = input('수를 입력하세요 :')
if a < b :
     print(b)
elif a > b :
     print(a) 
else :
    print('같다')

match game :
   case '가위' :
        print('짐')
   case '바위' :
        print('비김')
   case '보' :
        print('이김')
                
