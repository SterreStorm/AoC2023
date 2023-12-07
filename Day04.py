import time

start_time = time.time_ns()
def parse_input(filename):
    kaartjesbieb = {}
    with open(filename) as file:
        for i, line in enumerate(file):
            winningcard, entry = line.split(" | ")
            entry = entry.strip("\n").split(" ")
            winning_card = winningcard.split(": ")[1].split(" ")
            entry = [int(i) for i in entry if i != ""]
            winning_card = [int(i) for i in winning_card if i != ""]
            kaartjesbieb[i] = [entry, winning_card]
    return kaartjesbieb


def wins_and_points(biebjen):
    kaart_win_punten = {}
    total_points = 0
    for i in biebjen:
        cardnumber = i
        cardset = biebjen[cardnumber]
        winning_numbers = []
        entry = cardset[0]
        winning_card = cardset[1]
        for number in winning_card:
            if number in entry:
                winning_numbers.append(number)
        boolean_win = len(winning_numbers) > 0
        len_nums = len(winning_numbers)
        points = 2 ** (len_nums - 1) if boolean_win else 0
        total_points += points
        kaart_win_punten[cardnumber] = [len_nums, 1]

    return total_points, kaart_win_punten


def kaartjes_tellen(puntjesbieb):
    totalsum = 0
    for i in puntjesbieb:
        winning_numbers, aantal_copies = puntjesbieb[i]
        totalsum += aantal_copies
        for j in range(i + 1, i + winning_numbers + 1):
            templist = puntjesbieb[j]
            templist[1] = templist[1] + aantal_copies
            puntjesbieb[j] = templist
    return(totalsum)


def main(filename):
    biebjen = parse_input(filename)
    totaal, puntjensbieb = wins_and_points(biebjen)
    kaartjes = kaartjes_tellen(puntjensbieb)
    print("total points: " + str(totaal))
    print("total cards: " + str(kaartjes))


main("input/day04.txt")

print("day 04")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))
