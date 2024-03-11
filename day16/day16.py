from collections import deque

import numpy as np


def parse(lines):
    return np.array([list(line.strip()) for line in lines]).transpose()


def traverse(graph, x, y, dx, dy):
    visited = set()
    energized = set()
    queue = deque([(x, y, dx, dy)])
    while queue:
        (x, y, dx, dy) = queue.popleft()
        x += dx
        y += dy

        if not 0 <= x < graph.shape[0] or not 0 <= y < graph.shape[1] or (x, y, dx, dy) in visited:
            continue

        visited.add((x, y, dx, dy))
        energized.add((x, y))

        match [graph[x, y], dx, dy]:
            case ['.', _, _]:
                queue.append((x, y, dx, dy))
            case ['|', 0, _]:
                queue.append((x, y, dx, dy))
            case ['|', _, _]:
                queue.append((x, y, 0, 1))
                queue.append((x, y, 0, -1))
            case ['-', _, 0]:
                queue.append((x, y, dx, dy))
            case ['-', _, _]:
                queue.append((x, y, 1, 0))
                queue.append((x, y, -1, 0))
            case ['/', _, _]:
                queue.append((x, y, -dy, -dx))
            case ['\\', _, _]:
                queue.append((x, y, dy, dx))
    return len(energized)


def part1(graph):
    return traverse(graph, -1, 0, 1, 0)


def part2(graph):
    result = 0
    for x in range(graph.shape[0]):
        result = max(result, traverse(graph, x, -1, 0, 1))
        result = max(result, traverse(graph, x, graph.shape[1], 0, -1))
    for y in range(graph.shape[1]):
        result = max(result, traverse(graph, -1, 0, 1, 0))
        result = max(result, traverse(graph, graph.shape[0], 0, -1, 0))
    return result


if __name__ == '__main__':
    def main():
        with open('day16.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        graph = parse(lines)
        print(part1(graph))
        print(part2(graph))


    main()
