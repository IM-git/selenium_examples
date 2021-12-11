from tools.RandomTools import RandomTools

ID_GENDER_MALE = '//input[@id="gender-radio-1"]'
ID_GENDER_FEMALE = '//input[@id="gender-radio-2"]'
ID_GENDER_OTHER = '//input[@id="gender-radio-3"]'

class ChoiceGender:

    @staticmethod
    def get_random_gender():
        __initial_value = 0
        __end_value = 2
        value = RandomTools.RandomValue.get_random_value(__initial_value, __end_value)
        if value == 0:
            return ID_GENDER_MALE
        elif value == 1:
            return ID_GENDER_FEMALE
        elif value == 2:
            return ID_GENDER_OTHER
        else:
            raise Exception(f'Is something wrong!! Value can be 0-2, now the value is: {value}')
