#!/usr/bin/env python3

import csv
import sqlite3
import sys
import argparse
import os.path

__version__ = '1.0.0'

class SqliteToCsv:
    def __init__(self, sqlite_input_file, csv_output_file):
        self.sqlite_input = sqlite_input_file
        self.csv_output = csv_output_file

    def dump_csv(self):
        if os.path.isfile(self.csv_output):
            print('csv file {} already exists'.format(self.csv_output))
            exit(1)

        db = sqlite3.connect(self.sqlite_input)
        db.text_factory = str
        cur = db.cursor()
        data = cur.execute("SELECT type, front, back, known FROM cards ORDER BY id ASC")
        self.__write_csv(data)

    def __write_csv(self, items):
        with open(self.csv_output, mode='w') as f:
            c = csv.writer(f, delimiter='\t', lineterminator='\n')
            c.writerow(['type', 'front', 'back', 'known'])
            for item in items:
                c.writerow(item)


if __name__ == '__main__':
    """
    Sample usage: ./sqlite_to_csv.py cards.db cards.csv
    """
    parser = argparse.ArgumentParser(description='Convert flash cards sqlite db file to csv file.')
    parser.add_argument('sqlite_file', help="input sqlite db file")
    parser.add_argument('csv_file', help="output csv file")
    args = parser.parse_args()

    sqlite_file = args.sqlite_file
    csv_file = args.csv_file

    converter = SqliteToCsv(sqlite_file, csv_file)
    converter.dump_csv()
