from dilami_calendar.constants import DILAMI_LEAP_YEARS


def is_dilami_leap_year(y):
    return y in DILAMI_LEAP_YEARS


def jalali_to_dilami(jy, jm, jd):
    if jm < 5 or (jm == 5 and jd < 17):
        dy = jy + 194

    else:
        dy = jy + 195

    if jm == 5:
        dm = 1 if jd > 16 else 12
        dd = jd - 16 if jd > 16 else jd + 14

    elif jm == 6:
        dm = 2 if jd > 15 else 1
        dd = jd - 15 if jd > 15 else jd + 15

    elif jm == 7:
        dm = 3 if jd > 14 else 2
        dd = jd - 14 if jd > 14 else jd + 16

    elif jm == 8:
        dm = 4 if jd > 14 else 3
        dd = jd - 14 if jd > 14 else jd + 16

    elif jm == 9:
        dm = 5 if jd > 14 else 4
        dd = jd - 14 if jd > 14 else jd + 16

    elif jm == 10:
        dm = 6 if jd > 14 else 5
        dd = jd - 14 if jd > 14 else jd + 16

    elif jm == 11:
        dm = 7 if jd > 14 else 6
        dd = jd - 14 if jd > 14 else jd + 16

    elif jm == 12:
        dm = 8 if jd > 14 else 7
        dd = jd - 14 if jd > 14 else jd + 16

    elif jm == 1:
        is_leap = is_dilami_leap_year(dy)

        if is_leap and jd == 15:
            dm, dd = 0, 0

        elif is_leap and jd < 15:
            dm, dd = 8, jd + 16

        elif not is_leap and jd < 16:
            dm, dd = 8, jd + 15

        elif 15 < jd < 21:
            dm, dd = 0, jd - 15

        elif jd > 20:
            dm, dd = 9, jd - 20

    elif jm == 2:
        dm = 10 if jd > 19 else 9
        dd = jd - 19 if jd > 19 else jd + 11

    elif jm == 3:
        dm = 11 if jd > 18 else 10
        dd = jd - 18 if jd > 18 else jd + 12

    elif jm == 4:
        dm = 12 if jd > 17 else 11
        dd = jd - 17 if jd > 17 else jd + 13

    return dy, dm, dd


def dilami_to_jalali(dy, dm, dd):
    if dm != 0 and (dm < 8 or (dm == 8 and dd <= 15)):
        jy = dy - 195
    else:
        jy = dy - 194

    if dm == 0 and dd == 0:
        return jy, 1, 15

    if dm == 0:
        return jy, 1, dd + 15

    if dm == 1:
        jm = 5 if dd <= 15 else 6
        jd = dd + 16 if dd <= 15 else dd - 15

    elif dm == 2:
        jm = 6 if dd <= 16 else 7
        jd = dd + 15 if dd <= 16 else dd - 16

    elif dm == 3:
        jm = 7 if dd <= 16 else 8
        jd = dd + 14 if dd <= 16 else dd - 16

    elif dm == 4:
        jm = 8 if dd <= 16 else 9
        jd = dd + 14 if dd <= 16 else dd - 16

    elif dm == 5:
        jm = 9 if dd <= 16 else 10
        jd = dd + 14 if dd <= 16 else dd - 16

    elif dm == 6:
        jm = 10 if dd <= 16 else 11
        jd = dd + 14 if dd <= 16 else dd - 16

    elif dm == 7:
        jm = 11 if dd <= 16 else 12
        jd = dd + 14 if dd <= 16 else dd - 16

    elif dm == 8:
        k = 1 if is_dilami_leap_year(dy) else 0
        jm = 12 if dd <= (15 + k) else 1
        jd = dd + 14 if dd <= (15 + k) else dd - 15 - k
        if k == 1 and dd == 16:
            jy = jy - 1

    elif dm == 9:
        jm = 1 if dd <= 11 else 2
        jd = dd + 20 if dd <= 11 else dd - 11

    elif dm == 10:
        jm = 2 if dd <= 12 else 3
        jd = dd + 19 if dd <= 12 else dd - 12

    elif dm == 11:
        jm = 3 if dd <= 13 else 4
        jd = dd + 18 if dd <= 13 else dd - 13

    elif dm == 12:
        jm = 4 if dd <= 14 else 5
        jd = dd + 17 if dd <= 14 else dd - 14

    return jy, jm, jd


def get_days_in_dilami_month(year, month):
    if 1 <= month <= 12:
        return 1, 30

    if month != 0:
        raise ValueError("Month must be between 0 and 12 but 0 is after 8")

    # Panjik (پنجیک)
    if is_dilami_leap_year(year):
        return 0, 5

    return 1, 5
