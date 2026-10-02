# a) Calculate total regional sales
def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]


# Test with the first game
print(calculate_total_sales(video_game_sales[0]))


