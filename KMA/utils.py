from csv import DictReader
from os import path


def get_current_dir():
    return path.dirname(path.realpath(__file__))


def get_join(file):
    dir = get_current_dir()
    return path.join(dir, file)
