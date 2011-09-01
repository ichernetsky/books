import os.path
import sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def fix_path():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
fix_path()

import booklib

class MainPage(webapp.RequestHandler):
    def get(self):
        filename = booklib.guess_filename(self.request.path)
        if filename:
            parts = booklib.publish_book(filename)
            rendered_book = booklib.render_book(parts)
            self.response.out.write(rendered_book)

application = webapp.WSGIApplication([('/.*', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
