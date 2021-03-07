from datetime import datetime


class Date:
    def __init__(self, date: datetime = None, date_dict: dict = None):
        self.__date_time = date if date is not None else datetime(
            year=date_dict['year'],
            month=date_dict['month'],
            day=date_dict['day'],
            hour=date_dict['hour'],
            minute=date_dict['minute'],
            second=date_dict['second']
        )

    @property
    def year(self):
        return self.__date_time.year

    @property
    def month(self):
        return self.__date_time.month

    @property
    def day(self):
        return self.__date_time.day

    @property
    def hour(self):
        return self.__date_time.hour

    @property
    def minute(self):
        return self.__date_time.minute

    @property
    def second(self):
        return self.__date_time.second

    def broken(self) -> dict:
        return {
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'hour': self.hour,
            'minute': self.minute,
            'second': self.second
        }

    @staticmethod
    def __format(data):
        return '0' + data if len(data) < 2 else data

    def __add__(self, other: "Date"):
        return self.__date_time + other.__date_time

    def __sub__(self, other):
        return self.__date_time - other.__date_time

    def __gt__(self, other):
        return self.__date_time > other.__date_time

    def __lt__(self, other):
        return self.__date_time < other.__date_time

    def __str__(self):
        return f'{Date.__format(str(self.day))}/{Date.__format(str(self.month))}/{Date.__format(str(self.year))} | ' \
               f'{Date.__format(str(self.hour))}:{Date.__format(str(self.minute))}:{Date.__format(str(self.second))}'

    def __repr__(self):
        return self.__str__()
