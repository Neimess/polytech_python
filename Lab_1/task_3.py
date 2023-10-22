list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

half_length = len(list_players) // 2
first_half = list_players[:half_length]
second_half = list_players[half_length:]

print(first_half)
print(second_half)