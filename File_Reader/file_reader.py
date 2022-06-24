import os


def get_number_of_directories_in_a_path(path):
    """
    :param path: Get a String Input of the Directory
    :return: The total number of files specific to the directory
    """
    count_number_of_sub_directories = 0

    # Iterates through the list of directories
    for f in os.listdir(path):

        # Ignores hidden files that start with "." eg: .DS_Store
        if not f.startswith("."):
            count_number_of_sub_directories += 1

    # Returns the Number of Directories
    return count_number_of_sub_directories
