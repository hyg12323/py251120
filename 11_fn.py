
def add(x,y) :
    z = x + y 
    return z
a= add(1,2)
print(a)

def sub(x, y) :
    return x- y
a =sub(1,2)
print(a) # -1
b = sub(y =2, x =1)
print(b)

# c = sub(1,2,3)
# c = sub(1)

print(1,2,3,4)

def add_many(*a) :
    print(type(a),a)
    for data in a :
        print(data) 

add_many(1,2)
add_many()

def menu(pizza, *topping) : # 가변인지는 특성상 가장 마지막에 한번 밖에 못 옴
    print(pizza, topping)
menu('슈프림','버섯','옥수수')

def make_dict(**kwargs ) :
    # make_dict(10) # **로 받을 때는 key = value 형태만 가능
    print(type(kwargs),kwargs )

make_dict(x=5)
make_dict(x=5,y=10)
make_dict(key ='value')
make_dict()

def test_complex(*a, **b) :
    print('a',a)
    print('b',b)
test_complex(1,2,3)
test_complex(1,2,3, x=5)
test_complex(x=5)
# text_complex(x=5, 1,2,3)

def test_tuple() :
    return 1,2
a = test_tuple()  #튜플 한번에 받음
print(type(a),a)  
a, b = test_tuple()  #튜플 하나씩 담음
print(type(a),a)


def user_info(name, job, nation='한국') :
# def user_info(name, job, nation='한국', job) : # 중간에 낀건 안된다
    print(name, job, nation)

user_info('a','b','c')
user_info('a','b')
    
def add(x,y) :
    z = x + y
    return z +1
print(type(add))
c = add(1,2)
print(c)

# add =1 
# add(1,2)

add(1, add(2,3))


def test() :
    t = 1
test()
# print(t)

print('-'*20)
a = 1
def test2(z):
    a = z+1
test2(a)
print(a)

b = [1,2,3,4]
def test3(z):
    z.append(5)
test3(b)
print(b)


c = [1,2,3,4]
def test3(z):
    c = [1,2,3,4,5]
test3(c)
print(c)

#sep='' 지정해서 넣을수있다