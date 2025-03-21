from __future__ import unicode_literals
import csv

try:
    with open('example.xlsx') as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            for r in row:
                print(r.encode().decode().replace(';', ' '))
except Exception as e:
    print(e)
