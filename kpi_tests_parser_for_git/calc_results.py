import json
import sys
import statistics

TIME_TO_SEC_FACTOR = 1000000000
TO_MB_FACTOR = 1024 * 1024
NUM_OF_CORES = 4


def analise_start_test(json_file):
    """
        Function calculates maximum for memory, cpu and time.
        Data is taken from json file given in parameters.
        Returns dictionary with values, calculation function name
        Uses 'label', 'Test run'
    """
    parsed_json_res_list = []
    time_value_list = []
    cpu_value_list = []
    memory_value_list = []
    res_summary = {}

    for line in open(json_file, 'r', encoding='utf-8'):
        parsed_json_res_list.append(json.loads(line))

    for dict in parsed_json_res_list:
        if ('label', 'Test run') in dict.items():
            time_value_list.append(dict.get('total-elapsed-time[ns]'))
            cpu_value_list.append(dict.get('cpu-load[%]'))
            memory_value_list.append(dict.get('memory-resident-set-size[b]'))

    time_res_list, cpu_res_list, memory_res_list = [], [], []

    for el in time_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TIME_TO_SEC_FACTOR))
            time_res_list.append(g)

    for el in cpu_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / NUM_OF_CORES))
            cpu_res_list.append(g)

    for el in memory_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TO_MB_FACTOR))
            memory_res_list.append(g)

    res_summary['time'] = max(time_res_list)

    res_summary['cpu_max'] = max(cpu_res_list)
    res_summary['cpu_avg'] = float("{0:.2f}".format(sum(cpu_res_list) / len(cpu_res_list)))
    res_summary['cpu_min'] = min(cpu_res_list)

    res_summary['memory_max'] = max(memory_res_list)
    res_summary['memory_avg'] = float("{0:.2f}".format(sum(memory_res_list) / len(memory_res_list)))
    res_summary['memory_min'] = min(memory_res_list)

    res_summary['calc_function'] = str(sys._getframe().f_code.co_name)

    return res_summary


def analise_routing_test(json_file):
    """Function calculates maximum for memory, cpu and time.
        Data is taken from json file given in parametres.
        Returns dictionary with values + calculation function name
        Uses 'label', 'Calculate route'"""
    parsed_json_res_list = []
    time_value_list = []
    cpu_value_list = []
    memory_value_list = []
    res_summary = {}
    for line in open(json_file, 'r', encoding='utf-8'):
        parsed_json_res_list.append(json.loads(line))

    for dict in parsed_json_res_list:
        if ('label', 'Calculate route') in dict.items():
            time_value_list.append(dict.get('total-elapsed-time[ns]'))
            cpu_value_list.append(dict.get('cpu-load[%]'))
            memory_value_list.append(dict.get('memory-resident-set-size[b]'))

    time_res_list, cpu_res_list, memory_res_list = [], [], []

    for el in time_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TIME_TO_SEC_FACTOR))
            time_res_list.append(g)

    for el in cpu_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / NUM_OF_CORES))
            cpu_res_list.append(g)

    for el in memory_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TO_MB_FACTOR))
            memory_res_list.append(g)

    res_summary['time'] = max(time_res_list)

    res_summary['cpu_max'] = max(cpu_res_list)
    res_summary['cpu_avg'] = float("{0:.2f}".format(sum(cpu_res_list) / len(cpu_res_list)))
    res_summary['cpu_min'] = min(cpu_res_list)

    res_summary['memory_max'] = max(memory_res_list)
    res_summary['memory_avg'] = float("{0:.2f}".format(sum(memory_res_list) / len(memory_res_list)))
    res_summary['memory_min'] = min(memory_res_list)
    res_summary['calc_function'] = str(sys._getframe().f_code.co_name)

    return res_summary


def analise_guidance_test(json_file):
    """Function calculates maximum for memory, cpu and time.
            Data is taken from json file given in parametres.
            Returns dictionary with values + calculation function name
            Uses 'label', 'Start guidance'"""
    parsed_json_res_list = []
    time_value_list = []
    cpu_value_list = []
    memory_value_list = []
    res_summary = {}
    for line in open(json_file, 'r', encoding='utf-8'):
        parsed_json_res_list.append(json.loads(line))

    for dict in parsed_json_res_list:
        if ('label', 'Start guidance') in dict.items():
            time_value_list.append(dict.get('total-elapsed-time[ns]'))
            cpu_value_list.append(dict.get('cpu-load[%]'))
            memory_value_list.append(dict.get('memory-resident-set-size[b]'))

    time_res_list, cpu_res_list, memory_res_list = [], [], []

    for el in time_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TIME_TO_SEC_FACTOR))
            time_res_list.append(g)

    for el in cpu_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / NUM_OF_CORES))
            cpu_res_list.append(g)

    for el in memory_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TO_MB_FACTOR))
            memory_res_list.append(g)

    res_summary['time'] = max(time_res_list)

    res_summary['cpu_max'] = max(cpu_res_list)
    res_summary['cpu_avg'] = float("{0:.2f}".format(sum(cpu_res_list) / len(cpu_res_list)))
    res_summary['cpu_min'] = min(cpu_res_list)

    res_summary['memory_max'] = max(memory_res_list)
    res_summary['memory_avg'] = float("{0:.2f}".format(sum(memory_res_list) / len(memory_res_list)))
    res_summary['memory_min'] = min(memory_res_list)

    res_summary['calc_function'] = str(sys._getframe().f_code.co_name)

    return res_summary


