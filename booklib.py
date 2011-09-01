import fnmatch
import os
import os.path

from google.appengine.ext.webapp import template

from docutils.core import publish_parts

def get_base_dir():
    return os.path.split(__file__)[0]

def get_base_book_dir():
    return os.path.join(get_base_dir(), 'books')

def get_template_dir():
    return os.path.join(get_base_dir(), 'templates')

def is_rst(filename):
    return fnmatch.fnmatch(filename, '*.rst')

def guess_filename(path):
    path = path.strip('/')
    path = os.path.join(get_base_book_dir(), path)

    if is_rst(path):
        return path

    if os.path.isfile(path + '.rst'):
        return path + '.rst'

    if os.path.isdir(path):
        return os.path.join(path, 'index.rst')

    return None

def publish_book(path):
    source = file(path, 'r').read()

    settings = { 'config' : None }
    os.environ['DOCUTILSCONFIG'] = ''

    parts = publish_parts(source=source,
                          writer_name='html4css1',
                          settings_overrides=settings)

    important_parts = dict()
    important_parts['title'] = parts['title']
    important_parts['body'] = parts['html_body']

    return important_parts

def render_book(parts):
    template_variables = {
        'title' : parts['title'],
        'body'  : parts['body']
        }

    return template.render(
        os.path.join(get_template_dir(), 'book.html'),
        template_variables)
