print("hello")
print('world')

#print("wor
# ld") 엔터 안됨 

print("""wor
ld""") #띄어쓰기 가능하게만듬

"그냥 글씨"


'''
아무거나 
여러줄 주석
'''


print("나는 \"하용군\" 입니다")

print('''
   글씨1
   글씨2
   글씨3
''')
print('''
   글씨1\
   글\t씨2
   글\n씨3
''')

print(1,"2",'3')

print('처음'+'다음')

#print(1 + '글씨') 숫자글씨는 더할수없다
#print(1+"2") x
# ''+123 x
print( str(1)+ '글씨')
#print('문자'+1) 문자 글씨도 똑같음


print('-' *30)


a = 'abcde'
print(a, len(a) )

a = 14
b = "지금 기온은 " + str(a) +"도 입니다"
print(b)

c = f"지금 기온은 {a}도 입니다"  # formeting 의 약자
print(c)


d = f'''
<div>
    지금 기온은    <span> {a} </span>도 입니다
</div>
'''
print(d)


e = '지금 기온은 %d도 입니다' % -3.14 # %d 정수(버림)
print(e)

print('%2x' % 10)

f = '오늘: {0}일, 내일: {1}일'.format(20, 21)
print(f)


a = 'hobby'
print ( a.count('b'))  # 몇번 들어가있는지 세줌


print(a.find('b')) # 최초로 만나는 index 반환
print(a.find('x')) # 없으면 -1 이다
# index()도 비슷한데 없으면 에러


b = 'abcd'
c = ':'
d = c.join(b)
print(d)
#print(join(b)) 그냥은 못씀

a = '    a bc    '
print(a.strip())

b= a.replace('b','!')
print(b)

a = "Life is too short"
b = a.split(' ')
c = a.split()
print(a, b, c)
d= a.split('i')
print(d)

a = 'https://namer.com'
print(a.startswith('https'))
print(a.endswith('.net'))