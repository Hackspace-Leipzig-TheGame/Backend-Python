import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import player

gamesById = {}

class GameSocketHandler(tornado.websocket.WebSocketHandler):

    gameId = 0
    
    def open(self, id):
        print("Socket opened", id)
        self.gameId = int(id)
        p = player.Player(self)
        game = gamesById[self.gameId]
        game.addUser(p)

    def on_message(self, message):
        print(message)
        self.write_message(message + str(self.gameId))

    def on_close(self):
        print("Socket closed")

    def sendUpdateData(self, data):
        self.write_message(data)


class GameRequestHandler(tornado.web.RequestHandler):

    def get(self):
        loader = tornado.template.Loader("./templates/")
        self.write(loader.loader('index.html').generate())


class MainRequesHandler(tornado.web.RequestHandler):

    def get(self):
        loader = tornado.template.Loader("./templates/")
        self.write(loader.load('index.html').generate())


if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', MainRequesHandler),
        (r'/game/', GameRequestHandler),
        (r'/ws/(?P<id>[0-9]*)', GameSocketHandler),
        (r'/assets/(.)?', tornado.web.StaticFileHandler, {"path": "./assets/"}),
    ], debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
