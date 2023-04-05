ld = [{'id': 1, 'previous_id': 0, 'p1': {'health': 30, 'shields': 50}, 'p2': {'health': 15, 'shields': 55}, 'player': 'p1', 'spell': 'fire', 'rating': 1}, {'id': 2, 'previous_id': 0, 'p1': {'health': 30, 'shields': 50}, 'p2': {'health': 20, 'shields': 50}, 'player': 'p1', 'spell': 'frost', 'rating': -1}]
max_rating: int = -1
best_option: dict

for i in range(len(ld)):
    if max_rating < ld[i]['rating']:
        max_rating = ld[i]['rating']
        best_option = ld[i]

print(best_option)