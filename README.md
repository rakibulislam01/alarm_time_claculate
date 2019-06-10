
# AlarmTime

AlarmTime is a Python library for dealing with alarm.
Detect alarm time from natural sentence.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install AlarmTime
```

## Usage

```python
# Sample Code
from AlarmTime import DetectDate


t = DetectDate(1570000023345) 
print(t.now) #2019-10-02 13:07:39.393012
t = DetectDate('2019/5/2/14/5') 
print(t.now)  #2019-05-02 14:05:39.393185
t = DetectDate() 
print(t.now) #2019-04-21 12:26:12.542967

t = DetectDate()

target_time = t.date_time_detect('detect the time and date on December 16 8 p.m')
print(target_time) 

target_time = t.date_time_detect('detect the time and date on December 16 ')
print(target_time) 

target_time = t.date_time_detect('after 700 days')
print(target_time)

target_time = t.date_time_detect('after 6 month 700 days 8 hour 5 minute')
print(target_time)


# now we can get the value of target year, day, month, hour, minute, second
print(target_time.day) 
```

# Output
### 2019-04-21 12:26:12.542967
### 2019-12-16 20:00:00.542967
### 2019-12-16 00:00:00.542967
### 2021-03-21 12:26:12.542967
### 2021-09-20 20:31:12.542967
### 2021-03-21 12:26:12.542967
### 21

#

```python
from AlarmTime import DetectDate

t = DetectDate()
minute_diff = t.minute_diff_from_now('after 1 days')
print(minute_diff)
```
#1440.0

```python
from AlarmTime import DetectDate

t = DetectDate()
hour_diff = t.hour_diff_from_now('after 1 days')
print(hour_diff)
```
#24.0

```python
from AlarmTime import DetectDate

t = DetectDate()
day_diff = t.day_diff_from_now('after 1 days')
print(day_diff)
```
#1.0

```python
from AlarmTime import DetectDate

t = DetectDate()
sec_diff = t.second_diff_from_now('after 1 days')
print(sec_diff)
```
#86400.0
