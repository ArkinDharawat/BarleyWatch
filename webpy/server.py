#!/usr/bin/python
import web

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        # redirect to the static file ...
        raise web.seeother('/static/index.html')

app = web.application(urls, globals())

if __name__ == "__main__": app.run()