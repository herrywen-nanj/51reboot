import csv

def read_csv(filename):
    with open(filename, 'r') as fo:
        csv_reader = csv.reader(fo)
        headers = next(csv_reader)

        return headers


# read_csv('../user_list.csv')