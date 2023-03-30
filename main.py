

def parse_line(line: str) -> tuple:
    items = line.split()
    if len(items) < 4:
        raise ValueError(f'Not enough values to unpack (expected at least 4, got {len(items)})')
    _, country, area, population = items
    area = float(area)

    return country, area, population

def sort_by_area(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(parse_line(line))
    data = sorted(data, key=lambda x: float(x[1]), reverse=True)
    return data

def main(file_name):
    res = sort_by_area(file_name)
    for item in res:
        print(f'{item}')

if __name__ == '__main__':
    main('population.txt')