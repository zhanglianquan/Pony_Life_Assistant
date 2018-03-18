# coding=utf-8
# Author: zlq
# Copyright (C) 2018/03/18.

"""
    系统启动的主模块
"""


import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options as opt
import settings
import controller.base as base

opt.define("port", default=9090, help="Run server on a specific port", type=int)
opt.define("host", default="127.0.0.1", help="Run server on a specific host")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = base.collect_handlers()
        tornado.web.Application.__init__(self, handlers, **settings.tornado)


def main():
    opt.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(opt.options.port, opt.options.host)
    tornado.ioloop.IOLoop().instance().start()


if __name__ == "__main__":
    main()
