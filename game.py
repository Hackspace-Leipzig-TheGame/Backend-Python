import random
from helpers import get_random_string
class Game:
    def __init__(self, id, maxUsers, totalCards):
        #self.id = id
        self.mode = {
            self.maxUsers: maxUsers,
            self.maxHandCards: 7 if len(self.users) == 2 else 6,
            self.totalCards: totalCards or 100
        }
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

