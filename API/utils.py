#!/usr/bin python
# -*- coding: utf-8 -*-
# Python: 3.6
# @Time    : 2019/9/21 11:14
# @Author  : bnightning(QQ:1079056140)
# @Email   : bnightning@163.com
# @File    : utils.py
# @Software: PyCharm
# Errors should never pass silently.
# Unless explicitly silenced.

import datetime


def parse_ymd(time):
    # 2019-09-20 00:00:00
    # 2019-09-21 23:59:59
    ymd, hms = time.split(' ')
    year, month, day = ymd.split('-')
    hour, minute, second = hms.split(':')
    data = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
    # tz_utc_8 = timezone(timedelta(hours=8))
    # return data.replace(tzinfo=tz_utc_8)
    return data


def date_ymd(time):
    # 2019-09-20
    # 2019-09-21
    year, month, day = time.split('-')
    data = datetime.datetime(int(year), int(month), int(day))
    return data


def today_date():
    return datetime.date.today()


def before_n_day(n):
    today = datetime.date.today()
    return today - datetime.timedelta(days=n)


def after_n_day(n):
    today = datetime.date.today()
    return today + datetime.timedelta(days=n)


def from_before_n_day(day, n):
    return day - datetime.timedelta(days=n)


def from_after_n_day(day, n):
    return day + datetime.timedelta(days=n)


def before_n_day_time_start(n):
    date = datetime.date.today() - datetime.timedelta(days=n)
    time = str(date) + ' 00:00:00'
    ymd, hms = time.split(' ')
    year, month, day = ymd.split('-')
    hour, minute, second = hms.split(':')
    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))


def before_n_day_time_end(n):
    date = datetime.date.today() - datetime.timedelta(days=n)
    time = str(date) + ' 23:59:59'
    ymd, hms = time.split(' ')
    year, month, day = ymd.split('-')
    hour, minute, second = hms.split(':')
    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))


def getEveryDay(begin_date, end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def monthRange(beginDate, endDate):
    monthSet = set()
    for date in dateRange(beginDate, endDate):
        monthSet.add(date[0:7])
    monthList = []
    for month in monthSet:
        monthList.append(month)
    return sorted(monthList)


def getNowDay():
    DayNow = datetime.datetime.today().strftime('%Y-%m-%d')
    return DayNow


def getYesterDay():
    YesterDay = (datetime.datetime.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    return YesterDay


def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def dateHourRange(beginDateHour, endDateHour):
    dhours = []
    dhour = datetime.datetime.strptime(beginDateHour, "%Y-%m-%d %H")
    date = beginDateHour[:]
    while date <= endDateHour:
        dhours.append(date)
        dhour = dhour + datetime.timedelta(hours=1)
        date = dhour.strftime("%Y-%m-%d %H")
    return dhours


def check_none(value):
    if not value or value == 'undefined' or value == '':
        return None
    else:
        return value
