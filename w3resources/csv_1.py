# Write a Python program to read each row from a given csv file and print a list of strings.
import csv 
# with open('departments.csv', newline='') as csvfile:
#     data = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in data:
#         print(', '.join(row))

# with open('departments.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line)

# create new csv and write in
# with open('departments.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')

#         for line in csv_reader:
#             csv_writer.writerow(line)

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)