import argparse

from csv_to_json import csv_to_json
from results_to_csv import generate_results_list, generate_results_csv
from download_from_ci import download_from_ci

parser = argparse.ArgumentParser()
parser.add_argument("-dir_path", help='Path do directory where csv files located',
                    default='./csv_from_carlo_kpi_run', required=False)
parser.add_argument('-build', help='Build number where to download results',
                    required=False)
parser.add_argument('-release', help='Enter release version', required=True)
args = parser.parse_args()

if args.build:
    download_from_ci(build_number=args.build, dir_path=args.dir_path)
    csv_to_json(dir_path=args.dir_path)
    results_list = generate_results_list(dir_path=args.dir_path)
    generate_results_csv(results_list=results_list, filename='kpi_results_tablet.xlsx', sheetname=args.release)
else:
    csv_to_json(dir_path=args.dir_path)
    results_list = generate_results_list(dir_path=args.dir_path)
    generate_results_csv(results_list=results_list, filename='kpi_results_device.xlsx', sheetname=args.release)
