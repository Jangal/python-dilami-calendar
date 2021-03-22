from datetime import date, timedelta
from khayyam import JalaliDate

from dilami_calendar import (
    MINYEAR,
    MAXYEAR,
    dilami_to_jalali,
    jalali_to_dilami,
)


def test_jalali_to_dilami():
    dy, dm, dd = jalali_to_dilami(1398, 5, 1)
    assert dy == 1592
    assert dm == 12
    assert dd == 15

    for jy in range(1390, 1395):
        for jm in range(1, 13):
            for jd in range(1, 31):
                dy, dm, dd = jalali_to_dilami(jy, jm, jd)
                assert 1584 <= dy <= 1589
                assert 0 <= dm <= 12
                assert 0 <= dd <= 30

    # incremental check
    ldd = None
    ljd = None
    gdt = date(622, 4, 3)
    delta = timedelta(days=1)
    while ldd != (MAXYEAR, 1, 1):
        gdt = gdt + delta
        jdt = JalaliDate(gdt)
        ndd = jalali_to_dilami(jdt.year, jdt.month, jdt.day)
        njd = dilami_to_jalali(*ndd)
        assert ndd != ldd
        assert njd != ljd
        ldd = ndd
        ljd = njd
    assert ldd == (MAXYEAR, 1, 1)


def test_leap_year():
    assert jalali_to_dilami(1399, 12, 29) == (1594, 8, 15)
    assert jalali_to_dilami(1399, 12, 30) == (1594, 8, 16)
    assert jalali_to_dilami(1400, 1, 1) == (1594, 8, 17)


def test_dilami_to_jalali():
    jy, jm, jd = dilami_to_jalali(1592, 12, 15)
    assert jy == 1398
    assert jm == 5
    assert jd == 1

    for dy in range(1584, 1589):
        for dm in range(1, 12):
            for dd in range(1, 30):
                jy, jm, jd = dilami_to_jalali(dy, dm, dd)
                assert 1389 <= jy <= 1395
                assert 0 <= jm <= 12
                assert 0 <= jd <= 31

    # Test panjik days for leap years
    jy, jm, jd = dilami_to_jalali(1587, 0, 2)
    assert jy == 1393
    assert jm == 1
    assert jd == 17

    jy, jm, jd = dilami_to_jalali(1587, 0, 0)
    assert jy == 1393
    assert jm == 1
    assert jd == 15
