from patterns.Singleton import Singleton
from tools import read_file
import json

WAY = 'tools/data_names.json'


class DataNames(metaclass=Singleton):

    @staticmethod
    def _get_list_names(path):
        return read_file.read_file(path)
