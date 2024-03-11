def parse(lines):
    def to_vector(x):
        match x:
            case 'R' | 0:
                return 1, 0
            case 'D' | 1:
                return 0, 1
            case 'L' | 2:
                return -1, 0
            case 'U' | 3:
                return 0, -1

    parsed = []
    for line in lines:
        words = line.split()
        color = words[2][2:-1]
        parsed.append((to_vector(words[0]), int(words[1]), int(color[:5], 16), to_vector(int(color[5:], 16))))
    return parsed


def solve(parsed, vector_i, steps_i):
    x, y = 0, 0
    points = [(x, y)]

    perimeter = 0
    for data in parsed:
        (dx, dy) = data[vector_i]
        steps = data[steps_i]

        x += dx * steps
        y += dy * steps
        points.append((x, y))
        perimeter += steps

    area = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(points, points[1:])) // 2
    return area + perimeter // 2 + 1


def part1(parsed):
    return solve(parsed, 0, 1)


def part2(parsed):
    return solve(parsed, 3, 2)


if __name__ == '__main__':
    def main():
        with open('day18.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        parsed = parse(lines)
        print(part1(parsed))
        print(part2(parsed))


    main()
