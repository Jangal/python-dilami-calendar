from dilami_calendar.constants import MINYEAR, MAXYEAR
from dilami_calendar.exceptions import (
    InvalidDilamiYearError,
    InvalidPanjikError,
    InvalidVishakError,
    InvalidDilamiMonthError,
    InvalidDilamiDayError,
)
from dilami_calendar.algorithms import is_dilami_leap_year


def validate_dilami_year(dy):
    if dy < MINYEAR or dy > MAXYEAR:
        raise InvalidDilamiYearError(
            "Year (%s) not in range (%s,%s)" % (dy, MINYEAR, MAXYEAR)
        )


def validate_dilami_month(dm):
    if dm < 0 or dm > 12:
        raise InvalidDilamiMonthError(
            "Month (%s) not in range (%s,%s)" % (dm, 0, 12)
        )


def validate_dilami_day(dm):
    if dm < 0 or dm > 30:
        raise InvalidDilamiDayError(
            "Day (%s) not in range (%s,%s)" % (dm, 0, 30)
        )


def validate_dilami_date(dy, dm, dd):
    validate_dilami_year(dy)
    validate_dilami_month(dm)
    validate_dilami_day(dd)
    if not is_dilami_leap_year(dy) and dm == 0 and dd == 0:
        raise InvalidVishakError("%s is not leap year (Vishak)")

    if dm == 0 and dd > 5:
        raise InvalidPanjikError("Invalid Panjik day")
