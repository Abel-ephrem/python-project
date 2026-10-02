# a) Create a list containing only the names of all games
game_names = []

for game in video_game_sales:
    game_names.append(game[NAME])

print(game_names)

