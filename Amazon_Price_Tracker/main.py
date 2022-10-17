import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

WANT_PRICE = 200
AMAZON_URL = 'https://www.amazon.com/Nike-Mens-Dunk-Retro-DD1391/dp/B09SWPCL6J/ref=sr_1_111?crid=2697F8BVWZ1IO&keywords=nike+dunk&qid=1665983562&qu=eyJxc2MiOiI3LjA0IiwicXNhIjoiNy4xMSIsInFzcCI6IjUuNzYifQ%3D%3D&sprefix=nike+dunk%2Caps%2C257&sr=8-111'
EMAIL = "smtptest960@gmail.com"
PASSWORD = "dsfsdfqgQ"


def send_email(price):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="qspp@daum.net",
                            msg=f"Hi, Product that you want purchase is lower than your want price!\n"
                                f"Visit Amazon!!\n"
                                f"URL: {AMAZON_URL} Product Price: {price}"
                            )

response = requests.get(url=AMAZON_URL,headers={'Request Line': 'GET / HTTP/1.1',
                                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                                'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                                                'Cookie': 'PHPSESSID=fjooo3bu08jotslpdjkf0d4fe3; _ga=GA1.2.615614195.1665998484; _gid=GA1.2.1364359863.1665998484'
                                                })

soup = BeautifulSoup(response.text,'lxml')
price = soup.find('span','a-offscreen').getText()

price_float = float(price.split('$')[1])

if price_float < WANT_PRICE:
    send_email(price_float)
