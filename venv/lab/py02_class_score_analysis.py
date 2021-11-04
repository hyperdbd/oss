import csv
import pandas as pd


def read_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        data = []
        for row in reader:
            data.append([int(x) for x in row])
    return data
    # TODO


def add_weighted_average(data, weight):
    for row in data:
        weighted = sum(a * b for a, b in zip(row, weight))
        row.append(weighted)  # TODO


def analyze_data(data):
    analyze = pd.DataFrame(data)
    mean = analyze.stack().mean()  # TODO
    var = analyze.stack().var(ddof=0) # TODO
    median = analyze.stack().median()  # TODO
    return mean, var, median, min(data), max(data)


if __name__ == '__main__':
    data = read_data('../data/class_score_en.csv')
    if data and len(data[0]) == 2:
        add_weighted_average(data, [40 / 125, 60 / 100])
        if len(data[0]) == 3:
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [[row[c] for row in data] for c in range(col_n)]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')
