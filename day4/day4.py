def parse(lines):
    cards = []

    for line in lines:
        line_split = line.split(':')
        line_split = line_split[1].strip().split('|')
        winning_numbers = {int(num) for num in line_split[0].strip().split()}
        my_numbers = {int(num) for num in line_split[1].strip().split()}
        cards.append((winning_numbers, my_numbers))

    return cards


def part1(cards):
    result = 0

    for winning_numbers, my_numbers in cards:
        score = 0

        for num in my_numbers:
            if num in winning_numbers:
                if score == 0:
                    score += 1
                else:
                    score *= 2
        result += score

    return result


def part2(cards):
    card_amounts = [1 for _ in cards]

    for index, (winning_numbers, my_numbers) in enumerate(cards):
        matching_numbers = 0
        for num in my_numbers:
            if num in winning_numbers:
                matching_numbers += 1
        for i in range(matching_numbers):
            card_amounts[index + i + 1] += card_amounts[index]

    return sum(card_amounts)


if __name__ == '__main__':
    def main():
        with open('day4.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        cards = parse(lines)
        print(part1(cards))
        print(part2(cards))


    main()
