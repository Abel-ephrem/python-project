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


# c) Calculate total North America and Japan sales
total_na_sales = 0
total_jp_sales = 0

for game in video_game_sales:
    total_na_sales += game[NA_SALES]
    total_jp_sales += game[JP_SALES]

print("Total North America sales:", total_na_sales)
print("Total Japan sales:", total_jp_sales)

if total_na_sales > total_jp_sales:
    print("North America had higher sales.")
elif total_jp_sales > total_na_sales:
    print("Japan had higher sales.")
else:
    print("Both regions had the same sales.")


