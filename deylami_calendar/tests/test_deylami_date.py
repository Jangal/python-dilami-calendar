import pytest

from freezegun import freeze_time
from datetime import datetime
from khayyam import JalaliDatetime, TehranTimezone

from deylami_calendar import DeylamiDatetime
from deylami_calendar.pure_algorithms import deylami_to_jalali


def test_deylami_date():
    gdate = datetime(2018, 2, 1)
    ddate = DeylamiDatetime(gdate, tzinfo=TehranTimezone)

    assert ddate.year == 1591
    assert ddate.month == 6
    assert ddate.day == 28

    ddate = DeylamiDatetime(1591, 6, 28, tzinfo=TehranTimezone)
    assert ddate

    ddate = DeylamiDatetime(1592, 5, 1, tzinfo=TehranTimezone)
    deylami_date = DeylamiDatetime(ddate)
    assert deylami_date

    # Check deylami date return today
    ddate = DeylamiDatetime().now()
    jy, jm, jd = deylami_to_jalali(ddate.year, ddate.month, ddate.day)

    today = JalaliDatetime.now(TehranTimezone())
    assert today.year == jy
    assert today.month == jm
    assert today.day == jd

    with freeze_time(datetime.now()):
        deylami_now = DeylamiDatetime(datetime.now()).to_datetime()
        assert deylami_now.time() == datetime.now().time()

    now = datetime.now()
    daylami_date = DeylamiDatetime(now)
    assert daylami_date.to_date() == now.date()


def test_limits():
    # Test MinYear and MaxYear
    with pytest.raises(ValueError):
        DeylamiDatetime(194, 1, 1)
    with pytest.raises(ValueError):
        DeylamiDatetime(3373, 1, 1)

    # Test months
    with pytest.raises(ValueError):
        DeylamiDatetime(1592, -1, 3)

    with pytest.raises(ValueError):
        DeylamiDatetime(1592, 13, 1)

    # Test days
    with pytest.raises(ValueError):
        DeylamiDatetime(1592, 1, 32)
    with pytest.raises(ValueError):
        DeylamiDatetime(1592, 1, -1)

    # Test days of leap year
    with pytest.raises(ValueError):
        DeylamiDatetime(1595, 0, 0)

    with pytest.raises(ValueError):
        DeylamiDatetime(1593, 0, 6)
