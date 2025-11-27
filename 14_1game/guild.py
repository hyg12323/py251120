class Guild :

    def __init__(self, gname) :
        self.name = gname
        self.users = []

    def addUser(self, user) :
        self.users.append(user)
    
    def guildUsers(self):
        print(f"{self.name}")
        for i in self.users:
            print("이름",i.id,' ',end='')     
            print("레벨",i.level)   

    def ranker(self) :
        rank_user = self.users[0]

        for i in self.users:
            if i.level >rank_user.level :
                rank_user = i
        print("휴먼길드 랭커")
        print("이름:", rank_user.id)
        print("레벨:", rank_user.level)