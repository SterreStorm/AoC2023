from time import time_ns

start_time = time_ns()


def parse_input(filename):
    histories = []
    with open(filename) as file:
        for i, line in enumerate(file):
            histories.append([[int(x) for x in line.split()]])
    return histories


def find_zeroes(history):
    new_list = history[0]
    finished = False
    i = 1
    while not finished:
        working = new_list
        new_list = [working[j + 1] - working[j] for j in range(len(working) - 1)]
        history.append(new_list)
        finished = all(x == 0 for x in new_list)
        i += 1
    return history


def find_next_number(history, backwards):
    for i in range(len(history) - 1, 0, -1):
        if backwards:
            first_digit_working_range = history[i][0]
            first_digit_previous_range = history[i-1][0]
            history[i-1].insert(0, first_digit_previous_range - first_digit_working_range)
        else:
            last_digit_working_range = history[i][-1]
            last_digit_previous_range = history[i-1][-1]
            history[i-1].append(last_digit_previous_range + last_digit_working_range)
    returnvalue = history[0][0] if backwards else history[0][-1]
    return returnvalue


def main(filename):
    histories = parse_input(filename)
    totalsum = 0
    backwards = 0
    for history in histories:
        history = find_zeroes(history)
        totalsum += find_next_number(history, False)
        backwards += find_next_number(history, True)
    print(f"part 1: {totalsum}")
    print(f"part 2: {backwards}")


main("Input/day09.txt")

print("day 09")
print("--- %s ms ---" % ((time_ns() - start_time)/1000000))
