class FourCal : 

    # 생성자
    # 생성할 때 무조건 실행되는 함수
    # 전달인자가 안 맞으면 생성이 안된다
    def  __init__(self, x,y ) : 
        self.x = x
        self.y = y
    
    
    
    
    def setData(self, x, y) :
        self.x = x
        self.y = y
    def add(self) :
        return self.x + self.y
    
a = FourCal(1,2)
print( type(a))

b = FourCal(30,45)
print(id(a),id(b))


a.setData(3,4)
print('a.x :', a.x)

b.setData(30,40)
print('b.x :',b.x)

print('a.add()',a.add())
print('b.add()',b.add())

# c = FourCal()
# c.add()

class FourCal2 :
   
    static_var = '생성없이 사용가능'
 
    def __init__(self) :
        self.x = 5
        self.y = 10
    def add(self) :
        return self.x +self.y
    
    def pow(self) :
        return self.x **self.y
    def add(self) :
        return self.x + self.y +1
        

        

class MoreCal2 (FourCal2) :
    pass 
d = MoreCal2()
print('d.x :', d.x)
print('d.add() :', d.add())
print('d.pow() :', d.pow())

print( FourCal2.static_var)
print( MoreCal2.static_var)
print( d.static_var)