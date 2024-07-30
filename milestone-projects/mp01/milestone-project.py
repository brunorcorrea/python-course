MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def print_movie(movie):
    print(f"Title: {movie['title']}\nDirector: {movie['director']}\nRelease year: {movie['year']}")

def list_movies():
    if len(movies) == 0:
        print("There are no registered movies yet!")
        return

    for movie in movies:
        print_movie(movie)
        print("--- ---")
        
def find_movie(title):
    for movie in movies:
        if movie['title'] == title:
            print_movie(movie)
            break
    else:
        print("The requested movie was not found!")

user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": find_movie
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please try again.")
        
        selection = input(MENU_PROMPT)
        
menu()