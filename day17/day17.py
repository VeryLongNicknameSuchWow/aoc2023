from heapq import heappop, heappush

import numpy as np


def parse(lines):
    return np.array([[int(c) for c in line.strip()] for line in lines]).transpose()


def lowest_heat_loss(graph, min_steps, max_steps):  # Dijkstra <3
    pq = [(0, (0, 0), (0, 0))]
    visited = set()
    while pq:
        heat, (x, y), (pdx, pdy) = heappop(pq)
        if (x, y) == (graph.shape[0] - 1, graph.shape[1] - 1):
            return heat

        if (x, y, pdx, pdy) in visited:
            continue
        visited.add((x, y, pdx, pdy))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (dx, dy) == (pdx, pdy) or (dx, dy) == (-pdx, -pdy):
                continue

            new_heat = heat
            for steps in range(1, max_steps + 1):
                new_x, new_y = x + dx * steps, y + dy * steps
                if 0 <= new_x < graph.shape[0] and 0 <= new_y < graph.shape[1]:
                    new_heat += graph[new_x, new_y]
                    if steps >= min_steps:
                        heappush(pq, (new_heat, (new_x, new_y), (dx, dy)))


def part1(graph):
    return lowest_heat_loss(graph, 1, 3)


def part2(graph):
    return lowest_heat_loss(graph, 4, 10)


if __name__ == '__main__':
    def main():
        with open('day17.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        graph = parse(lines)
        print(part1(graph))
        print(part2(graph))


    main()
