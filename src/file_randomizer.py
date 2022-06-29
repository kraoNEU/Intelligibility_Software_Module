import random


def file_randomizer_file_path(number_of_directories):
    """
    :returns: Returns Random integer between 1 and the Number of Directories
    """
    return random.randint(1, number_of_directories)
