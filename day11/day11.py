def parse(lines):
    arr = [line.strip() for line in lines]
    rows = len(arr)
    cols = len(arr[0])

    empty_rows = set()
    for i in range(rows):
        if all(c == '.' for c in arr[i]):
            empty_rows.add(i)

    empty_columns = set()
    for i in range(cols):
        if all(row[i] == '.' for row in arr):
            empty_columns.add(i)

    stars = []
    for row in range(rows):
        for col in range(cols):
            if arr[row][col] == '#':
                stars.append((row, col))

    return empty_columns, empty_rows, stars


def solve(parsed, expansion):
    empty_columns, empty_rows, stars = parsed

    result = 0
    for i, (r1, c1) in enumerate(stars):
        for (r2, c2) in stars[i + 1:]:
            min_r, max_r = min(r1, r2), max(r1, r2)
            min_c, max_c = min(c1, c2), max(c1, c2)
            distance = max_r - min_r + max_c - min_c

            for row in range(min_r + 1, max_r, 1):
                if row in empty_rows:
                    distance += expansion

            for col in range(min_c + 1, max_c, 1):
                if col in empty_columns:
                    distance += expansion

            result += distance
    return result


if __name__ == '__main__':
    def main():
        with open('day11.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        parsed = parse(lines)
        print(solve(parsed, 1))
        print(solve(parsed, 999999))


    main()
