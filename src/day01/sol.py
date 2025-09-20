def parse_input(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    left = sorted([int(item.split(" ")[0]) for item in lines])
    right = sorted([int(item.split(" ")[-1]) for item in lines])

    return left, right


def calc_part1(left, right):
    return sum(abs(a - b) for a, b in zip(left, right))


def calc_part2(left, right):
    similarity = 0
    for num in left:
        similarity += num * right.count(num)

    return similarity


def main():
    sample_input_path = "../../inputs/day01_sample.txt"
    input_path = "../../inputs/day01.txt"
    # left, right = parse_input(sample_input_path)
    left, right = parse_input(input_path)

    distance = calc_part1(left, right)
    # print(distance)
    print(calc_part2(left, right))


if __name__ == "__main__":
    main()
