import re
import os
import pytz

class FieldNames:
    """
    All of the field names in the csv.
    """
    NAME = 'Name'
    NUMBER = 'Number'
    DATE = 'Date'
    TIME = 'Time'
    DURATION = 'Duration'
    TYPE = 'Type'

NUMBER_GROUP_NAME = 'number'
NUMBER_REGEX = re.compile(fr"^\'(?P<{NUMBER_GROUP_NAME}>\+?[\d-]*)\'$")
LOCAL_TZ_INFO = pytz.timezone('Asia/Jerusalem')
DATE_FORMAT = f"M/D/YY HH:mm"
DATA_FILE = os.path.join('.', 'calls.csv')

INDEX = 'calls_metada'
HOST = 'localhost:9200'
MAPPINGS = {
  "properties": {
    "name": {
      "type": "keyword"
    },
    "number": {
      "type": "text"
    },
    "duration": {
      "type": "integer"
    },
    "call_type": {
      "type": "keyword"
    },
    "date": {
      "type": "date"
    },
    "week_day": {
      "type": "keyword"
    }
  }
}