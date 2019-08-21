from csv import DictReader
from collections import OrderedDict
from call_metadata import CallMetadata, _parse_number

def read_file(path_to_file : str) -> OrderedDict:
    with open(path_to_file) as calls:
        return list(DictReader(calls))


if __name__ == "__main__":
    data = read_file('./calls.csv')
    calls_metadata = map(CallMetadata.from_dict, data)
    for d in calls_metadata:
            print(d)