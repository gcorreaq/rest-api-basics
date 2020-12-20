from datetime import datetime, timedelta
from unittest import TestCase

from models.events import Event


class TestEvent(TestCase):

    def test_contains_all_expected_fields(self):
        start_datetime = datetime.utcnow() + timedelta(days=1)
        end_datetime = start_datetime + timedelta(days=5)

        event = Event(
            name='My test event',
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            location='Here',
            description='My test description',
        )

        self.assertEqual(event.name, 'My test event')
        self.assertEqual(event.start_datetime, start_datetime)
        self.assertEqual(event.end_datetime, end_datetime)
        self.assertEqual(event.location, 'Here')
        self.assertEqual(event.description, 'My test description')
        self.assertTrue(event.unique_id)

    def test_raises_exception_if_start_datetime_is_in_the_past(self):
        pass

    def test_raises_exception_if_end_datetime_is_before_start_datetime(self):
        pass
