import time

start_time = time.time_ns()
def parse_input(filename):  # RegEx is not my strongest suit
    games_list = []
    with open(filename) as file:
        for line in file:
            game, reveals = line.strip("\n").split(": ")  # split game number and reveals
            reveals = reveals.split("; ")  # split into reveals arrays
            game, game_id = game.split(" ")  # parse game number
            reveals_list = []
            # maakt list aan reveal dicts:
            for i, reveal in enumerate(reveals):
                reveal_dict = {}
                colorsets = reveal.split(", ")
                for c_set in colorsets:
                    amount, color = c_set.split(" ")
                    reveal_dict[color] = int(amount)
                reveals_list.append(reveal_dict)
            games_list.append([int(game_id), reveals_list])
    return games_list


# written for pt 01
def check_game(game_list):
    check_dict = {'green': 13, 'red': 12, 'blue': 14}
    color_list = ['blue', 'green', 'red']
    check = True
    for game in game_list:
        for color in color_list:
            if color in game:
                if game[color] > check_dict[color]:
                    check = False
                    break
    return check


# written vor pt. 02
def get_green(subgame):
    retval = subgame.get('green')
    return retval if isinstance(retval, int) else 0


def get_blue(subgame):
    retval = subgame.get('blue')
    return retval if isinstance(retval, int) else 0


def get_red(subgame):
    retval = subgame.get('red')
    return retval if isinstance(retval, int) else 0


def find_power(game):
    game.sort(key=get_blue, reverse=True)
    highblue = game[0]['blue']
    game.sort(key=get_green, reverse=True)
    highgreen = game[0]['green']
    game.sort(key=get_red, reverse=True)
    highred = game[0]['red']
    power = highblue * highred * highgreen
    return power


def main(filename):
    idtotal = 0
    powertotal = 0
    games_list = parse_input(filename)
    for game in games_list:
        if check_game(game[1]):
            idtotal += game[0]
        powertotal += find_power(game[1])
    print('id total: ' + str(idtotal))
    print('power total: ' + str(powertotal))


main("input/day02.txt")


print("day 02")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))