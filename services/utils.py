import csv


def read_file(source):
    results = []
    with open(source) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            results.append(row)
    return results
