import math

def parse_input(filename):
    lists = []
    combined = []
    with open(filename) as file:
        for line in file:
            new_string = ""
            line_2 = line.split()
            line = [int(item.strip()) for item in line.split(' ') if item.strip().isdigit()]
            lists.append(line)
            for entry in line_2:
                if entry.isdigit():
                    new_string += entry
            combined.append(int(new_string))
    lists = list(zip(lists[0], lists[1]))
    return lists, combined

    # d = tx - x^2 -> x^2 - tx + d
def calculate_minimum_press(race):
    print(race)
    time_t = race[0]
    record_d = race[1]
    discriminant = (time_t ** 2) - (4 * record_d)
    if discriminant > 0:
        axis_1 = ((time_t - math.sqrt(discriminant))/2)
        axis_2 = ((time_t + math.sqrt(discriminant))/2)
        if axis_1.is_integer():
            axis_1 += 1
        if axis_2.is_integer():
            axis_2 -= 1
        delta = math.floor(axis_2) - math.ceil(axis_1) + 1
    else:
        delta = 0
    return delta

def main(filename):
    list_of_presstimes = []
    time_record, combined = parse_input(filename)
    print(combined)
    for race in time_record:
        list_of_presstimes.append(calculate_minimum_press(race))
    answer = math.prod(list_of_presstimes)
    part_2 = calculate_minimum_press(combined)
    print(f"answer: {answer}")
    print(f"part 2: {part_2}")


main("input/day06.txt")
