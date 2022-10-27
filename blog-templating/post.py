import requests

BLOG_URL = 'https://api.npoint.io/19c7eb285b25a215e543'


class Post:
    def __init__(self):
        self.response = requests.get(url=BLOG_URL)
        self.blog_data = self.response.json()

    def get_blog_data(self):
        return self.blog_data

    def find_id_blog_data(self,blog_id):
        for post in self.blog_data:
            if post['id'] == blog_id:
                return post