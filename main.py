

def parse_line(line: str) -> tuple:
    items = line.split()
    if len(items) < 4:
        raise ValueError(f'Not enough values to unpack (expected at least 4, got {len(items)})')
    _, country, area, population = items
    area = float(area)

    return country, area, population


def main(file_name):


if __name__ == '__main__':
    main('population.txt')