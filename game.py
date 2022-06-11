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
        self.active_user = self.users[random(range(len(self.users)))] # Spieler, der an der Reihe ist - initial zufällig
        self.cardstack = random.shuffle([i+1 for i in range(self.totalCards)]) # Zielstapel mit X gemischten Karten
        self.heap_1, self.heap_2, self.heap_3, self.heap_4 = [] # die 4 Spiel"stapel"

        game_id = self.addUser() # User, der das Spiel eröffnet hinzufügen
        return game_id

    def checkUserNumber(self):
        if len(self.users) < self.mode["maxUsers"]:
            return True
        else:
            raise("no place left")

    def addUser(self):
        userstring = get_random_string(10)
        if self.checkUserNumber():
            self.users.append(userstring)
        return userstring

    def giveCards(self, cardstack, users, giveCard):
        for i in range(self.mode["maxHandCards"]):
            j = 0
            for user in users:
                giveCard(user, cardstack[i])
                j += 1

