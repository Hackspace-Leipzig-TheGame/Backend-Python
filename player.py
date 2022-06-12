

class Player:

    def __init__(self, socket, displayName=''):
        self.socket = socket
        self.displayName = displayName
        self.handCards = [-1 for _ in range(6)]

    def sendUpdate(self, game):
        # generate update data
        data = {
            "data": "Much Update, such Wow!"
        }
        self.socket.sendUpdateData(data)

    def updateCards(self, cards, game):
        self.handCards = cards
        self.sendUpdate(game)

    def giveCard(self, card):
        
