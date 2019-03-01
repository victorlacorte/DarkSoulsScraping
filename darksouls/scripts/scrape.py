import asyncio
import json
import os

import aiohttp
from lxml import etree

from darksouls import parsing


base = 'http://darksouls.wiki.fextralife.com/'
weapons = f'{base}Weapons'

weapon_classes = ['Daggers',
                  'Straight+Swords',
                  'Greatswords',
                  'Ultra+Greatswords',
                  'Curved+Swords',
                  'Katanas',
                  'Curved+Greatswords',
                  'Piercing+Swords',
                  'Axes',
                  'Great+Axes',
                  'Hammers',
                  'Great+Hammers',
                  'Fist+Weapons',
                  'Spears',
                  'Halberds',
                  'Whips']

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64)' \
                    ' AppleWebKit/537.36 (KHTML, like Gecko)' \
                    ' Chrome/41.0.2225.0 Safari/537.36',
}

async def fetch_url(loop, url):
    name = os.path.basename(url.lower()) + '.html'
    async with aiohttp.ClientSession(loop=loop, headers=headers) as session:
        async with session.get(url) as resp:
            text = await resp.text()
            with open(name, 'w') as f:
                print(text, file=f)
            with open(name, 'r') as f:
                tree = etree.parse(
                        f,
                        parser=etree.HTMLParser(remove_blank_text=True))
                tree.write(
                        name,  # Ugly hack
                        encoding='utf-8',
                        method='html',
                        pretty_print=True)

async def fetch_weapon_classes(loop, weapon_classes=weapon_classes):
    async with aiohttp.ClientSession(loop=loop, headers=headers) as session:
        weapons = []
        for w in weapon_classes:
            async with session.get(f'{base}{w}') as resp:
                text = await resp.text()
                tree = etree.fromstring(
                        text,
                        parser=etree.HTMLParser(remove_blank_text=True))
                for parsed in parsing.parse_weapon_class(tree):
                    weapons.append(parsed)
        with open('out.json', 'w') as out:
            print(json.dumps(weapons, indent=4, ensure_ascii=False), file=out)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(fetch_url(loop, f'{base}Daggers'))
    loop.run_until_complete(fetch_weapon_classes(loop))
