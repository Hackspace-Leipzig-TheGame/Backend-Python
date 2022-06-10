import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template


class GameSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print("Socket opened")

    def on_message(self, message):
        print(message)
        self.write_message(message)

    def on_close(self):
        print("Socket closed")

    def sendUpdateData(self, data):
        self.write_message(data)
        

class MainRequesHandler(tornado.web.RequestHandler):

    def get(self):
        loader = tornado.template.Loader("./templates/")
        self.write(loader.load('index.html').generate())


if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', MainRequesHandler),
        (r'/ws', GameSocketHandler),
        (r'/assets/(.)?', tornado.web.StaticFileHandler, {"path": "./assets/"}),
    ], debug=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
