import time

start_time = time.time_ns()

vertaaltabel = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"}


def first_digit(line):
    for i, digit in enumerate(line):
        if digit.isdigit():
            return digit
        for word in vertaaltabel:
            revword = word[::-1]
            if digit == word[0] or digit == revword[0]:
                if line[i:i+len(word)] == word or line[i:i+len(word)] == revword:
                    return vertaaltabel[word]


def main(filename):
    with open(filename) as inp:
        total = 0
        for line in inp:
            combi_int = int(first_digit(line) + first_digit(line[::-1]))
            total += combi_int
    print(total)


main("input/day01.txt")

print("day 01")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
