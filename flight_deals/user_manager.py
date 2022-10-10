import requests

END_POINT = 'https://api.sheety.co/522dcb0493698871159d9ab4cd20f4f1/flightDeals/users'
API_KEY = 'Bearer nfldjlwejlkfjdskjfwkebk'

class UserManager:

    def sign_up_user(self):

        self.first_name = input("Your first Name?: ")
        self.last_name = input("Your last Name?: ")
        self.email = input("Your Email?: ")
        check_email = input("Your Email(CHECK): ")
        if self.email == check_email:
            print("Congratulation!!")
            self.update_user_sheet()
        else:
            print("Email is not same")

    def update_user_sheet(self):
        self.header = {
            'Authorization': API_KEY,
        }

        self.params = {
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'Email': self.email,
        }
        self.response = requests.put(url=END_POINT,json=self.params,headers=self.header)


