from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = '5'


HtmlDocument.media_type = 'text/html'

pprint(HtmlDocument.__dict__)