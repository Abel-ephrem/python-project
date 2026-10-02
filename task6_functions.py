# a) Calculate total regional sales
def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]


# Test with the first game
print(calculate_total_sales(video_game_sales[0]))


# b) Filter games by genre
def filter_by_genre(data, genre='Platform'):
    filtered_games = []

    for game in data:
        if game[GENRE] == genre:
            filtered_games.append(game)

    return filtered_games


# Test without specifying a genre
platform_games = filter_by_genre(video_game_sales)
print(platform_games)


# Test with a specified genre
sports_games = filter_by_genre(video_game_sales, 'Sports')
print(sports_games)


