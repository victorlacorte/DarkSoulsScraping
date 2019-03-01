'''
'''

import json

from lxml.html import HtmlElement


headers = ['Image',
          'Name',
          'Physical AR / DR',
          'Magical AR / DR',
          'Fire AR / DR',
          'Lightning AR / DR',
          'Critical bonus / ?',
          'Aux effects',
          'Str req / scaling / scaling @ max',
          'Dex req / scaling / scaling @ max',
          'Int req / scaling / scaling @ max',
          'Fai req / scaling / scaling @ max',
          'Durability / Weight',
          'Attack type(s)',
          'Acquired from']

def parse_weapon_class(tree):
    '''
    Return a dict representing the table @class=wiki_table found in `tree'.
    '''
    for tr in tree.xpath('.//table[@class="wiki_table"]//tr'):
        weapon = {}
        i = 0
        for child in tr:
            if child is not None and child.tag != 'td':
                break
            #h = HtmlElement(child)
            #weapon[headers[i]] = h.text_content()
            s = []
            for text in child.itertext():
                res = text.strip()
                if res:
                    s.append(res)
            weapon[headers[i]] = ', '.join(s)
            i += 1
        yield weapon
    #     weapons.append(weapon)
    # return json.dumps(weapons, indent=4, ensure_ascii=False)
