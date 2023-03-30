
def Line():
    print("===============================")
def parse_line(line: str) -> tuple:
    items = line.split()
    if len(items) < 4:
        raise ValueError(f'Not enough values to unpack (expected at least 4, got {len(items)})')
    _, country, area, population = items

    return country, area, population

def sort_by_area(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(parse_line(line))
    data = sorted(data, key=lambda x: float(x[1]), reverse=True)
    return data

def sort_by_population(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(parse_line(line))
    data = sorted(data, key=lambda x: float(x[2]), reverse=True)
    return data
def main(file_name):
    res = sort_by_area(file_name)
    counter = 1
    for item in res:
        print(f'{counter}) {item}')
        counter += 1
    Line()
    counter = 1
    res1 = sort_by_population(file_name)
    for item in res1:
        print(f'{counter}) {item}')
        counter += 1

if __name__ == '__main__':
    main('population.txt')