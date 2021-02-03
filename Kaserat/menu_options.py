import requests, json
import os
#https://www.youtube.com/watch?v=hJ2HfejqppE

class MenuOption:
    def __init__(self):
        pass

    def search_menu():
         user_search = input("Vilken film vill du söka på?\n")
         MenuOption.fetch_url(f"http://www.omdbapi.com/?apikey=c5aaff41&s={user_search}")

    def fetch_url(url):
        save_movie = []
        response = requests.get(url)
        data = response.json()
        i = 0
        for r in data['Search']:
            title = r['Title']
            year = r['Year']
            print(f'{i}. {title} - {year}')
            i=i+1
        index_length = len(data['Search'])-1
        user_choose = input(f"\nVilken film vill du veta mer om? 0 - {index_length}\n")
        y = 0
        for j in data['Search']:
            if y == int(user_choose):
                save_movie.append(j)
                MenuOption.print_movie_information(j)
                y = y+1
            else:
                y = y+1
                pass
        
    def print_movie_information(movie_info):
        title = movie_info['Title']
        year = movie_info['Year']
        type = movie_info['Type']
        imbd_id = movie_info['imdbID']
        poster = movie_info['Poster']

        MenuOption.get_movie_info(imbd_id)

        if os.path.isfile("saved_movies.json") == False:
            with open("saved_movies.json", "w", encoding="utf-8") as file:
                data = {'save':[]}
                data['save'].append(movie_info)
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            with open("saved_movies.json") as file:
                data = json.load(file)
                temp = data["save"]
                y = {'Title': title, 'Year': year, 'imdbID': imbd_id, 'Type': type, 'Poster': poster}
                temp.append(y)
                MenuOption.write_json(data)

    def get_movie_info(id):
        data = requests.get(f"http://www.omdbapi.com/?i={id}&apikey=c5aaff41")
        movie = data.json()

        title = movie['Title']
        year = movie['Year']
        directors = movie['Director']
        runtime = movie['Runtime']
        plot = movie['Plot']
        rating = movie['imdbRating']
        genre = movie['Genre']

        print("Information om filmen:\n")
        print(f"Title: {title}")
        print(f"Prodocerad: {year}\n")
        print(f"Imbd rating: {rating}")
        print(f"Regissörer: {directors}\n\n")
        print(f"{runtime} | {genre}")
        print(f"{plot}")
        input()

    def write_json(data, filename="saved_movies.json"):
        with open (filename, "w") as file:
            json.dump(data, file, indent=4)
