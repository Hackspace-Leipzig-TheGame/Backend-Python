import tornado.ioloop
import tornado.web
import tornado.websocket

class GameSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print("Socket opened")

    def on_message(self, message):
        print(message)

    def on_close(self):
        print("Socket closed")

class MainRequesHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello World")


if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', MainRequesHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
