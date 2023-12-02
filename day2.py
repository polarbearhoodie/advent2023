import helper as hp

array = hp.parse_input("input2")
array = [game.split(":")[1].strip() for game in array]
array = [sample.split(";") for sample in array]

array3 = []
for game in array:
    dict1 = {}
    for sample in game:
        cubes = sample.split(',')
        for count in cubes:
            count = count.strip()
            keyval = count.split(' ')
            dict1[keyval[1]] = max(dict1.get(keyval[1], 0), int(keyval[0]))

    array3.append(dict1)

game_totals = 0

for i in range(len(array3)):
    game = array3[i]
    n = i+1
    if game.get('red', 0) <= 12 and game.get('blue', 0) <= 14 and game.get('green', 0) <= 13:
        game_totals += n

print(game_totals)

power_total = 0
for game in array3:
    powers = 1
    powers *= game.get('red', 0)
    powers *= game.get('green', 0)
    powers *= game.get('blue', 0)
    power_total += powers

print(power_total)