import unittest
from datetime import date, timedelta, datetime
from student import Student
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request")

    def test_student_start_date(self):
        day = self.student.start_date()
        self.assertEqual(self.student._start_date, day)

    def test_student_end_date_leap_year(self):
        self.student._start_date = date(2020, 1, 1)
        print(self.student._start_date)
        correct_end_date = date(2021, 1, 1)
        calc_end = self.student.set_end_date()
        self.assertEqual(calc_end, correct_end_date)

    def test_student_end_date_regular_year(self):
        self.start_date = datetime(2022, 1, 1)
        calc_end = self.student.set_end_date()
        self.assertEqual(calc_end, date(2023, 1, 1))


if __name__ == "__main__":
    unittest.main()
