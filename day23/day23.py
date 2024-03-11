from collections import deque

import numpy as np


def parse(lines):
    return np.array([list(line.strip()) for line in lines])


def part1(arr):
    start = (0, 1)
    queue = deque([(start, [start])])

    result = 0
    while queue:
        (x, y), path = queue.pop()

        if x == arr.shape[1] - 1:
            result = max(result, len(path) - 1)

        for dx, dy, allowed in [(1, 0, 'v'), (-1, 0, '^'), (0, 1, '>'), (0, -1, '<')]:
            neighbour = n_x, n_y = x + dx, y + dy
            if not 0 <= n_x < arr.shape[0] or not 0 <= n_y < arr.shape[1] or neighbour in path:
                continue

            if arr[neighbour] == '.' or arr[neighbour] == allowed:
                queue.append((neighbour, path + [neighbour]))

    return result


def part2(arr):
    start = (0, 1)
    queue = deque([(start, [start])])

    result = 0
    while queue:
        (x, y), path = queue.pop()

        if x == arr.shape[1] - 1:
            result = max(result, len(path) - 1)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbour = n_x, n_y = x + dx, y + dy
            if not 0 <= n_x < arr.shape[0] or not 0 <= n_y < arr.shape[1] or neighbour in path:
                continue

            if arr[neighbour] != '#':
                queue.append((neighbour, path + [neighbour]))

    return result


if __name__ == '__main__':
    def main():
        with open('day23.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        arr = parse(lines)
        print(part1(arr))
        print(part2(arr))


    main()
