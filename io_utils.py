from csv import DictReader
from collections import OrderedDict
from consts import DATA_FILE
from typing import List

def get_data(path_to_file: str = DATA_FILE) -> List[OrderedDict]:
    """
    Convert the csv file to a list of dicts with the data.
    """
    with open(path_to_file) as calls:
        return list(DictReader(calls))
