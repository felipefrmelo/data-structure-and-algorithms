## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os


def find_files(suffix="", path="."):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

    Returns:
            a list of paths
    """
    list_of_paths = []
    def _find_files(suffix, path):

        if (os.path.isfile(path)):
            if path.endswith(suffix):
                list_of_paths.append(path)
        else:
            files = os.listdir(path)
            for file in files:
                _find_files(suffix, os.path.join(path, file))

    _find_files(suffix, path)

    if(len(list_of_paths) == 0):
        raise FileNotFoundError()

    return list_of_paths
