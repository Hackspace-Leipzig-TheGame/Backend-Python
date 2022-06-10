import random

class Game:
    def __init__(self, id, userstring):
        self.id = id
        self.users = []
        self.cardstack = random.shuffle([i+1 for i in range(100)])


    def addUser(self, userstring):
        self.users.append(userstring)

    def giveCards(cardstack, users, giveCard):
        for i in range(6):
            for user in users:
                i = 0
                giveCard(user, cardstack[i])
                i += 1

