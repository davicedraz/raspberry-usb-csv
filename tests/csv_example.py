import csv
from datetime import datetime

dir = #your dir

read_path = dir + "Google Stock Market Data - google_stock_data.csv.csv"
write_path = dir + "output.csv"


def format_data(data):
    formated_data = []
    for row in data:
        date = datetime.strptime(row[0], "%m/%d/%Y")
        open_p = float(row[1])
        high_p = float(row[2])
        low_p = float(row[3])
        close_p = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])

        formated_data.append(
            [date, open_p, high_p, low_p, close_p, volume, adj_close])

    return formated_data


def read_file(file):
    reader = csv.reader(file)
    header = next(reader)

    data = format_data(reader)
    return data


def write_file(file, data):
    writer = csv.writer(file)
    writer.writerow(["Date", "Return"])

    for i in range(len(data) - 1):
        today = data[i][0]
        writer.writerow([today, 'name'])


if __name__ == "__main__":
    input_file = open(read_path, newline='')
    output_file = open(write_path, 'w', newline='')

    data = read_file(input_file)
    write_file(output_file, data)
