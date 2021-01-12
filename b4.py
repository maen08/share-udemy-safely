import requests
from bs4 import BeautifulSoup



url = 'https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F'


# data_form = {'email': '2001stany@gmail.com', 'password': 'mwanaume'}
# resp = requests.post(url, data=data_form)
# BeautifulSoup(resp.text, 'html.parser')


res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
form = soup.find('div', {'name': 'email'})

value_data = form[0].input['value']




print(soup)