# a) Print games with more than 25 million global sales
for game in video_game_sales:
    if game[GLOBAL_SALES] > 25:
        print(game[NAME], game[GLOBAL_SALES])


