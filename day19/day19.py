import copy
import math


def parse(text_input):
    workflows_lines, ratings_lines = text_input.strip().split('\n\n')
    workflows = {}
    for w in workflows_lines.split('\n'):
        workflow_name, workflow_flow = w.split('{')
        workflow_flow = workflow_flow[:-1].split(',')
        workflows[workflow_name] = workflow_flow

    ratings = []
    ratings_lines = ratings_lines.split()
    for r in ratings_lines:
        assignments = r[1:-1].split(',')
        state = {}
        for assignment in assignments:
            name, value = assignment.split('=')
            state[name] = int(value)
        ratings.append(state)

    return workflows, ratings


def part1(parsed):
    workflows, ratings = parsed

    def execute(state, workflow):
        if workflow in ['A', 'R']:
            return workflow

        for routine in workflows[workflow]:
            if '>' in routine:
                conditional, next_routine = routine.split(':')
                var, value = conditional.split('>')
                if state[var] > int(value):
                    return execute(state, next_routine)
            elif '<' in routine:
                conditional, next_routine = routine.split(':')
                var, value = conditional.split('<')
                if state[var] < int(value):
                    return execute(state, next_routine)
            else:
                return execute(state, routine)

    result = 0
    for initial_state in ratings:
        if execute(initial_state, 'in') == 'A':
            result += sum(initial_state.values())
    return result


def part2(parsed):
    workflows, _ = parsed

    def execute(current_state, workflow):
        if workflow in ['A', 'R']:
            counts = [(b - a + 1) for a, b in current_state.values()]
            if workflow == 'A' and all(count > 0 for count in counts):
                return math.prod(counts)
            return 0

        result = 0
        for routine in workflows[workflow]:
            if '>' in routine:
                operator = '>'
            elif '<' in routine:
                operator = '<'
            else:
                result += execute(current_state, routine)
                continue

            conditional, next_routine = routine.split(':')
            var, value = conditional.split(operator)
            value = int(value)
            var_min, var_max = current_state[var]
            new_state = copy.deepcopy(current_state)

            if operator == '>':
                new_state[var] = max(var_min, value + 1), var_max
                current_state[var] = var_min, min(var_max, value)
            else:
                new_state[var] = var_min, min(var_max, value - 1)
                current_state[var] = max(var_min, value), var_max

            result += execute(new_state, next_routine)
        return result

    initial_state = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000),
    }
    return execute(initial_state, 'in')


if __name__ == '__main__':
    def main():
        with open('day19.txt', 'r') as puzzle_input:
            text_input = puzzle_input.read()
        parsed = parse(text_input)
        print(part1(parsed))
        print(part2(parsed))


    main()
