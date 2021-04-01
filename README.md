# python-dilami-calendar

[![Build Status](https://travis-ci.org/Jangal/python-dilami-calendar.svg?branch=master)](https://travis-ci.org/Jangal/python-dilami-calendar)
![PyPI](https://img.shields.io/pypi/v/dilami-calendar)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dilami-calendar)
![GitHub license](https://img.shields.io/github/license/Jangal/python-dilami-calendar)

## Install

```bash
pip install dilami-calendar
```


## Usage


Get current datetime in Dilami

```python
from dilami_calendar import DilamiDatetime

print(DilamiDatetime.now())

```


Convert Gregorian datetime to Dilami

```python
from datetime import datetime
from dilami_calendar import DilamiDatetime

gregorian_datetime = datetime(2018, 2, 1)
dilami_datetime = DilamiDatetime(gregorian_datetime)

```

Convert Dilami to Gregorian datetime


```python
from dilami_calendar import DilamiDatetime

dilami_datetime = DilamiDatetime(1591, 6, 28)
gregorian_datetime = dilami_datetime.to_datetime()
```


Read attributes 

```python
from dilami_calendar import DilamiDatetime

d = DilamiDatetime().now()
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
from dilami_calendar import DilamiDatetime

d = DilamiDatetime(tzinfo=pytz.timezone('Asia/Tehran')).now()
print(d)

```

## Maybe You Like
[PHP Dilami Calendar](https://github.com/Jangal/php-dilami-calendar)
<br/>
[C++ Dilami Calendar](https://github.com/LordArma/Dilami-Calendar-C-)
<br/>
[Arduino Dilami Calendar](https://github.com/LordArma/Dilami-Calendar-Arduino)
<br/>
[.Net Dilami Calendar](https://github.com/Jangal/Dilami-Calendar-.Net)
<br/>
[تقویم دیلمی](http://giltime.ir)


## Credits
 
- https://github.com/pylover/khayyam
- [wiki:گاه‌شماری_گیلکی](https://fa.wikipedia.org/wiki/%DA%AF%D8%A7%D9%87%E2%80%8C%D8%B4%D9%85%D8%A7%D8%B1%DB%8C_%DA%AF%DB%8C%D9%84%DA%A9%DB%8C)
