# a) Total global sales by genre
sales_by_genre = {}

for game in video_game_sales:
    genre = game[GENRE]
    sales = game[GLOBAL_SALES]

    if genre not in sales_by_genre:
        sales_by_genre[genre] = 0

    sales_by_genre[genre] += sales

print(sales_by_genre)

# b) Count how many games each publisher has
games_per_publisher = {}

for game in video_game_sales:
    publisher = game[PUBLISHER]

    if publisher not in games_per_publisher:
        games_per_publisher[publisher] = 0

    games_per_publisher[publisher] += 1

print(games_per_publisher)

# c) Create a dictionary containing details of the #1 ranked game
top_game = {
    'name': video_game_sales[0][NAME],
    'year': video_game_sales[0][YEAR],
    'genre': video_game_sales[0][GENRE],
    'publisher': video_game_sales[0][PUBLISHER],
    'global_sales': video_game_sales[0][GLOBAL_SALES]
}

for key, value in top_game.items():
    print(key, ":", value)

