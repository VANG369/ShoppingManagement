
import csv
import os

def read_data(file_path):
    data = []

    if not os.path.exists(file_path):
        return data

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        # encoding = 'utf-8' to handle special characters supported like khmer, emoji, etc run on web and desktop application
        reader = csv.reader(file)

        # Skip header
        next(reader, None) #none use to show error if file is empty

        for row in reader:
            if row:
                data.append(row)

    return data

def write_data(file_path, header, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(header)
        # Write rows
        writer.writerows(data)


def append_data(file_path, header, row):
    file_exists = os.path.exists(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header if file doesn't exist or empty
        if not file_exists or os.path.getsize(file_path) == 0:
            writer.writerow(header)
        # Write row
        writer.writerow(row)