def parse(lines):
    return [list(map(int, line.strip().split())) for line in lines]


def solve(parsed):
    part1 = part2 = 0
    for case in parsed:
        sgn = 1
        while any(num != 0 for num in case):
            part1 += case[-1]
            part2 += sgn * case[0]
            sgn *= -1
            case = [b - a for a, b in zip(case, case[1:])]
    return part1, part2


if __name__ == '__main__':
    def main():
        with open('day9.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        parsed = parse(lines)
        print(solve(parsed))


    main()
