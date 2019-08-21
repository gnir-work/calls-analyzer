from es_utils import reset_index, index_data
from call_metadata import CallMetadata
from io_utils import get_data
from dataclasses import asdict

if __name__ == "__main__":
    data = map(asdict, map(CallMetadata.from_dict, get_data()))
    reset_index()
    list(map(index_data, data))