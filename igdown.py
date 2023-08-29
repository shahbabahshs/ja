from requests import Session
from bs4 import BeautifulSoup

class IG_Down(Session):
  def get_media(self, url):
    ses = self.get('https://gnome-connected-tropical-clients.trycloudflare.com/')
    soup = BeautifulSoup(ses.content, 'html.parser')
    form = soup.find('form')
    if form:
      token = form.find('textarea', {'name': 'url'})['required']
      download_response = self.post('https://gnome-connected-tropical-clients.trycloudflare.com/', data={
        'url': url,
        'token': token,
      },
      headers={
        'hx-current-url': 'https://gnome-connected-tropical-clients.trycloudflare.com',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://gnome-connected-tropical-clients.trycloudflare.com/',
        'pragma': 'no-cache',
        'referer': 'https://gnome-connected-tropical-clients.trycloudflare.com/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': "Android",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) ' 'AppleWebKit/537.36 (KHTML, like Gecko)' ' Chrome/115.0.0.0 Mobile Safari/537.36'
      })
      download_soup = BeautifulSoup(download_response.content, 'html.parser')
      video_link = download_soup.find('a')['href']
      thumbnail = download_soup.find('img')['src']
      return [video_link,thumbnail]
    else:
      return ["Form not found on the page."]
      
def sssig(url):
    return IG_Down().get_media(url)