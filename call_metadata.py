from __future__ import annotations

import arrow
import datetime
from dataclasses import dataclass
from collections import OrderedDict
import re
from consts import FieldNames, NUMBER_REGEX, NUMBER_GROUP_NAME, LOCAL_TZ_INFO
from pytimeparse.timeparse import timeparse

@dataclass
class CallMetadata:
    name: str
    number: str
    duration: int
    call_type: str
    date: datetime.datetime

    @classmethod
    def from_dict(cls, raw_data: OrderedDict) -> CallMetadata:
        """
        Create an instance of the class from a given dict.
        """
        return cls(name=raw_data[FieldNames.NAME],
                   number=_parse_number(raw_data[FieldNames.NUMBER]),
                   duration=timeparse(raw_data[FieldNames.DURATION]),
                   call_type=raw_data[FieldNames.TYPE],
                   date=_parse_date(raw_data[FieldNames.DATE], raw_data[FieldNames.TIME])
                   )


def _parse_number(number):
    return NUMBER_REGEX.match(number.replace(' ','')).groupdict()[NUMBER_GROUP_NAME]

def _parse_date(date, time):
    date_time = f"{date} {time}"
    return arrow.get(date_time, f"M/D/YY HH:mm").replace(tzinfo=LOCAL_TZ_INFO).datetime
