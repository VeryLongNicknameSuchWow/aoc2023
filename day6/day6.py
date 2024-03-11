import math


def parse(lines):
    times = list(map(int, lines[0].split(':')[1].strip().split()))
    distances = list(map(int, lines[1].split(':')[1].strip().split()))
    return times, distances


def part1(times, distances):
    result = 1

    for time, distance in zip(times, distances):
        # find the number of integer solutions of:
        # distance < t * (time - t)
        discriminant = math.sqrt(time ** 2 - 4 * distance)
        t1 = (time + discriminant) / 2
        t2 = (time - discriminant) / 2
        t1, t2 = min(t1, t2), max(t1, t2)

        # strict inequality
        if t1.is_integer():
            t1 += 1
        t1 = math.ceil(t1)

        if t2.is_integer():
            t2 -= 1
        t2 = math.floor(t2)

        result *= t2 - t1 + 1
    return result


def part2(times, distances):
    times = [int(''.join(map(str, times)))]
    distances = [int(''.join(map(str, distances)))]
    return part1(times, distances)


if __name__ == '__main__':
    def main():
        with open('day6.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        times, distances = parse(lines)
        print(part1(times, distances))
        print(part2(times, distances))


    main()
