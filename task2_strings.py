# a) extract the name of the 5th game 
game_name = video_game_sales[4][NAME]
pokemon = game_name[:7]
print(pokemon)

# b) clean the game names by stripping whitespace and converting to lowercase

messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

for name in messy_names:
    clean_name = name.strip().lower()
    print(clean_name)

# c) fomatted summary of the 1st game 

top_game = video_game_sales[0]

print(f"#1 Best Seller: {top_game[NAME]} ({top_game[YEAR]}) - ${top_game[GLOBAL_SALES]:.2f}M global sales") 
