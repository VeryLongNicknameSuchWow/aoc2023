import operator

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
max_card_value = len(cards) + 1
card_strength_map = {card: max_card_value - i for i, card in enumerate(cards)}


def parse(lines):
    parsed = []

    for line in lines:
        split = line.split(' ')
        hand = split[0].strip()
        bet = int(split[1])
        card_counts = [hand.count(card) for card in cards if card in hand]
        card_counts.sort(reverse=True)
        jokers = hand.count('J')
        parsed.append((hand, card_counts, jokers, bet))

    return parsed


def solve(parsed, overrides, use_jokers):
    def hand_strength(card_counts, wildcards=0):
        if 0 < wildcards < 5:
            card_counts.remove(wildcards)
            card_counts[0] += wildcards

        if 5 in card_counts:
            return 50
        if 4 in card_counts:
            return 40
        if 3 in card_counts:
            if 2 in card_counts:
                return 32
            return 30
        pair_count = card_counts.count(2)
        if pair_count == 2:
            return 22
        if pair_count == 1:
            return 20
        return 10

    def individual_strength(hand):
        strength = 0
        for card in hand:
            strength += overrides.get(card, card_strength_map[card])
            strength *= max_card_value
        return strength

    values = [
        (
            hand_strength(card_counts, jokers if use_jokers else 0),
            individual_strength(hand),
            bet,
        ) for hand, card_counts, jokers, bet in parsed
    ]
    values.sort(key=operator.itemgetter(0, 1))

    return sum((i + 1) * bet for i, (_, _, bet) in enumerate(values))


if __name__ == '__main__':
    def main():
        with open('day7.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        parsed = parse(lines)
        print(solve(parsed, {}, False))
        print(solve(parsed, {'J': 1}, True))


    main()
