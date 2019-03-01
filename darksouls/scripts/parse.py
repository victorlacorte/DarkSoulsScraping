from lxml import etree
import requests

from darksouls import parsing


base = 'http://darksouls.wiki.fextralife.com/'

def main():
    # url = f'{base}Daggers'
    # req = requests.get(url)
    tree = etree.parse(
            'daggers.html',
            parser=etree.HTMLParser(remove_blank_text=True))
    #tree = etree.fromstring(req.content)
    parsing.parse_weapon_class(tree)

if __name__ == '__main__':
    main()
