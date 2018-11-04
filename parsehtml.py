from html.parser import HTMLParser
class DemoHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print('Start'.ljust(6, ' ')+':', tag)
        for a in attr:
            print('-> {} > {}'.format(a[0], a[1]))
    def handle_endtag(self, tag):
        print('End'.ljust(6, ' ')+':', tag)
    def handle_startendtag(self, tag, attr):
        print('Empty'.ljust(6, ' ')+':', tag)
        for a in attr:
            print('-> {} > {}'.format(a[0], a[1]))
    def handle_comment(self, data):
        pass

parser = DemoHTMLParser()
for _ in range(int(input())):
    parser.feed(input())