# Define the weighted elo score over a number of games:
def get_elo(game_results, opponent_scores):
    # opponent_scores = [x for ind, x in enumerate(opponent_scores) if game_results[ind]!='1/2-1/2']
    opponent_sum = opponent_scores
    games = len(game_results)
    wins = game_results.count(1)
    losses = game_results.count(-1)

    elo = (opponent_sum + 400 * (wins - losses)) / games
    return elo
