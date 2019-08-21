import re
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