import numpy as np


def parse(file):
    return [np.array(list(map(list, case.split('\n')))) for case in file.strip().split('\n\n')]


def process(arr, mismatches):
    def check(a, b):
        sub_arr = arr[a:b, :]
        rev_sub_arr = sub_arr[::-1, :]
        if np.sum(np.not_equal(sub_arr, rev_sub_arr)) == mismatches:
            mid = (b + 1 - a) // 2
            return mid if a == 0 else arr.shape[0] - mid
        return 0

    return sum(
        check(start, arr.shape[0])
        for start in range(1, arr.shape[0] - 1, 2)
    ) + sum(
        check(0, end)
        for end in range(2, arr.shape[0] + 1, 2)
    )


def solve(parsed, mismatches):
    return sum(100 * process(case, mismatches) + process(case.transpose(), mismatches) for case in parsed)


if __name__ == '__main__':
    def main():
        with open('day13.txt', 'r') as puzzle_input:
            file = puzzle_input.read()
        parsed = parse(file)
        print(solve(parsed, 0))
        print(solve(parsed, 2))


    main()
