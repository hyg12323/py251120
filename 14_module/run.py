import mod1

print(mod1.add(1,2)) 

from mod1 import add, sub
print(add(1,2))
print(sub(3,2))


import sys
print(sys.path) # 모듈을 가져오는 경로 확인
print('_'*20)
print( sys.modules.keys() ) # 지금 import 없이 사용가능  모듈 목록
print( 'traceback' in sys.modules.keys() ) 
print('_'*20)

import folder.calc # 전체 경로
folder.calc.add()

import folder.calc 
folder.calc.add()


from folder.calc import add
add()


import folder.calc as fc 
fc.add()

from folder import calc #파일 
calc.add()


