import unittest
from deylami_calendar.pure_algorithms import (
    deylami_to_jalali,
    jalali_to_deylami
)


class TestAlgorithms(unittest.TestCase):

    def test_jalali_to_deylami(self):
        dy, dm, dd = jalali_to_deylami(1398, 5, 1)
        self.assertEqual(dy, 1592)
        self.assertEqual(dm, 12)
        self.assertEqual(dd, 15)

        jy, jm, jd = deylami_to_jalali(1592, 12, 15)
        self.assertEqual(jy, 1398)
        self.assertEqual(jm, 5)
        self.assertEqual(jd, 1)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

