class User:

    def __init__(self, x, y):
        self.id = x
        self.level = y
        self.inven = []

    def addItem(self, *items):
        for item in items:
            self.inven.append(item)

    def printinfo(self):
        print('id', self.id)
        print('level', self.level)
        print('inven', self.inven)


    def __str__(self) : # 사용자한테 보여주기용
        return f'(str)user(id:{self.id}, level:{self.level}, inven :{self.inven})'
    def __repr__(self) : #개발자용
        return f'(str)user(id:{self.id}, level:{self.level}, inven :{self.inven})'

# u1 = User("용군", 10)
# u1.addItem("gun","bomb")
# u1.printinfo()

# u2 = User("우영", 8)
# u2.addItem("gun","bomb")
# u2.printinfo()

                
          
    

     


    
