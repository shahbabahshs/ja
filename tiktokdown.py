from httpx import AsyncClient
from requests import Session
import re
from base64 import b64decode
from bs4 import BeautifulSoup

class SsstikIO(Session):
    def get_media(self, url):
        ses = self.get('https://ssstik.io')
        resp = self.post(
            'https://ssstik.io/abc?url=dl', data={
                'id': url,
                'locale': 'en',
                'tt': ses.text,
                #'tt': re.findall(r'tt:\'([\w\d]+)\'', ses.text)[0],
            },
            headers={
                'hx-current-url': 'https://ssstik.io/en',
                'hx-request': 'true',
                'hx-target': 'target',
                'hx-trigger': '_gcaptcha_pt',
                'origin': 'https://ssstik.io',
                'pragma': 'no-cache',
                'referer': 'https://ssstik.io/en',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120",'
                '"Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Android",
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) '
                'AppleWebKit/537.36 (KHTML, like Gecko)'
                ' Chrome/120.0.0.0 Mobile Safari/537.36'
                }
        )
        download_soup = BeautifulSoup(resp.content, 'html.parser')
        video_link = download_soup.find('a')['href']
        return [video_link][0]
        

def ssstik(url):
    return SsstikIO().get_media(url)
