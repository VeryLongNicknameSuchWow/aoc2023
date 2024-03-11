import math


def parse_input(lines):
    games = {}

    for line in lines:
        game_data = line.split(':')
        game_id = int(game_data[0].split(' ')[1])
        rounds_str = game_data[1].split(';')

        rounds = []
        for round_str in rounds_str:
            round_data = {}
            for subset_str in round_str.strip().split(','):
                subset_str_split = subset_str.strip().split()
                round_data[subset_str_split[1]] = int(subset_str_split[0])
            rounds.append(round_data)
        games[game_id] = rounds

    return games


def part1(games):
    result = 0

    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    def is_game_valid(game_rounds):
        for round_data in game_rounds:
            for color, amount in round_data.items():
                if amount > limits[color]:
                    return False
        return True

    for game_id, rounds_data in games.items():
        if is_game_valid(rounds_data):
            result += game_id

    return result


def part2(games):
    result = 0

    for game_id, rounds_data in games.items():
        limits = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for round_data in rounds_data:
            for color, amount in round_data.items():
                current_limit = limits[color]
                limits[color] = max(amount, current_limit)

        result += math.prod(limits.values())

    return result


if __name__ == '__main__':
    def main():
        with open('day2.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        games = parse_input(lines)
        print(part1(games))
        print(part2(games))


    main()
