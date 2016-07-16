# coding: UTF-8
import os
import web

from weixinInterface import WeixinInterface

urls = (
    '/','WeixinInterface',
    '/test', 'index',
    '/call','mycall',
    '/regex/(.*)/(.*)','myregex'
)


class index:
    def GET(self):
        return "Hello, world 6!"
        
class mycall:
    # http://localhost:8080/call?args1=the&args2=world
    # take default values, with the concept of <Storage>
    def GET(self, args1="wtf", args2=None):
        data = web.input()

	if data.has_key('args1'):
	    args1 = data.args1

        args2 = data.args2
        return "hello: " + args1 + " " + args2 + "!"
        
class myregex:
    # http://localhost:8080/regex/aaa/bbb
    # no default values, w/o the concept of <Storage>
    def GET(self,args1,args2):
        data = web.input()
        print data

        return "regex: " + args1 + " " + args2 +"!!"






app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
else:
    # pass
    import sae
    app = web.application(urls, globals()).wsgifunc()        
    application = sae.create_wsgi_app(app)
