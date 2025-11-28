import time 

def delay() :
    time.sleep(0.1)
    print('2초 뒤')


print('시작')
for i in range(3) :
    delay()
print('끝')

import threading

print('쓰레드 시작')
for i in range(3) :
    t = threading.Thread(target=delay)
    t.start()
print('쑤레드 끝')

def delay2(x) :
    time.sleep(0.1)
    print(x,'1초 뒤')
for i in range(3) :
    t = threading.Thread(target=delay2, args=(str(i)))
    t.daemon = True
    t.start()

    #json 
    import json 
    j = '''
        {
          "name" : "용군",
          "age"  : "40"
        }

    '''
    d = json.loads(j) # json 형식을 dict 로 바꿔주는 
    print(d,type(d))

    j2 = json.dumps(d)
    print(j2)


    d2 = {
        'hasCar' : True
    }
    j3 = json.dumps(d2)
    print( j3)
    print(json.loads(j3))

    # import requests # 외부 라이브러리
    # requests.get('http://naver.com')
    # print(response)

    import urllib.request as req
    response = req.urlopen('https://naver.com')
    print(response)


    print(response.read().decode("utf-8"))

    import webbrowser
    webbrowser.open_new('https://naver.com')
    webbrowser.open('https://daum.net')