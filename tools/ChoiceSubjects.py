from tools.RandomTools import RandomTools


SUBJECTS = ['English', 'Computer Science', 'Chemistry', 'Commerce',
                'Economics', 'Social Studies', 'Maths', 'Physics', 'Arts',
                'History', 'Civics']


class ChoiceSubjects:

    def get_subject(self, list_):
        return RandomTools.RandomValue.get_random_value_from_text_list(list_)

    @staticmethod
    def random_quantity_subjects():
        return RandomTools.RandomValue.get_random_value(
            initial_value=1, end_value=6)

    def list_of_selected_subjects(self, quantity=random_quantity_subjects()):
        subjects = SUBJECTS
        list_of_selected_values = []
        quantity_subjects = quantity
        while len(list_of_selected_values) < quantity_subjects:
            subject = self.get_subject(subjects)
            list_of_selected_values.append(subject)
            subjects.remove(subject)
        return list_of_selected_values
