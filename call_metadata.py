from __future__ import annotations

from dataclasses import dataclass
from collections import OrderedDict
import re
from consts import FieldNames, NUMBER_REGEX, NUMBER_GROUP_NAME
from pytimeparse.timeparse import timeparse

@dataclass
class CallMetadata:
    name: str
    number: str
    duration: int
    call_type: str

    @classmethod
    def from_dict(cls, raw_data: OrderedDict) -> CallMetadata:
        """
        Create an instance of the class from a given dict.
        """
        return cls(name=raw_data[FieldNames.NAME],
                   number=_parse_number(raw_data[FieldNames.NUMBER]),
                   duration=timeparse(raw_data[FieldNames.DURATION]),
                   call_type=raw_data[FieldNames.TYPE])


def _parse_number(number):
    return NUMBER_REGEX.match(number).groupdict()[NUMBER_GROUP_NAME]