def analise_hybrid_test(json_file):
    """Function calculates maximum for memory, cpu and time.
                Data is taken from json file given in parametres.
                Returns dictionary with values + calculation function name
                Uses 'label', 'Hybrid search'"""
    parsed_json_res_list = []
    time_value_list = []
    cpu_value_list = []
    memory_value_list = []
    res_summary = {}
    for line in open(json_file, 'r', encoding='utf-8'):
        parsed_json_res_list.append(json.loads(line))

    for dict in parsed_json_res_list:
        if ('label', 'Hybrid search') in dict.items():
            time_value_list.append(dict.get('total-elapsed-time[ns]'))
            cpu_value_list.append(dict.get('cpu-load[%]'))
            memory_value_list.append(dict.get('memory-resident-set-size[b]'))

    time_res_list, cpu_res_list, memory_res_list = [], [], []

    for el in time_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TIME_TO_SEC_FACTOR))
            time_res_list.append(g)

    for el in cpu_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / NUM_OF_CORES))
            cpu_res_list.append(g)

    for el in memory_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TO_MB_FACTOR))
            memory_res_list.append(g)

    res_summary['time'] = max(time_res_list)

    res_summary['cpu_max'] = max(cpu_res_list)
    res_summary['cpu_avg'] = float("{0:.2f}".format(sum(cpu_res_list) / len(cpu_res_list)))
    res_summary['cpu_min'] = min(cpu_res_list)

    res_summary['memory_max'] = max(memory_res_list)
    res_summary['memory_avg'] = float("{0:.2f}".format(sum(memory_res_list) / len(memory_res_list)))
    res_summary['memory_min'] = min(memory_res_list)
    res_summary['calc_function'] = str(sys._getframe().f_code.co_name)

    return res_summary


def analise_radius_test(json_file):
    """Function calculates maximum for memory, cpu and time.
                    Data is taken from json file given in parametres.
                    Returns dictionary with values + calculation function name
                    Uses 'label', 'Radius search'"""
    parsed_json_res_list = []
    time_value_list = []
    cpu_value_list = []
    memory_value_list = []
    res_summary = {}
    for line in open(json_file, 'r', encoding='utf-8'):
        parsed_json_res_list.append(json.loads(line))

    for dict in parsed_json_res_list:
        if ('label', 'Radius search') in dict.items():
            time_value_list.append(dict.get('total-elapsed-time[ns]'))
            cpu_value_list.append(dict.get('cpu-load[%]'))
            memory_value_list.append(dict.get('memory-resident-set-size[b]'))

    time_res_list, cpu_res_list, memory_res_list = [], [], []

    for el in time_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TIME_TO_SEC_FACTOR))
            time_res_list.append(g)

    for el in cpu_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / NUM_OF_CORES))
            cpu_res_list.append(g)

    for el in memory_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TO_MB_FACTOR))
            memory_res_list.append(g)

    res_summary['time'] = max(time_res_list)

    res_summary['cpu_max'] = max(cpu_res_list)
    res_summary['cpu_avg'] = float("{0:.2f}".format(sum(cpu_res_list) / len(cpu_res_list)))
    res_summary['cpu_min'] = min(cpu_res_list)

    res_summary['memory_max'] = max(memory_res_list)
    res_summary['memory_avg'] = float("{0:.2f}".format(sum(memory_res_list) / len(memory_res_list)))
    res_summary['memory_min'] = min(memory_res_list)

    res_summary['calc_function'] = str(sys._getframe().f_code.co_name)

    return res_summary


def analise_endurance_test(json_file):
    """Function calculates max, min, average for memory, cpu.
        Data is taken from json file given in parameteres.
        Returns dictionary with values + calculation function name"""
    parsed_json_res_list = []
    time_value_list = []
    cpu_value_list = []
    memory_value_list = []
    res_summary = {}
    for line in open(json_file, 'r', encoding='utf-8'):
        parsed_json_res_list.append(json.loads(line))

    for dict in parsed_json_res_list:
        time_value_list.append(dict.get('total-elapsed-time[ns]'))
        cpu_value_list.append(dict.get('cpu-load[%]'))
        memory_value_list.append(dict.get('memory-resident-set-size[b]'))

    time_res_list, cpu_res_list, memory_res_list = [], [], []

    for el in cpu_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / NUM_OF_CORES))
            cpu_res_list.append(g)

    for el in memory_value_list:
        if el is not None:
            g = float("{0:.2f}".format(el / TO_MB_FACTOR))
            memory_res_list.append(g)

    res_summary['cpu_max'] = max(cpu_res_list)
    res_summary['cpu_min'] = min(cpu_res_list)
    res_summary['cpu_avg'] = float("{0:.2f}".format(sum(cpu_res_list) / len(cpu_res_list)))
    res_summary['cpu_std'] = float("{0:.2f}".format(statistics.stdev(cpu_res_list)))

    res_summary['memory_max'] = max(memory_res_list)
    res_summary['memory_min'] = min(memory_res_list)
    res_summary['memory_avg'] = float("{0:.2f}".format(sum(memory_res_list) / len(memory_res_list)))
    res_summary['memory_std'] = float("{0:.2f}".format(statistics.stdev(memory_res_list)))

    res_summary['calc_function'] = str(sys._getframe().f_code.co_name)

    return res_summary
