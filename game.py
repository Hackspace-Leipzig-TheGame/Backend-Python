import random

class Game:
    def __init__(self, id, userstring):
        self.id = id
        self.users = []
        self.cardstack = random.shuffle([i+1 for i in range(100)])


    def addUser(self, userstring):
        self.users.append(userstring)

    def giveCards(self):
        for i in range(6):
            for user in self.users:
                user.giveCard(self.cardstack[0])
                self.cardstack = self.cardstack[1:]

        for u in self.users:
            u.sendUpdate()

