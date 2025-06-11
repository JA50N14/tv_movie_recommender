import sys
from tv_shows_api import show_search_title, show_recommender, show_similar, show_description
from movies_api import movie_search_title, movie_recommender, movie_similar, movie_description

SEARCH_TV_OPTIONS = {
    1: "TV Show Recommender",
    2: "TV Show Similar",
    3: "TV Show Description/Reviews"
}

SEARCH_MOVIE_OPTIONS = {
    1: "Movie Recommender",
    2: "Movie Similar",
    3: "Movie Description/Reviews"
}

def entrance():
    print("--------------------------------------------------------------------------------------------------------------------")
    print("""Welcome to TV Show and Movie recommender main menu! At any point, press 0 to return to this main menu OR \"q\" to quit.\n
Press 1 if searching for a TV show or 2 if searching for a movie.
          """)

    while True:
        search_type = input("> ")
        main_menu_or_quit(search_type)
        if search_type.isdigit():
            search_type = int(search_type)
            if search_type == 1 or search_type == 2:
                break
        print("You did not enter a 1 or 2! Please enter a 1 if searching for a TV show OR 2 if searching for a movie.")

    if search_type == 1:
        query_type = tv_query_type()
    elif search_type == 2:
        query_type = movie_query_type()
    
    while True:
        tv_movie_title_str = get_tv_movie_title(search_type)

        if search_type == 1:
            title_id_list = show_search_title(tv_movie_title_str)
        elif search_type == 2:
            #title_id_list = movie_search_title(tv_movie_title_str)
            pass
        
        if len(title_id_list) != 0:
            break
        print(f"There were no matches found for \"{tv_movie_title_str}\". Please try entering a different title.")
    
    title_and_id = select_tv_movie_title_from_results(title_id_list, tv_movie_title_str)
    print(title_and_id)
    #########################

    if search_type == 1:
        match query_type:
            case 1:
                show_recommender(title_and_id)
            case 2:
                show_similar(title_and_id)
            case 3:
                show_description(title_and_id)
    elif search_type == 2:
        match query_type:
            case 1:
                movie_recommender(title_and_id)
            case 2:
                movie_similar(title_and_id)
            case 3:
                movie_description(title_and_id)
    
    
        


    #CALL TV SHOW OR MOVIE API BASED ON: search_type (1=tv, 2=movie) / query_type (1=recommender, 2=similar, 3=description) / title_and_id=(title, id)


def select_tv_movie_title_from_results(title_id_list, title_str):
    if len(title_id_list) == 1:
        return title_id_list[0]
    for i in range(len(title_id_list)):
        if title_str.lower() == title_id_list[i][0].lower():
            return title_id_list[i]
    
    while True:
        print(f"Select the title by entering its corresponding number.")
        for i in range(len(title_id_list)):
            print(f"{i + 1}. {title_id_list[i][0]}")
        title_num = input("> ")
        main_menu_or_quit(title_num)
        if title_num.isdigit():
            title_num = int(title_num)
            if 0 < title_num <= len(title_id_list):
                return title_id_list[title_num - 1]
        print("Not a valid entry!")


def get_tv_movie_title(search_type):
    print("----------------------------------------")
    while True:
        if search_type == 1:
            print("Enter the name of the TV Show.")
        else:
            print("Enter the name of the movie.")
        title = input("> ").strip()
        main_menu_or_quit(title)
        print(f"\nIs this correct \"{title}\"? Enter y or n")
        verify_title = input("> ").lower()
        if verify_title == "y":
            break
        main_menu_or_quit(verify_title)
    return title


def tv_query_type():
    print("-------------------------------------------------------------------------")
    print("""Select the type of TV Show search by entering its corresponding number:\n
1. View list of recommended TV shows based off a TV show you liked\n
2. View list of similar TV shows based off a TV show you liked\n
3. TV show description/review information
          """)
    while True:
        query_type = input("> ")
        main_menu_or_quit(query_type)
        if query_type.isdigit():
            query_type = int(query_type)
            if query_type in SEARCH_TV_OPTIONS:
                break
        print("You did not enter a valid input. Please select a valid search option.")
    return query_type


def movie_query_type():
    print("-----------------------------------------------------------------------")
    print("""Select the type of movie search by entering its corresponding number:\n
1. View list of recommended movies based off a movie you liked\n
2. View list of similar movies based off a movie you liked\n
3. Movie description/review information
          """)
    while True:
        query_type = input("> ")
        main_menu_or_quit(query_type)
        if query_type.isdigit():
            query_type = int(query_type)
            if query_type in SEARCH_MOVIE_OPTIONS:
                break
        print("You did not enter a valid input. Please select a valid search option.")
    return query_type


def main_menu_or_quit(user_input):
    if user_input.lower() == "q":
        print("Exiting Program...")
        sys.exit()
    elif user_input == "0":
        return entrance()
    return

if __name__ == "__main__":
    entrance()