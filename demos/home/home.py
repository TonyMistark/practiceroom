#!/usr/bin/env python
# encoding: utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8880, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class HomeHandler(tornado.web.RequestHandler):

    def get(self):
        web_sites = [
            ("PR | Blog", "http://blog.practiceroom.top:8882"),
            ("PR | DjangoX", "http://home.practiceroom.top:8885/xadmin"),
            ("PR | Chat", "http://home.practiceroom.top:8887"),
            ("OsChina | michao", "https://my.oschina.net/michao"),
            ("GitHub | michao", "https://github.com/TonyMistark")
        ]
        self.render(web_sites=web_sites, template_name="templates/my_home.html")


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", HomeHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
