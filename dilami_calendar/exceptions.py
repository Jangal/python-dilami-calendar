class DilamiValueError(ValueError):
    pass


class InvalidDilamiYearError(DilamiValueError):
    pass


class InvalidDilamiMonthError(DilamiValueError):
    pass


class InvalidDilamiDayError(DilamiValueError):
    pass


class InvalidPanjikError(DilamiValueError):
    pass


class InvalidVishakError(DilamiValueError):
    pass
