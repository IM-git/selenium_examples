from tools.RandomTools import RandomTools


ID_HOBBY_SPORTS = '//input[@id="hobbies-checkbox-1"]'
ID_HOBBY_READING = '//input[@id="hobbies-checkbox-2"]'
ID_HOBBY_MUSIC = '//input[@id="hobbies-checkbox-3"]'


class ChoiceHobbies:

    def get_hobbies(self):
        __list_hobbies = []
        __quantity_click = self.get_value_clicks()
        for value in range(__quantity_click):
            __list_hobbies.append(self.choice_hobby())
        return __list_hobbies

    def get_value_clicks(self):
        __initial_value = 0
        __end_value = 6
        value = RandomTools.RandomValue.get_random_value(
            __initial_value, __end_value)
        return value

    def choice_hobby(self):
        __initial_value = 0
        __end_value = 2
        __list_id_hobbies = [ID_HOBBY_SPORTS, ID_HOBBY_READING, ID_HOBBY_MUSIC]
        __id_hobby = RandomTools.RandomValue.get_random_value(
            __initial_value, __end_value)
        return __list_id_hobbies[(__id_hobby-1)]
