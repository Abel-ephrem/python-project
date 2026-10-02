# a) extract the name of the 5th game 
game_name = video_game_sales[4][NAME]
pokemon = game_name[:7]
print(pokemon)

# b) clean the game names by stripping whitespace and converting to lowercase

messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

for name in messy_names:
    clean_name = name.strip().lower()
    print(clean_name)

