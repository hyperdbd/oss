import glob, csv
import matplotlib.pyplot as plt
import numpy


def read_data(filename):
    files = glob.glob(filename)
    all_data = []
    for file in files:
        with open(file, 'r') as f:  # Construct a file object
            csv_reader = csv.reader(f)  # Construct a CSV reader object
            data = []
            for line in csv_reader:
                if line and not line[0].strip().startswith('#'):  # If 'line' is valid and not a header
                    data.append([int(val) for val in line])  # Append 'line' to 'data' as numbers
            all_data = all_data + data  # Merge 'data' to 'all_data'
    return all_data


def add_total(data, weight):
    for row in data:
        total = sum(a * b for a, b in zip(row, weight))
        row.append(total)


if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    total_weight = [40 / 125, 60 / 100]
    add_total(class_kr, total_weight)
    add_total(class_en, total_weight)
    # Derive miterm, final, and total scores
    midtm_kr = []
    final_kr = []
    total_kr = []
    midtm_en = []
    final_en = []
    total_en = []

    for row in class_kr:
        midtm_kr.append(row[0])
        final_kr.append(row[1])
        total_kr.append(row[2])
        # total_kr.append(sum(a * b for a, b in zip(row, total_weight)))

    for row in class_en:
        midtm_en.append(row[0])
        final_en.append(row[1])
        total_en.append(row[2])
        # total_en.append(sum(a * b for a, b in zip(row, total_weight)))

    # Plot midterm/final scores as points

    plt.plot(midtm_kr, final_kr, 'ro', label='Korean')
    plt.plot(midtm_en, final_en, 'b+', label='English')
    plt.xlim(0, 125)
    plt.ylim(0, 100)
    plt.xlabel("Midterm scores")
    plt.ylabel("Final scores")
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.savefig('class_score_scatter.png')
    plt.show()

    # # Plot total scores as a histogram
    bins = numpy.linspace(0, 100, 18)

    plt.hist(total_kr, bins=bins, label='Korean', color='r')
    plt.hist(total_en, bins=bins, label='English', color='b', alpha=0.3)
    plt.xlim(0, 100)
    plt.xlabel("Total scores")
    plt.ylabel("The number of students")
    plt.legend(loc='upper left')
    plt.savefig('class_score_hist.png')
    plt.show()
