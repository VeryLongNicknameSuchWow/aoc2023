def part1(lines):
    result = 0

    for line in lines:
        first_digit = None
        last_digit = None

        for char in line:
            if char.isnumeric():
                value = int(char)
                if first_digit is None:
                    first_digit = value
                last_digit = value

        result += first_digit * 10 + last_digit

    return result


def part2(lines):
    digits_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    result = 0

    for line in lines:
        first_digit = None
        last_digit = None

        for i, char in enumerate(line):
            if char.isnumeric():
                value = int(char)
                if first_digit is None:
                    first_digit = value
                last_digit = value
                continue

            # Jebać złożność obliczeniową AUUUUUUUUUUU
            for word, value in digits_map.items():
                if line.startswith(word, i):
                    if first_digit is None:
                        first_digit = value
                    last_digit = value

        result += first_digit * 10 + last_digit

    return result


if __name__ == '__main__':
    def main():
        with open('day1.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
            print(part1(lines))
            print(part2(lines))


    main()
