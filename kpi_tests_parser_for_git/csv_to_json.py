import os


def csv_to_json(dir_path):
    """
    Renames csv files to json. Initially results are generated as json files and re-formatted to csv. This
    function reverse this.
    :param dir_path: path where csv files from carlo kpi run located
    :return: None
    """
    for dirpath, _, filenames in os.walk(dir_path):
        for file_name in filenames:
            root, ext = os.path.splitext(file_name)
            if ext == '.csv':
                os.rename(os.path.join(dirpath, file_name), os.path.join(dirpath, root) + '.json')
            elif ext == '.json':
                print(file_name, 'OK')
            else:
                print(file_name, 'Cannot recognize extension')
