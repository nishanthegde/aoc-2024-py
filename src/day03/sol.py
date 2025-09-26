import re


def parse_input(file):
    with open(file) as f:
        lines = [line.strip() for line in f]

    return lines


def extract_mul_result(lines):
    pattern = r"mul\((\d+),(\d+)\)"
    mul_result = 0

    for line in lines:
        match_iterator = re.finditer(pattern, line)
        for match in match_iterator:
            mul_result += int(match.group(1)) * int(match.group(2))

    return mul_result


def extract_enabled_mul_result(lines):
    pattern = r"\bdon't\b|\bdo\b|mul\((\d+),(\d+)\)"
    mul_result = 0
    enabled = True

    for line in lines:
        match_iterator = re.finditer(pattern, line)
        for match in match_iterator:
            if match.group(0) == "don't":
                enabled = False
            elif match.group(0) == "do":
                enabled = True
            elif enabled and match.group(0).startswith("mul"):
                mul_result += int(match.group(1)) * int(match.group(2))

    return mul_result


def main():
    file = "../../inputs/day03.txt"
    # file = "../../inputs/day03_sample.txt"
    # file = "../../inputs/day03_sample_2.txt"
    lines = parse_input(file)
    res = extract_mul_result(lines)
    print(res)

    res = extract_enabled_mul_result(lines)
    print(res)


if __name__ == "__main__":
    main()
