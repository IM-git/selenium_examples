import datetime

DATE_OF_BIRTH = '14 Dec 2011'
TODAY_DATE = datetime.datetime.today().strftime("%d %b %Y")
MONTH_LIST = {"Jan": 1,
              "Feb": 2,
              "Mar": 3,
              "Apr": 4,
              "May": 5,
              "Jun": 6,
              "Jul": 7,
              "Aug": 8,
              "Sep": 9,
              "Oct": 10,
              "Nov": 11,
              "Dec": 12,
              }


class CheckingDateBirth:

    def get_today_date(self):
        return TODAY_DATE

    def compare_date(self, date, minimum_age=6):
        __date_entered = date.split(' ')
        __today_date = TODAY_DATE.split(' ')
        __comparison_of_date = int(__today_date[2]) - int(__date_entered[2])
        __message = f'Is something wrong!! The age must be more than ' \
                    f'{__comparison_of_date} years old, now the age is: {date}'
        if __comparison_of_date >= minimum_age:
            if MONTH_LIST[__today_date[1]] >= MONTH_LIST[__date_entered[1]]:
                if int(__today_date[0]) >= int(__date_entered[0]):
                    pass
                else:
                    raise Exception(__message)
            else:
                raise Exception(__message)
        else:
            raise Exception(__message)
