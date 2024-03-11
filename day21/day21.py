from collections import deque

import numpy as np


def parse(lines):
    arr = np.array([list(line.strip()) for line in lines])
    start = np.where(arr == 'S')
    return arr, (start[0][0], start[1][0])


def part1(arr, start, steps):
    n = arr.shape[0]

    result = 0
    queue = deque([(start[0], start[1], 1)])
    visited = set()
    while queue:
        x, y, step = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if not 0 <= new_x < n or not 0 <= new_y < n:
                continue
            if arr[new_x, new_y] != '#' and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                if step < steps:
                    queue.append((new_x, new_y, step + 1))
                if step % 2 == 0:
                    result += 1
    return result


def part2(arr, start, steps):
    # https://www.reddit.com/r/adventofcode/comments/18ofc8i/2023_day_21_part_2_intuition_behind_solution/
    n = arr.shape[0]
    remainder = steps % n
    ys = {remainder + i * n: 0 for i in range(3)}
    bound = remainder + 2 * n

    total = [0, 0]
    queue = deque([(start[0], start[1], 1)])
    visited = set()
    while queue:
        x, y, step = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if arr[new_x % n, new_y % n] != '#' and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                if step < bound:
                    queue.append((new_x, new_y, step + 1))
                total[step % 2] += 1
        if step in ys:
            ys[step] = total[step % 2]

    coefficients = np.polyfit([0, 1, 2], list(ys.values()), deg=2)
    y_final = np.polyval(coefficients, steps // n)
    return y_final.round().astype(int)


if __name__ == '__main__':
    def main():
        with open('day21.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
            arr, start = parse(lines)
            print(part1(arr, start, 64))
            print(part2(arr, start, 26501365))


    main()
