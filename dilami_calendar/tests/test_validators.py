import pytest
from dilami_calendar import (
    MINYEAR,
    MAXYEAR,
    InvalidDilamiYearError,
    InvalidDilamiMonthError,
    InvalidDilamiDayError,
    InvalidPanjikError,
    InvalidVishakError,
    validate_dilami_date,
    validate_dilami_year,
    validate_dilami_month,
    validate_dilami_day,
)


def test_validators():
    # date
    with pytest.raises(InvalidVishakError):
        assert validate_dilami_date(1593, 0, 0)

    with pytest.raises(InvalidPanjikError):
        assert validate_dilami_date(1593, 0, 6)

    with pytest.raises(InvalidPanjikError):
        assert validate_dilami_date(1594, 0, 6)

    # year
    validate_dilami_year(MINYEAR + 1)
    validate_dilami_year(MAXYEAR - 1)
    with pytest.raises(InvalidDilamiYearError):
        assert validate_dilami_year(MINYEAR - 1)

    with pytest.raises(InvalidDilamiYearError):
        assert validate_dilami_year(MAXYEAR + 1)

    # month
    validate_dilami_month(0)
    validate_dilami_month(12)
    with pytest.raises(InvalidDilamiMonthError):
        assert validate_dilami_month(-1)

    with pytest.raises(InvalidDilamiMonthError):
        assert validate_dilami_month(13)

    # day
    validate_dilami_day(0)
    validate_dilami_day(30)
    with pytest.raises(InvalidDilamiDayError):
        assert validate_dilami_day(-1)

    with pytest.raises(InvalidDilamiDayError):
        assert validate_dilami_day(31)
