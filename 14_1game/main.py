from User import User
from guild import Guild
# import guild

u1 = User("용군", 10)
u2 = User("우영", 7)
u3 = User("동현", 12)


u1.addItem("gun","bomb")
u2.addItem("gun","bomb")

print(1,u1)
print(2,str(u1)+'!!!!')

u1.printinfo()
u2.printinfo()
u3.printinfo()


g = Guild("----휴먼길드----")
g.addUser(u1)
g.addUser(u2)
g.addUser(u3)
g.guildUsers()


g.ranker()