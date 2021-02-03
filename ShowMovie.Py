import json
import GetMovie as run
class ShowMoive:
    def __init__(self):
        pass

def show_last_five():
    try:
        with open("saved_movies.json", "r") as file:
            data = json.load(file)
        i = 1
        print("\nFem senaste sökta filmerna:\n")
        for r in reversed(data['save'][-5:]):
            movie = run.GetMovie(r['Title'], r['Year'], r['Type'],r['imdbID'], r['Poster'])
            movie.index = i
            movie.print_search()
            i = i+1
        print()
    except FileNotFoundError:
        print("Det finns ingen fil att läsa ifrån")

def more_info_last_five():
    show_last_five()
    try:
        with open("saved_movies.json", "r") as file:
            data = json.load(file)
        index_length = len(data['save'])
        y =  index_length-5
        print(f"Vilken film vill du veta mer om? 1 - 5")
        user_input = run.int_check(5)
        user_input = index_length - user_input 
        for j in data['save'][-5:]:
            if y == int(user_input):
                run.more_info(j['imdbID'])
                y = y+1
            else:
                y = y+1
                pass
    except FileNotFoundError:
        return