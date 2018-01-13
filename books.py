import os.path
import sys

import webapp2

import booklib


class MainPage(webapp2.RequestHandler):
    def get(self):
        filename = booklib.guess_filename(self.request.path)
        if filename:
            parts = booklib.publish_book(filename)
            rendered_book = booklib.render_book(parts)
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(rendered_book)


app = webapp2.WSGIApplication([('/.*', MainPage)],
                              debug=True)
