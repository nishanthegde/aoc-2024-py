def parse_input(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    left = sorted([int(item.split(" ")[0]) for item in lines])
    right = sorted([int(item.split(" ")[-1]) for item in lines])

    return left, right


def calc_part1(left, right):
    distance = [abs(a - b) for a, b in zip(left, right)]

    return sum(distance)


def main():
    sample_input_path = "../../inputs/day01_sample.txt"
    input_path = "../../inputs/day01.txt"
    left, right = parse_input(input_path)

    distance = calc_part1(left, right)
    print(distance)


if __name__ == "__main__":
    main()
