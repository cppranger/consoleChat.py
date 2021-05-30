import datetime


def getDate() -> tuple:
    date = str(datetime.date.today())
    year, month, day = date.split('-')
    year, month, day = int(year), int(month), int(day)
    return day, month, year
