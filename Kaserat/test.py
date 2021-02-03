import requests
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def introduce_self(self):
        print(f"The title of the movie is: {self.title}")
        print(f'It was produced year: {self.year}')


response = requests.get("http://www.omdbapi.com/?apikey=c5aaff41&s=inception")
data = response.json()
for r in data['Search']:
    movie1 = Movie(r['Title'], r['Year'])
    movie1.introduce_self()
