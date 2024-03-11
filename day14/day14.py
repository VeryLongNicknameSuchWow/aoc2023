import numpy as np


def parse(lines):
    return np.array([list(line.strip()) for line in lines])


def tilt(arr):
    n_rows, n_cols = arr.shape

    for col in range(n_cols):
        segment = arr[:, col]
        separator_indices = np.where(segment == '#')[0]
        segment_starts = np.concatenate(([0], separator_indices + 1))
        segment_ends = np.concatenate((separator_indices, [n_rows]))

        for start, end in zip(segment_starts, segment_ends):
            segment_slice = segment[start:end]
            num_rocks = np.count_nonzero(segment_slice == 'O')
            segment_slice[:num_rocks] = 'O'
            segment_slice[num_rocks:] = '.'
    return arr


def get_load(arr):
    rock_positions = np.where(arr == 'O')
    return np.sum(arr.shape[0] - rock_positions[0])


def part1(arr):
    return get_load(tilt(arr))


def run_cycle(arr):
    for _ in range(4):
        arr = tilt(arr)
        arr = np.rot90(arr, k=-1)
    return arr


def run_cycles(arr, cycles):
    seen_states = {}
    cycle_count = 0

    while cycle_count < cycles:
        state_key = arr.tobytes()
        if state_key in seen_states:
            cycle_period = cycle_count - seen_states[state_key]
            remaining_cycles = (cycles - cycle_count) % cycle_period
            return run_cycles(arr, remaining_cycles)

        seen_states[state_key] = cycle_count
        arr = run_cycle(arr)
        cycle_count += 1
    return arr


def part2(arr):
    return get_load(run_cycles(arr, 1000000000))


if __name__ == '__main__':
    def main():
        with open('day14.txt', 'r') as puzzle_input:
            lines = puzzle_input.readlines()
        arr = parse(lines)
        print(part1(arr))
        print(part2(arr))


    main()
