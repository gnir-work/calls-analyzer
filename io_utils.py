from csv import DictReader
from collections import OrderedDict
from consts import DATA_FILE

def get_data(path_to_file : str = DATA_FILE) -> OrderedDict:
    with open(path_to_file) as calls:
        return list(DictReader(calls))