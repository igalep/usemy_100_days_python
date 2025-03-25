import os


def get_file_path(file_name):
    '''
    read from file
    :param file_name: file to read from
    :return: the file content
    '''
    file_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(file_path, '..', 'resources', file_name)