from datetime import date, timedelta
import requests


class Student:
    """ A student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = self._start_date + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def apply_extension(self, ext):
        self.end_date = self.end_date + timedelta(days=ext)

    def course_schedule(self):
        response = requests.get(
            f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request"

    def start_date(self):
        return self._start_date

    def set_end_date(self):
        if self._start_date.year % 4 == 0 and self._start_date.year % 100 != 0:
            if self._start_date.year % 400 == 0:
                self.end_date = self._start_date + timedelta(days=366)
        else:
            self.end_date = self._start_date + timedelta(days=365)
        return self.end_date
