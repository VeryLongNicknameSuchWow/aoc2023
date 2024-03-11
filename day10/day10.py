from collections import defaultdict

from PIL import Image, ImageDraw

tile_connects_to = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    '.': [],
    'S': [(-1, 0), (1, 0), (0, -1), (0, 1)],
}


def parse(lines):
    len_y = len(lines)
    len_x = len(lines[0]) - 1  # account for '\n'

    graph = defaultdict(list)
    start = None
    for y, line in enumerate(lines):
        for x, tile in enumerate(line.strip()):
            if tile == 'S':
                start = (y, x)

            for d in range(-1, 2, 1):
                ny = y + d
                nx = x + d
                if 0 <= ny < len_y:
                    neighbour = lines[ny][x]
                    vector = (d, 0)
                    opposite_vector = (-d, 0)
                    if vector in tile_connects_to[tile] and opposite_vector in tile_connects_to[neighbour]:
                        graph[(y, x)].append((ny, x))
                if 0 <= nx < len_x:
                    neighbour = lines[y][nx]
                    vector = (0, d)
                    opposite_vector = (0, -d)
                    if vector in tile_connects_to[tile] and opposite_vector in tile_connects_to[neighbour]:
                        graph[(y, x)].append((y, nx))

    return start, graph, (len_y, len_x)


def part1(start, graph):
    queue = [start]
    distance = {start: 0}

    # BFS
    while queue:
        current = queue.pop(0)
        current_distance = distance[current]

        for neighbour in graph[current]:
            if neighbour not in distance:
                distance[neighbour] = current_distance + 1
                queue.append(neighbour)

    # Remove vertices disconnected from S point (for part 2)
    for k in [k for k in graph.keys()]:
        if k not in distance:
            graph.pop(k)

    return max(distance.values())


def visualize(filename, shape, graph, draw_spots=False, fill_outside=False, draw_border=False):
    len_y, len_x = shape

    pixel_size = 3
    img = Image.new('RGB', (len_x * pixel_size, len_y * pixel_size), 'black')
    draw = ImageDraw.Draw(img, 'RGBA')

    pixels = {}
    for (y, x), neighbours in graph.items():
        pixels[(x * pixel_size, y * pixel_size)] = 'white'
        for (ny, nx) in neighbours:
            dy, dx = ny - y, nx - x
            pixels[(x * pixel_size + dx, y * pixel_size + dy)] = 'white'

    if draw_spots:
        for y in range(len_y):
            middle_y = y * pixel_size
            for x in range(len_x):
                middle_x = x * pixel_size
                is_empty = True
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (middle_x + dx, middle_y + dy) in pixels:
                            is_empty = False
                            break
                    if not is_empty:
                        break

                if is_empty:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            pixels[(middle_x + dx, middle_y + dy)] = 'red'
                    pixels[(middle_x, middle_y)] = 'orange'

    for (x, y), color in pixels.items():
        draw.point((x, y), fill=color)

    if fill_outside:
        for _ in range(3):
            ImageDraw.floodfill(img, (1, 1), (0, 0, 0), thresh=50)
            ImageDraw.floodfill(img, (1, 1), (255, 0, 0), thresh=50)
        ImageDraw.floodfill(img, (1, 1), (0, 0, 255), thresh=50)

    if draw_border:
        draw.rectangle(
            (
                len_x * pixel_size * 1 // 4,
                len_y * pixel_size * 1 // 4,
                len_x * pixel_size * 3 // 4,
                len_y * pixel_size * 3 // 4
            ),
            fill=(0, 255, 0, 80),
            outline=(0, 255, 0, 120),
            width=1,
        )

    img.save(filename)


def part2(lines, shape, graph):
    lx = shape[0] // 4
    ly = shape[1] // 4

    result = 0
    for y, line in enumerate(lines[ly:-ly]):
        y += ly
        for x, tile in enumerate(line[lx:-lx]):
            x += lx
            if (y, x) not in graph.keys():
                result += 1
    return result


if __name__ == '__main__':
    def main():
        with open('day10.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        start, graph, shape = parse(lines)

        # visualize the input with disconnected pipes (part1 removes them)
        visualize('1.png', shape, graph)
        print(part1(start, graph))

        # without disconnected pipes and show empty spots
        visualize('2.png', shape, graph)
        visualize('3.png', shape, graph, True)

        # solve part2 visually using floodfill XD
        visualize('4.png', shape, graph, True, True)
        visualize('5.png', shape, graph, True, True, True)

        # get the number
        print(part2(lines, shape, graph))


    main()
