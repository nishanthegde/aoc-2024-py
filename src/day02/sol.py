def parse_input(file):
    return_reports = []
    with open(file) as f:
        reports = [line.strip() for line in f]

    for report in reports:
        levels = report.split()
        return_reports.append([int(level) for level in levels])

    return return_reports


def all_increasing(report):
    res = True
    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            res = False
            break
    return res


def all_decreasing(report):
    res = True
    for i in range(len(report) - 1):
        if report[i] <= report[i + 1]:
            res = False
            break
    return res


def calc_part1(reports):
    safe_count = 0

    for report in reports:
        safe = True
        # print(report)

        diffs = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]

        if not all(1 <= level <= 3 for level in diffs):
            safe = False

        # print(all_increasing, all_decreasing)
        if not all_increasing(report) and not all_decreasing(report):
            safe = False

        if safe:
            safe_count += 1
            # print(safe_count)

    return safe_count


def check_safe(report):
    safe = True

    diffs = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
    if not all(1 <= level <= 3 for level in diffs):
        safe = False
        return safe

    if not all_increasing(report) and not all_decreasing(report):
        safe = False
        return safe

    return safe


def calc_part2(reports):
    safe_count = 0
    for report in reports:
        # print(report)
        if check_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                report_damp = report[:i] + report[i + 1 :]
                if check_safe(report_damp):
                    safe_count += 1
                    break

    return safe_count


def main():
    filename = "../../inputs/day02.txt"
    reports = parse_input(filename)
    safe_count = calc_part1(reports)
    safe_count = calc_part2(reports)


if __name__ == "__main__":
    main()
