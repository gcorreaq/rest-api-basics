from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class Event:
    name: str
    start_datetime: datetime
    end_datetime: datetime
    location: str
    description: str
    unique_id: str = uuid4().hex

    def __post_init__(self):
        if self.start_datetime < datetime.utcnow():
            raise ValueError('Start datetime is in the past')

        if self.end_datetime < self.start_datetime:
            raise ValueError('End datetime should happen after start datetime')
