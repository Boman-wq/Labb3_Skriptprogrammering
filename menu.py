#http://www.omdbapi.com/?apikey=[DINAPINYCKEL]&s=[FilmensNamn] 
import ShowMovie as call
import GetMovie as run


def mainmenu():
    while True:
        print("1) Sök efter film\n2) Visa senaste sökningar\n3) Avsluta")
        user_input = input()
        if user_input == "1":
            run.clear()
            run.search_menu()
        elif user_input == "2":
            run.clear()
            submenu()
        elif user_input == "3":
            run.clear()
            break

def submenu():
    while True:
        print("1) Visa historik\n2) Visa mer information i historik\n3) Gå tillbaka till huvudmenyn")
        user_input = input()
        if user_input == "1":
            run.clear()
            call.show_last_five()
        elif user_input == "2":
            run.clear()
            call.more_info_last_five()
        elif user_input == "3":
            run.clear()
            break