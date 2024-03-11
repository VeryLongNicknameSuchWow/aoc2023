import math


def parse(lines):
    symbol_type_dict = {}

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line.strip()):
            if not char.isnumeric() and not char == '.':
                symbol_type_dict[(line_index, char_index)] = char

    def get_adjacent_symbol(line_index, char_index):
        for (symbol_line_index, symbol_char_index), symbol in symbol_type_dict.items():
            if abs(symbol_line_index - line_index) <= 1 and abs(symbol_char_index - char_index) <= 1:
                return (symbol_line_index, symbol_char_index), symbol
        return None

    symbol_adjacent_dict = {key: list() for key in symbol_type_dict.keys()}
    for line_index, line in enumerate(lines):
        number = None
        adjacent_symbol = None
        for char_index, char in enumerate(line):
            if not char.isnumeric():
                if number is not None and adjacent_symbol is not None:
                    symbol_adjacent_dict[adjacent_symbol[0]].append(number)
                number = None
                adjacent_symbol = None
                continue

            possible_symbol = get_adjacent_symbol(line_index, char_index)
            if possible_symbol is not None:
                adjacent_symbol = possible_symbol

            if number is None:
                number = int(char)
            else:
                number *= 10
                number += int(char)
    return symbol_type_dict, symbol_adjacent_dict


def part1(symbol_adjacent_dict):
    result = 0
    for adjacent_numbers in symbol_adjacent_dict.values():
        result += sum(adjacent_numbers)
    return result


def part2(symbol_type_dict, symbol_adjacent_dict):
    result = 0
    for symbol_dimensions, adjacent_numbers in symbol_adjacent_dict.items():
        if symbol_type_dict[symbol_dimensions] == '*':
            if len(adjacent_numbers) == 2:
                result += math.prod(adjacent_numbers)
    return result


if __name__ == '__main__':
    def main():
        with open('day3.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        symbol_type_dict, symbol_adjacent_dict = parse(lines)
        print(part1(symbol_adjacent_dict))
        print(part2(symbol_type_dict, symbol_adjacent_dict))


    main()
