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
        return datetime.datetime.today().strftime("%d %b %Y")

    def compare_date(self, date=DATE_OF_BIRTH, minimum_age=6):
        __date_entered = date.split(' ')
        __today_date = TODAY_DATE.split(' ')
        __comparison_of_date = int(__today_date[2]) - int(__date_entered[2])
        __message = f'Is something wrong!! The age must be more than ' \
                    f'{minimum_age} years old, now the age is: {__comparison_of_date}'

        if __comparison_of_date >= minimum_age:
            pass
        elif MONTH_LIST[__today_date[1]] >= MONTH_LIST[__date_entered[1]]:
            pass
        elif int(__today_date[0]) >= int(__date_entered[0]):
            pass
        else:
            raise Exception(__message)
