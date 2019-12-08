import os
import pandas as pd

from config import registered_tests


def generate_results_list(dir_path):
    """
    Calculates kpi results for every test
    :param dir_path: where files for calculation located
    :return: list of dictionaries, with calculated results for every specified file
    """
    files_list = []
    results_to_csv_list = []

    for dirpath, _, filenames in os.walk(dir_path):
        for file_name in filenames:
            files_list.append(file_name)

    for file_name in files_list:
        # Split TC_name.json to 2 values: name(root), ext
        root, ext = os.path.splitext(file_name)
        if root not in registered_tests.keys():
            print('TC does not have assigned function for calculation', file_name)
        else:
            # some test cases have 2 or more calculation methods, which returned as list type
            if type(registered_tests.get(root)) == list:
                for func in registered_tests.get(root):
                    calculation_res_dict = func(os.path.join(dir_path, file_name))
                    calculation_res_dict['test_name'] = root
                    results_to_csv_list.append(calculation_res_dict)
            else:
                calculation_res_dict = registered_tests.get(root, "No function called")(os.path.join(dir_path,
                                                                                                     file_name))
                calculation_res_dict['test_name'] = root
                results_to_csv_list.append(calculation_res_dict)

    return results_to_csv_list


def generate_results_csv(results_list, filename, sheetname):
    """
    Generates CSV file with final results
    :param results_list: calculation results which should be passed to resulting csv file
    :param filename: filename where to store calculation results
    :return: None
    """
    df = pd.DataFrame.from_dict(data=results_list)
    df = df[['test_name', 'cpu_max', 'cpu_avg', 'cpu_min', 'cpu_std', 'memory_max', 'memory_avg', 'memory_min',
             'memory_std', 'time', 'calc_function']]
    try:
        if os.stat(filename).st_size > 0:
            with pd.ExcelWriter(filename, engine="openpyxl", mode='a') as writer:
                df.to_excel(writer, sheet_name=sheetname, float_format="%.2f")
        else:
            df.to_excel(filename, engine="openpyxl", sheet_name=sheetname, float_format="%.2f")
    except OSError:
        print(f'Cannot create results file, no {filename} exists')


