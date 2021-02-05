import requests, json, os

class GetMovie:
    def __init__(self, title, year, type, imbd_id, poster):
        self.title = title
        self.year = year
        self.type = type
        self.imbd_id = imbd_id
        self.poster = poster

    def print_search(self):
        print(f"{self.index}. {self.title} {self.year}")

    def chosen_movie_to_json(self):
        y = {'Title': self.title, 'Year': self.year, 'imdbID': self.imbd_id, 'Type': self.type, 'Poster': self.poster}
        if os.path.isfile("saved_movies.json") == False:
            with open("saved_movies.json", "w", encoding="utf-8") as file:
                data = {'save':[]}
                data['save'].append(y)
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            with open("saved_movies.json") as file:
                data = json.load(file)
                temp = data["save"]
                if len(temp) == 5:
                    temp.pop(0)
                temp.append(y)
            with open ("saved_movies.json", "w") as file:
                json.dump(data, file, indent=4)

class MovieInfo:
    def __init__(self, title, year, imdb_rating, directors, runtime, genre, type_of, plot):
        self.title = title
        self.year = year
        self.imdb_rating = imdb_rating
        self.directors = directors
        self.runtime = runtime
        self.genre = genre
        self.type = type_of
        self.plot = plot

    def print_more_info(self):
        clear()
        print("Mer information om filmen:\n")
        print(f"Film titel: {self.title} | {self.year}")
        print(f"Imdb score: {self.imdb_rating}\n")
        print(f"Regissörer: {self.directors}")
        print(f"{self.runtime} | {self.genre} | {self.type}")
        print(f"Plot: {self.plot}")

def search_menu():
    user_search = input("Vilken film vill du söka på?\n")
    fetch_url(f"http://www.omdbapi.com/?apikey=c5aaff41&s={user_search}")

def fetch_url(url):
    try:
        save_movie = []
        response = requests.get(url)
        data = response.json()
        i = 1
        for r in data['Search']:
            movie = GetMovie(r['Title'], r['Year'], r['Type'],r['imdbID'], r['Poster'])
            movie.index = i
            movie.print_search()
            i = i+1
        index_length = len(data['Search'])
        print(f"Vilken film vill du veta mer om? 1 - {index_length}")
        user_choose = int_check(index_length)
        y = 1

        for j in data['Search']:
            if y == int(user_choose):
                save_movie = GetMovie(j['Title'],j['Year'],j['Type'], j['imdbID'], j['Poster'])
                save_movie.chosen_movie_to_json()
                more_info(j['imdbID'])
                y = y+1
            else:
                y = y+1
                pass
    except KeyError:
        print("Hittade ingen film med det namnet")

    
def more_info(id):
    data = requests.get(f"http://www.omdbapi.com/?i={id}&apikey=c5aaff41")
    m = data.json()
    info_movie = MovieInfo(m['Title'], m['Year'], m['imdbRating'], m['Director'], m['Runtime'], m['Genre'], m['Type'], m['Plot'])
    info_movie.print_more_info()
    input("\n\n--Tryck på enter för att komma tillbaka till huvudmenyn--")
    clear()

def write_json(data, filename="saved_movies.json"):
        with open (filename, "w") as file:
            json.dump(data, file, indent=4)

def clear():
    os.system('cls')

def int_check(max_value):
    while True:
        try:
            user_input = int(input())
            if user_input > 0 and user_input <= max_value:
                return user_input
            else:
                print(f"Skriv ett tal som är mellan 1 och {max_value}")
        except ValueError:
            print("Skriv ett heltal :)")