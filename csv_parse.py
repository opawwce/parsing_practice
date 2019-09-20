import math
import csv
<------------------------------------------------ ->
# html_output = ''
# names = []

# with open('names.csv', 'r') as data_file:
#     csv_data = csv.DictReader(data_file)
#     # Delete first string in output
#     next(csv_data)
#     for line in csv_data:
#         names.append(f"{line[0]} {line[1]}")

# html_output += f'<p>There are currently {len(names)} public contributors: <p>'

# html_output += '\n<ul>'

# for name in names:
#     html_output += f'\n\t<li>{name}<li>'

# html_output += '\n</ul>'

# print(html_output)
<--------------------------------------------------------- ->
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open('new_names.csv', 'w') as new_file:
#         fieldnames = ['first_name', 'last_name']
#         csv_writer = csv.DictWriter(
#             new_file, fieldnames=fieldnames, delimiter='\t')

#         csv_writer.writeheader()

#         for line in csv_reader:
#             del line['email']
#             csv_writer.writerow(line)
