from bs4 import BeautifulSoup
import requests

URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'


class RentalDataManager():

    def __init__(self):
        self.response = requests.get(url=URL, headers={'User-Agent': 'Mozilla/5.0'})
        self.rental_page = self.response.text
        self.rental_price = []
        self.rental_link = []
        self.rental_address = []

        soup = BeautifulSoup(self.rental_page,'html.parser')
        rental_data = soup.find_all('li','ListItem-c11n-8-73-8__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation')

        count = 0

        for rental in rental_data:
            count += 1
            address = rental.find('address').getText()
            link = rental.find('a').get('href')
            price = rental.find('span').getText()
            if '+' in price:
                price = price.split('+')
                price = price[0]
            elif '/' in price:
                price = price.split('/')
                price = price[0]

            if link[0] == '/':
                link = link.split('/')
                link = 'https://www.zillow.com/homedetails/' + link[2]

            self.rental_address.append(address)
            self.rental_link.append(link)
            self.rental_price.append(price)

            if count == 8:
                break



