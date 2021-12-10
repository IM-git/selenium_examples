from tools.RandomTools import RandomTools
from tools.DataNames import DataNames
import random


# WAY = 'data_names.json'


class RandomName:

    @staticmethod
    def choice_gender():
        genders = ["girls", "boys"]
        num = random.randint(0, 1)
        return genders[num]

    @staticmethod
    def random_name(way):
        get_data_names = DataNames._get_list_names(way)
        get_gender = RandomName.choice_gender()
        name = RandomTools.RandomValue.get_random_value_from_text_list(get_data_names[get_gender])
        # print(name)
        return name

# RandomName.random_name()
