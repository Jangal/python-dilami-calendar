import pytest

from freezegun import freeze_time
from datetime import datetime
from khayyam import JalaliDatetime, TehranTimezone

from dilami_calendar import DilamiDatetime, dilami_to_jalali


def test_dilami_date():
    gdate = datetime(2018, 2, 1)
    ddate = DilamiDatetime(gdate, tzinfo=TehranTimezone)

    assert ddate.year == 1591
    assert ddate.month == 6
    assert ddate.day == 28

    ddate = DilamiDatetime(1591, 6, 28, tzinfo=TehranTimezone)
    assert ddate

    ddate = DilamiDatetime(1592, 5, 1, tzinfo=TehranTimezone)
    dilami_date = DilamiDatetime(ddate)
    assert dilami_date

    # Check Dilami date return today
    ddate = DilamiDatetime().now()
    jy, jm, jd = dilami_to_jalali(ddate.year, ddate.month, ddate.day)

    today = JalaliDatetime.now(TehranTimezone())
    assert today.year == jy
    assert today.month == jm
    assert today.day == jd

    with freeze_time(datetime.now()):
        dilami_now = DilamiDatetime(datetime.now()).to_datetime()
        assert dilami_now.time() == datetime.now().time()

    now = datetime.now()
    dilami_date = DilamiDatetime(now)
    assert dilami_date.to_date() == now.date()


def test_limits():
    # Test MinYear and MaxYear
    with pytest.raises(ValueError):
        DilamiDatetime(194, 1, 1)
    with pytest.raises(ValueError):
        DilamiDatetime(3373, 1, 1)

    # Test months
    with pytest.raises(ValueError):
        DilamiDatetime(1592, -1, 3)

    with pytest.raises(ValueError):
        DilamiDatetime(1592, 13, 1)

    # Test days
    with pytest.raises(ValueError):
        DilamiDatetime(1592, 1, 32)
    with pytest.raises(ValueError):
        DilamiDatetime(1592, 1, -1)

    # Test days of leap year
    with pytest.raises(ValueError):
        DilamiDatetime(1595, 0, 0)

    with pytest.raises(ValueError):
        DilamiDatetime(1593, 0, 6)
