
def find_J(hand):
    return True if "J" in hand else False


def evaluate_hand(hand):
    groups = len(hand)
    first_list = hand[0]
    hand_j = sorted(hand, key=find_J, reverse=True)[0]
    num_of_J = len(hand_j) if "J" in hand_j else 0

    if groups == 1:
        hand_type = 1
    elif groups == 2:
        hand_type = 1 if num_of_J > 0 else 2 if len(first_list) == 4 else 3
    elif groups == 3:
        if len(first_list) == 3:
            hand_type = 4 if num_of_J == 0 else 2
        else:
            hand_type = 5 if num_of_J == 0 else 3 if num_of_J == 1 else 2
    elif groups == 4:
        hand_type = 6 if (num_of_J == 0) else 4
    else:
        hand_type = 7 if num_of_J == 0 else 6
    return hand_type


def sort_hand(hand):
    sorted_list = {}
    for character in hand:
        sorted_list.setdefault(character, []).append(character)
    return list(sorted_list.values())


def parse_input(filename):
    hands_and_bids = {}
    with open(filename) as file:
        for line in file:
            hand, bid = line.split()
            sorted_hand = sorted(hand)
            sorted_hand = sort_hand(sorted_hand)
            sorted_hand.sort(key=len, reverse=True)
            hand_type = evaluate_hand(sorted_hand)
            hands_and_bids.setdefault(hand_type, []).append([hand, int(bid)])
    return dict(sorted(hands_and_bids.items(), key=None, reverse=True))


def sort_cards(hand):
    hand = hand[0]
    # c = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] pt 1
    c = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']  # pt 2
    return c.index(hand[0]), c.index(hand[1]), c.index(hand[2]), c.index(hand[3]), c.index(hand[4])


def main(filename):
    hands_and_bids = parse_input(filename)
    final_ranking = []
    final_total = 0
    for hand_types in hands_and_bids:
        final_ranking += sorted(hands_and_bids[hand_types], key=sort_cards)
    for i, combo in enumerate(final_ranking):
        final_total += (combo[1] * (i + 1))
    print(final_total)


main("input/Day07.txt")
