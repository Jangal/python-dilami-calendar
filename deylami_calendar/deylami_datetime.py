from datetime import datetime, time
from khayyam import JalaliDatetime
from .pure_algorithms import (
    deylami_to_jalali,
    jalali_to_deylami,
    get_days_in_deylami_month
)
from .constants import (
    DEYLAMI_WEEKDAY_NAMES,
    DEYLAMI_MONTH_NAMES,
    MAXYEAR,
    MINYEAR
)


class DeylamiDatetime:
    """
    Represent date in Deylami

    The first parameter can be :py:class:`datetime.date`
                            or :py:class:`khayyam.JalaliDate`.

    :param year: deylami year
    :param month: deylami month 0-12
    :param day: deylami day 0-30
    :param hour: 0-23
    :param minute: 0-59
    :param second: 0-59
    :param microsecond: 0-999999
    :param tzinfo: Timezone info

    :type year: :py:class:`int` | :py:class:`datetime.date`
                                | :py:class: `DeylamiDatetime`
    :type month: int
    :type day: int
    :type hour: int
    :type minute: int
    :type second: int
    :type microsecond: int
    :type tzinfo: :py:class:`datetime.tzinfo` | callable
    :return: A :py:class:`deylami_calendar.DeylamiDatetime` instance.
    :rtype: :py:class:`deylami.DeylamiDatetime`

    """

    def __init__(self, year=None, month=None, day=None, hour=None,
                 minute=None, second=None, microsecond=None, tzinfo=None):

        if callable(tzinfo):
            tzinfo = tzinfo()

        if isinstance(year, datetime):
            jd = JalaliDatetime(year, tzinfo=tzinfo)
            year, month, day = jalali_to_deylami(jd.year, jd.month, jd.day)
            hour, minute, second, microsecond = jd.hour, jd.minute, jd.second, \
                jd.microsecond
        elif isinstance(year, DeylamiDatetime):
            dd = year
            year, month, day, hour, minute, second, microsecond = \
                dd.year, dd.month, dd.day, dd.hour, dd.minute, dd.second, \
                dd.microsecond

        jalali_date_time = JalaliDatetime.now(tzinfo)
        dy, dm, dd = jalali_to_deylami(
            jalali_date_time.year, jalali_date_time.month, jalali_date_time.day)

        self.year = year if year else dy
        self.month = month if month is not None else dm
        self.day = day if day is not None else dd
        self.year, self.month, self.day = self._validate(
            self.year, self.month, self.day)

        self._hour = hour if hour else jalali_date_time.hour
        self._minute = minute if minute else jalali_date_time.minute
        self._second = second if second else jalali_date_time.second
        self._microsecond = microsecond if microsecond else \
            jalali_date_time.microsecond
        self._time = time(self._hour, self._minute, self._second,
                          self._microsecond, tzinfo)

    # Properties #
    ##############

    @property
    def hour(self):
        """
        :getter: Returns the hour
        :type: int
        """
        return self._time.hour

    @property
    def minute(self):
        """
        :getter: Returns the minute
        :type: int
        """
        return self._time.minute

    @property
    def second(self):
        """
        :getter: Returns the second
        :type: int
        """
        return self._time.second

    @property
    def microsecond(self):
        """
        :getter: Returns the microsecond
        :type: int
        """
        return self._time.microsecond

    @property
    def tzinfo(self):
        """
        :getter: Returns the timezone info
        :type: :py:class:`datetime.tzinfo`
        """
        return self._time.tzinfo

    @classmethod
    def now(cls, tz=None):
        jalali_date = JalaliDatetime.now(tz)
        dy, dm, dd = jalali_to_deylami(
            jalali_date.year, jalali_date.month, jalali_date.day)

        return cls(dy, dm, dd, tzinfo=tz)

    def _to_jalali(self):
        jy, jm, jd = deylami_to_jalali(self.year, self.month, self.day)
        jalali_datetime = JalaliDatetime(
            jy, jm, jd, self.hour, self.minute, self.second, self.microsecond,
            tzinfo=self._time.tzinfo)

        return jalali_datetime

    def to_datetime(self):
        """
        Converts the current instance to the python builtins
        :py:class:`datetime.datetime` instance.

        :return: the new :py:class:`datetime.datetime` instance representing
                 the current date and time in gregorian calendar.
        :rtype: :py:class:`datetime.datetime`
        """
        return self._to_jalali().todatetime()

    def to_date(self):
        """
        Calculates the corresponding day in the gregorian calendar.

        :return: Corresponding date in gregorian calendar.
        :rtype: :py:class:`datetime.date`
        """
        return self._to_jalali().todate()

    def weekday(self):
        """
        :rtype: int
        :return: The day of the week as an integer,
                 where Saturday is 0 and Friday is 6.
        """
        return self._to_jalali().weekday()

    def weekdayname(self):
        """
        :return: The corresponding deylami weekday name: [شمبه - جۊمه]
        :rtype: unicode
        """
        return DEYLAMI_WEEKDAY_NAMES[self.weekday()]

    def monthname(self):
        """
        :rtype: unicode
        :return: The corresponding deylami month name: [پنجیک - اسفندار ما]
        """
        return DEYLAMI_MONTH_NAMES[self.month]

    @staticmethod
    def _validate(year, month, day):
        year = year if isinstance(year, int) else int(year)
        month = month if isinstance(month, int) else int(month)
        day = day if isinstance(day, int) else int(day)

        if year < MINYEAR or year > MAXYEAR:
            raise ValueError('Year must be between %s and %s, but it is: %s' %
                             (MINYEAR, MAXYEAR, year))
        if month < 0 or month > 12:
            raise ValueError(
                'Month must be between 0 and 12, but it is: %s' % month)

        _days_in_month = get_days_in_deylami_month(year, month)
        if day < _days_in_month[0] or day > _days_in_month[1]:
            raise ValueError('Day must be between 0 and %s, but it is: %s'
                             % (_days_in_month, day))
        return year, month, day

    def __repr__(self):
        return 'deylami_calendar.DeylamiDatetime(%s, %s, %s, %s)' % \
               (self.year, self.month, self.day, self.weekdayname())