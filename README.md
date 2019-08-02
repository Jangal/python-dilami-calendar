# python-deylami-calendar

[![Build Status](https://travis-ci.org/Jangal/python-deylami-calendar.svg?branch=master)](https://travis-ci.org/Jangal/python-deylami-calendar)

## Install

```bash
pip install deylami-calendar
```


## Usage


Get current datetime in deylami

```python
from deylami_calendar import DeylamiDatetime

print(DeylamiDatetime.now())

```


Convert Gregorian datetime to Deylami

```python
from datetime import datetime
from deylami_calendar import DeylamiDatetime

gregorian_datetime = datetime(2018, 2, 1)
deylami_datetime = DeylamiDatetime(gregorian_datetime)

```

Convert Deylami to Gregorian datetime


```python
from deylami_calendar import DeylamiDatetime

deylami_datetime = DeylamiDatetime(1591, 6, 28)
gregorian_datetime = deylami_datetime.to_datetime()
```


Read attributes 

```python
from deylami_calendar import DeylamiDatetime

d = DeylamiDatetime().now()
print(
    d.year,
    d.month,
    d.day,
    d.hour,
    d.minute,
    d.second
)
```

Set time-zone

```python
import pytz
from deylami_calendar import DeylamiDatetime

d = DeylamiDatetime(tzinfo=pytz.timezone('Asia/Tehran')).now()
print(d)

```


## Credits
 
- https://github.com/pylover/khayyam
- [wiki:گاه‌شماری_گیلکی](https://fa.wikipedia.org/wiki/%DA%AF%D8%A7%D9%87%E2%80%8C%D8%B4%D9%85%D8%A7%D8%B1%DB%8C_%DA%AF%DB%8C%D9%84%DA%A9%DB%8C)
