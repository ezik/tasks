import requests
import os
import shutil
from config import registered_tests

project_url = "some_project_url_here"


def download_from_ci(build_number, dir_path):
    """
    Downloads results from Jenkins. Require access to network.
    :param build_number: job number where CSV files located
    :param dir_path: directory, where files should be saved
    :return: None
    """
    # create a list of tests to download
    registered_tests_to_download = [*registered_tests.keys()]

    print('Downloading files from config.py list')
    print("build to download: ", build_number)

    # create folder
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        shutil.rmtree(dir_path)
        os.makedirs(dir_path)

    for test_to_download in registered_tests_to_download:
        url = project_url + str(build_number) + "path" + test_to_download + ".csv"
        r = requests.get(url, allow_redirects=True)

        if r.status_code == 200:
            file_name_to_save_test_data = test_to_download + ".csv"
            open(dir_path + "/" + file_name_to_save_test_data, 'wb').write(r.content)
            print("Downloading file ", test_to_download, " from build ", build_number, "complete!")
        else:
            print("During downloading ", test_to_download, " from build ", build_number, "http response: ",
                  r.status_code)

        r.close()
