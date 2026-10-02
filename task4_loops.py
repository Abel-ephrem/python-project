# a) Print games with more than 25 million global sales
for game in video_game_sales:
    if game[GLOBAL_SALES] > 25:
        print(game[NAME], game[GLOBAL_SALES])


# b) Count games released before the year 2000
pre_2000_count = 0

for game in video_game_sales:
    if game[YEAR] < 2000:
        pre_2000_count += 1

print("Games released before 2000:", pre_2000_count)


