from xml.etree.ElementTree import XMLParser

class DemoXMLParser:
    score = 0
    def start(self, tag, attr):
        self.score += len(attr)
    def close(self):
        return self.score

parser = XMLParser(target=DemoXMLParser())
n = int(input())
template = []
for _ in range(n):
    template.append(input())
template = '\n'.join(template)
parser.feed(template)
print(parser.close())