import math, time

start_time = time.time_ns()

def form_grid(filename):
    grid = []
    with open(filename) as file:
        for line in file:
            line = line.strip("\n")
            grid.append(line)
    return grid

# def check_line(line, a, b):
#     part = False
#     for x in range(a, b):
#         value = line[x]
#         if not value.isdigit() and value != ".":
#             part = True
#     return part

def check_parts_01(line, upper_line, lower_line):
    line_dict = {}
    last_number_end = -1
    len_line = len(line) - 1
    total = 0
    bool_upper = isinstance(upper_line, str)
    bool_lower = isinstance(lower_line, str)
    for i, digit in enumerate(line):
        #check if start of a number
        if digit.isdigit() and i > last_number_end:
            part = False
            number = digit
            j = i + 1
            #check number length
            while j <= len_line:
                    nextdigit = line[j]
                    if nextdigit.isdigit():
                        number += nextdigit
                        j += 1
                    else:
                        break
            last_number_end = j - 1
            numrange = (i, last_number_end)
            range_i = i - 1 if i > 1 else i
            range_j = j  if len_line >= j else last_number_end
            before = line[range_i]
            after = line[range_j]
            if before != "." and not before.isdigit() and range_i < i:
                part = True
            if after != "." and not after.isdigit() and range_j >= last_number_end:
                part = True
            for x in range(range_i, range_j + 1):
                if bool_upper:
                    value = upper_line[x]
                    if not value.isdigit() and value != ".":
                        part = True
                if bool_lower:
                    value = lower_line[x]
                    if not value.isdigit() and value != ".":
                        part = True
            if part:
                total += int(number)
                line_dict[numrange] = number
    return line_dict, total


def sum_parts(grid):
    part_dict = {}
    parttotal = 0
    for i, line in enumerate(grid):
        upper_line = grid[i - 1] if i > 0 else None
        lower_line = grid[i + 1] if i < len(grid) - 1 else None
        line_parts, total = check_parts_01(line, upper_line, lower_line)
        parttotal += total
        part_dict[i] = line_parts
    return part_dict, parttotal

def part_02(dict_parts, grid):
    total = 0
    for i, line in enumerate(grid):
        numbers_upper =  dict_parts[i - 1] if i > 0 else {}
        numbers_line = dict_parts[i]
        numbers_lower = dict_parts[i + 1] if i < len(grid) - 1 else {}
        dictlist = [numbers_lower, numbers_line, numbers_upper]

        for x, value in enumerate(line):
            if value == "*":
                products = []
                for d in dictlist:
                    keys = d.keys()
                    print(x, keys)
                    for key in keys:
                        num_start = key[0]
                        num_end = key[1]
                        if num_start <= x <= num_end or x == num_end + 1 or x == num_start - 1:
                             products.append(int(d[key]))
                print(products)
                if len(products) == 2:
                    total += math.prod(products)
    return total


def main(filename):
    grid = form_grid(filename)
    dict_parts, parttotal = sum_parts(grid)

    sumpart2 = 0
    sumpart2 += part_02(dict_parts, grid)
    print("sum of parts: " + str(parttotal))
    print("sumpart2: " + str(sumpart2))

    print(dict_parts)


main("input/day03.txt")

print("day 03")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
