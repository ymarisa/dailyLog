import json
import sys
import copy
from datetime import date, timedelta


def make_log_record(example_record, pk, record_date, score, habit):
    this_record = copy.deepcopy(example_record)
    this_record["pk"] = pk
    this_record["fields"]["date"] = record_date.isoformat()
    this_record["fields"]["score"] = score
    this_record["fields"]["habit"] = habit

    # print(example_record)
    # print(this_record)

    return this_record


def nice_print(data):
    print(json.dumps(data, indent=4))


def write_json(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def main(argv=None):
    if argv is None or len(argv) < 3 or len(argv) > 3:
        print("usage: create_data.py [file.json]")
        sys.exit()

    # Setup
    gen_data = [
        [0, 1, 0, 1, 1, -1, 1, 0, 1, 1, -1, 1, -1, 1, 0, -1, 1, 1, -1, 0, 1, 0, -1, 1, 1, 1, -1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, -1, 1, 1, 0, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 0, 0, 0, 0, 1, -1],
        [6, 8, 6, 8, 8, 7, 7, 5, 5, 8, 8, 8, 6, 5, 4, 8, 8, 7, 6, 7, 7, 7, 8, 6, 4, 8, 7, 8],
    ]

    pk_record = 1
    start_date = date.fromisoformat("2019-08-12")
    # print(start_date + timedelta(days=1))

    # Read in data
    in_file = argv[1]
    out_file = argv[2]

    print("opening " + in_file + " writing to " + out_file)
    with open(in_file) as json_file:
        data = json.load(json_file)

    print("example: record")
    nice_print(data[0])
    example_record = data[0]

    out_data = []
    for habit in range(0, len(gen_data)):
        print(habit)
        record_date = start_date
        for record in gen_data[habit]:
            new_record = make_log_record(example_record, pk_record, record_date, record, habit + 1)
            out_data.append(new_record)
            record_date += timedelta(1)
            pk_record += 1

    write_json(out_data, out_file)


if __name__ == "__main__":
    main(sys.argv)

