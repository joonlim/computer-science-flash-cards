#!/usr/bin/env python3

import csv
import sqlite3
import sys
import argparse
import os.path

__version__ = '1.0.0'

class CsvToSqlite:
    def __init__(self, csv_input_file, sqlite_output_file):
        self.csv_input = csv_input_file
        self.sqlite_output = sqlite_output_file

    def dump_sqlite(self,):
        if os.path.isfile(self.sqlite_output):
            print('sqlite db file {} already exists'.format(self.sqlite_output))
            exit(1)

        with open(self.csv_input, 'r') as file:
            c = csv.reader(file, delimiter='\t', lineterminator='\n')
            rows = list(c)
            self.__write_sqlite(rows[1:])

    def __write_sqlite(self, items):
        db = sqlite3.connect(self.sqlite_output)
        cur = db.cursor()
        with open('data/schema.sql', mode='r') as f:
            cur.executescript(f.read())

        for item in items:
            if len(item) is 4 and item[0].strip()[0] != '#':
                cur.execute('INSERT INTO cards (type, front, back, known) VALUES (?, ?, ?, ?)',
                            item)

        db.commit()
        db.close()

if __name__ == '__main__':
    """
    Sample usage: ./csv_to_sqlite.py cards.csv cards.db
    """
    parser = argparse.ArgumentParser(description='Convert flash cards csv file to sqlite db file.')
    parser.add_argument('csv_file', help="input csv file")
    parser.add_argument('sqlite_file', help="output sqlite db file")
    args = parser.parse_args()

    csv_file = args.csv_file
    sqlite_file = args.sqlite_file

    converter = CsvToSqlite(csv_file, sqlite_file)
    converter.dump_sqlite()
