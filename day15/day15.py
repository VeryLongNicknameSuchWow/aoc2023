from collections import defaultdict


def parse(text_input):
    return text_input.strip().split(',')


def hash_str(label):
    result = 0
    for char in label:
        result += ord(char)
        result *= 17
        result %= 256
    return result


def part1(parsed):
    return sum(hash_str(label) for label in parsed)


def part2(parsed):
    boxes = defaultdict(dict)
    for instruction in parsed:
        if '-' in instruction:
            label, _ = instruction.split('-')
            boxes[hash_str(label)].pop(label, None)
        elif '=' in instruction:
            label, focal = instruction.split('=')
            boxes[hash_str(label)][label] = int(focal)
    return sum(
        (box_i + 1) * (lens_i + 1) * focal
        for box_i, box_content in boxes.items()
        for lens_i, focal in enumerate(box_content.values())
    )


if __name__ == '__main__':
    def main():
        with open('day15.txt', 'r') as puzzle_input:
            text_input = puzzle_input.read()
        parsed = parse(text_input)
        print(part1(parsed))
        print(part2(parsed))


    main()
