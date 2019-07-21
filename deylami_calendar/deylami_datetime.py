# -*- coding: utf-8 -*-
import datetime
from khayyam import JalaliDatetime, TehranTimezone, JalaliDate
from .pure_algorithms import deylami_to_jalali, jalali_to_deylami


class DeylamiDate:
    """
    Represent date in Deylami

    The first parameter can be :py:class:`datetime.date`
                            or :py:class:`khayyam.JalaliDate`.

    :param year: delylami year
    :param month: deylami month
    :param day: daylami day

    :type year: :py:class:`int` | :py:class:`datetime.date` |
                :py:class:`khayyam.JalaliDate` | :py:class: `DeylamiDate`
    :type month: int
    :type day: int

    :return: A :py:class:`deylami_calendar.DeylamiDate` instance.
    :rtype: :py:class:`khayyam.JalaliDate`

    """

    def __init__(self, year=None, month=None, day=None):
        if isinstance(year, JalaliDate):
            jd = year
            year, month, day = jalali_to_deylami(jd.year, jd.month, jd.day)

        elif isinstance(year, datetime.date):
            jd = JalaliDate(year)
            year, month, day = jalali_to_deylami(jd.year, jd.month, jd.day)

        elif isinstance(year, DeylamiDate):
            dd = year
            year = dd.year
            month = dd.month
            day = dd.day

        jalali_date = JalaliDatetime.now(TehranTimezone())
        dy, dm, dd = jalali_to_deylami(
            jalali_date.year, jalali_date.month, jalali_date.day)

        self.year = year if year else dy
        self.month = month if month else dm
        self.day = day if day else dd

    @staticmethod
    def now():
        jalali_date = JalaliDatetime.now(TehranTimezone())
        deylami_date = jalali_to_deylami(
            jalali_date.year, jalali_date.month, jalali_date.day)

        return deylami_date

    @staticmethod
    def month_name(month_number):
        months = [
            "پنجیک", "نؤرۊز ما", "کۊرچ ٚ ما", "أرئه ما",
            "تیر ما", "مۊردال ما", "شریرما",
            "أمیر ما", "آول ما", "سیا ما",
            "دیا ما", "ورفن ٚ ما", "اسفندار ما"
        ]

        return months[month_number]

    @staticmethod
    def day_of_week(day_number):
        if 7 < day_number or day_number < 1:
            return False

        week = ["یکشمبه", "دۊشمبه", "سۊشمبه",
                "چارشمبه", "پئنشمبه", "جۊمه", "شمبه"]
        return week[day_number]
