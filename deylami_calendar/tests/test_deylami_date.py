import unittest
from khayyam import JalaliDate, JalaliDatetime, TehranTimezone

from deylami_calendar import DeylamiDate
from deylami_calendar.pure_algorithms import (
    deylami_to_jalali
)


class TestDeylamiDate(unittest.TestCase):

    def test_deylami_date(self):
        jdate = JalaliDate(1398, 5, 1)
        ddate = DeylamiDate(jdate)
        self.assertEqual(ddate.year, 1592)
        self.assertEqual(ddate.month, 12)
        self.assertEqual(ddate.day, 15)

        ddate = DeylamiDate(1592, 12, 15)
        assert ddate

        # Check deylami date return today
        ddate = DeylamiDate()
        jy, jm, jd = deylami_to_jalali(ddate.year, ddate.month, ddate.day)

        today = JalaliDatetime.now(TehranTimezone())
        self.assertEqual(today.year, jy)
        self.assertEqual(today.month, jm)
        self.assertEqual(today.day, jd)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

