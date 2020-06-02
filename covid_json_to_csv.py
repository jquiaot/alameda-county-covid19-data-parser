import argparse
from datetime import date
import json
import sys

def convert_covid_json_to_csv(root, date_field, value_fields):
    print('date_field {}'.format(date_field))
    for data_point in root['features']:
        # { "Fremont": num_cumulative_cases, "DtCreate": timestamp_epoch }
        timestamp_epoch = data_point['attributes'][date_field]
        timestamp_date = date.fromtimestamp(timestamp_epoch // 1000)
        values = []
        for value_field in value_fields:
            values.append(data_point['attributes'][value_field])
        print('{},{}'.format(timestamp_date, ','.join(map(str, values))))

if __name__ == '__main__':
    # read from file or stdin
    parser = argparse.ArgumentParser(
        description = 'Process JSON from Alameda County Cumulative Cases By Place And Zip.'
        )
    parser.add_argument('-f', '--file', help = 'JSON file to read')
    parser.add_argument('-d', '--date_field', help = 'Date field name to use (required)', required = True)
    parser.add_argument('-v', '--value_fields', help = 'CSV of value field names to use (required)', required = True)

    args = parser.parse_args()
    inf = None
    if args.file:
        if args.file != '-':
            inf = open(args.file)
        else:
            inf = sys.stdin
    else:
        inf = sys.stdin

    root = json.load(inf)
    date_field = args.date_field
    value_fields = None
    if args.value_fields:
        value_fields = args.value_fields.split(',')

    convert_covid_json_to_csv(root, date_field, value_fields)

# END
