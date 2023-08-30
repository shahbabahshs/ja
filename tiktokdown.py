from httpx import AsyncClient
from requests import Session
import re
from base64 import b64decode
#from bs4 import BeautifulSoup

class SsstikIO(Session):
    def get_media(self, url):
        ses = self.get('https://ssstik.io')
        resp = self.post(
            'https://ssstik.io/abc?url=dl', data={
                'id': url,
                'locale': 'en',
                'tt': re.findall(r'tt:\'([\w\d]+)\'', ses.text)[0],
            },
            headers={
                'hx-current-url': 'https://ssstik.io/id',
                'hx-request': 'true',
                'hx-target': 'target',
                'hx-trigger': '_gcaptcha_pt',
                'origin': 'https://ssstik.io',
                'pragma': 'no-cache',
                'referer': 'https://ssstik.io/id',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", '
                '"Google Chrome";v="102"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Linux",
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) '
                'AppleWebKit/537.36 (KHTML, like Gecko)'
                ' Chrome/102.0.5059.159 Safari/537.36'
                }
        )
        #download_soup = BeautifulSoup(resp.content, 'html.parser')
        #video_link = download_soup.find('a')['href']
        return [
            (b64decode('/'.join(x.split('/')[5:])).decode() if 'ssscdn.io' in x else x)
            for x in set(re.findall('href="(.*?)"', resp.text))
        ]

def ssstik(url):
    return SsstikIO().get_media(url)
