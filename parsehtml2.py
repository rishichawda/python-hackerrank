from html.parser import HTMLParser

class DemoHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
    def handle_comment(self, data):
        print('>>> Multi-line Comment' if '\n' in data else '>>> Single-line Comment')
        print(data)

parser = DemoHTMLParser()
for _ in range(int(input())):
    parser.feed(input())