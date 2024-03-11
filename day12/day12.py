from functools import cache
from typing import Tuple


def parse(lines):
    parsed = []
    for line in lines:
        split_line = line.strip().split()
        parsed.append((split_line[0], tuple(map(int, split_line[1].split(',')))))
    return parsed


@cache
def count_valid(springs: str, groups: Tuple[int]) -> int:
    n_springs = len(springs)
    n_groups = len(groups)

    if n_springs == 0:
        # if there are no more groups to match the string is valid
        return 0 if n_groups != 0 else 1

    match springs[0]:
        case '#':
            # no groups left or string can't contain the current group
            if n_groups == 0 or n_springs < groups[0]:
                return 0

            # current group is invalid
            if '.' in springs[:groups[0]]:
                return 0

            # current group is longer
            if springs[groups[0]:].startswith('#'):
                return 0

            # '?' can be a separator
            if n_springs > groups[0] and springs[groups[0]] == '?':
                return count_valid(springs[groups[0] + 1:].lstrip('.'), groups[1:])

            # check the rest of the string
            return count_valid(springs[groups[0]:].lstrip('.'), groups[1:])
        case '.':
            # trim dots and check rest
            return count_valid(springs.lstrip('.'), groups)
        case '?':
            # check both replacement possibilities
            return count_valid('#' + springs[1:], groups) + count_valid('.' + springs[1:], groups)


def part1(parsed):
    return sum(count_valid(springs, groups) for springs, groups in parsed)


def part2(parsed):
    result = 0

    for springs, groups in parsed:
        big_springs = '?'.join([springs for _ in range(5)])
        big_groups = groups * 5
        result += count_valid(big_springs, big_groups)

    return result


if __name__ == '__main__':
    def main():
        with open('day12.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        parsed = parse(lines)
        print(part1(parsed))
        print(part2(parsed))


    main()
