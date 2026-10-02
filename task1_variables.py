total_games = len(video_game_sales)
print(f"Total number of games: {total_games}")

total_global_sales = sum(game[GLOBAL_SALES] for game in video_game_sales)

avg_global_sales = total_global_sales / total_games
print(f"Average global sales: {avg_global_sales:.2f} million copies")
