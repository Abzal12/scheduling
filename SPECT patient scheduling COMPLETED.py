from tabulate import tabulate
from datetime import timedelta
import pandas
import fontstyle

# Dictionary(MENU) with study characteristics
MENU = {
    "скелет_1ч": {
        "stress/syringe": 0,
        "waiting_time": 3600,
        "duration": 4800,
        "drug": "Резоскан",
    },
    "скелет_3ч": {
        "stress/syringe": 0,
        "waiting_time": 10800,
        "duration": 4800,
        "drug": "Фосфотех/Технефор/Пирфотех",
    },
    "сер_1": {
        "stress/syringe": 900,
        "waiting_time": 1800,
        "duration": 3000,
        "drug": "Технетрил",
    },
    "сер_1_доп": {
        "stress/syringe": 0,
        "waiting_time": 2100,
        "duration": 3000,
        "drug": "Технетрил",
    },
    "сер_2": {
        "stress/syringe": 900,
        "waiting_time": 1800,
        "duration": 3000,
        "drug": "Технетрил",
    },
    "сер_2_доп": {
        "stress/syringe": 0,
        "waiting_time": 2100,
        "duration": 3000,
        "drug": "Технетрил",
    },
    "сер_3": {
        "stress/syringe": 900,
        "waiting_time": 1800,
        "duration": 3000,
        "drug": "Технетрил",
    },
    "сер_3_доп": {
        "stress/syringe": 0,
        "waiting_time": 2100,
        "duration": 3000,
        "drug": "Технетрил",
    },
    "п_1": {
        "stress/syringe": 0,
        "waiting_time": 900,
        "duration": 3600,
        "drug": "Н.перт, Технетрил",
    },
    "п_1_доп": {
        "stress/syringe": 0,
        "waiting_time": 0,
        "duration": 2100,
        "drug": " ",
    },
    "п_2": {
        "stress/syringe": 0,
        "waiting_time": 900,
        "duration": 3600,
        "drug": "Н.перт, Технетрил",
    },
    "п_2_доп": {
        "stress/syringe": 0,
        "waiting_time": 0,
        "duration": 2100,
        "drug": " ",
    },
    "п_3": {
        "stress/syringe": 0,
        "waiting_time": 900,
        "duration": 3600,
        "drug": "Н.перт, Технетрил",
    },
    "п_3_доп": {
        "stress/syringe": 0,
        "waiting_time": 0,
        "duration": 2100,
        "drug": " ",
    },
    "щитавидка": {
        "stress/syringe": 300,
        "waiting_time": 900,
        "duration": 3000,
        "drug": "Н.перт",
    },
    "голова": {
        "stress/syringe": 0,
        "waiting_time": 1200,
        "duration": 3000,
        "drug": "Теоксим",
    },
    "почки": {
        "stress/syringe": 300,
        "waiting_time": 0,
        "duration": 3000,
        "drug": "Пентатех",
    },
    "слу": {
        "stress/syringe": 0,
        "waiting_time": 300,
        "duration": 3600,
        "drug": "Нанотоп",
    },
}

# constants
PERV_OSM = 2100
PRIHOD = 900
list_of_names_for_typer = []

# functions
def get_time_hh_mm_ss(sec):
    td_str = str(timedelta(seconds=sec))
    x = td_str.split(':')
    return f"{x[0]}:{x[1]}:{x[2]}"


def time_to_sec(time):
    sec = sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))
    return sec


def calculate(study):
    begin = injection_in_s + MENU[study]["waiting_time"]
    end = begin + MENU[study]["duration"]
    stressSyringe = injection_in_s - MENU[study]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[study]["drug"]
    list.extend([study, prihod, perv_osm, stressSyringe, injection_in_s, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(study)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_renal_thyroid(next_study_input):
    stressSyringe = table[n - 1][6] + 600
    injection = stressSyringe + MENU[next_study_input]["stress/syringe"]
    begin = injection + MENU[next_study_input]["waiting_time"]
    end = begin + MENU[next_study_input]["duration"]
    perv_osm1 = stressSyringe - PERV_OSM
    prihod = perv_osm1 - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm1, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_parathyroid_1(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_parathyroid_1_dop(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    for r in range(1, len(table)):
        if "п_1" in table[r]:
            if begin - table[r][4] < 9000:
                begin = table[r][4] + 9000
                end = begin + MENU[next_study_input]["duration"]
                injection = begin - MENU[next_study_input]["waiting_time"]
                stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
                perv_osm = stressSyringe - PERV_OSM
                prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_parathyroid_2(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_parathyroid_2_dop(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    for r in range(1, len(table)):
        if "п_2" in table[r]:
            if begin - table[r][4] < 9000:
                begin = table[r][4] + 9000
                end = begin + MENU[next_study_input]["duration"]
                injection = begin - MENU[next_study_input]["waiting_time"]
                stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
                perv_osm = stressSyringe - PERV_OSM
                prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_parathyroid_3(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_parathyroid_3_dop(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    for r in range(1, len(table)):
        if "п_3" in table[r]:
            if begin - table[r][4] < 9000:
                begin = table[r][4] + 9000
                end = begin + MENU[next_study_input]["duration"]
                injection = begin - MENU[next_study_input]["waiting_time"]
                stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
                perv_osm = stressSyringe - PERV_OSM
                prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_perf_1(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_perf_1_dop(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    for r in range(1, len(table)):
        if "сер_1" in table[r]:
            if injection - table[r][4] < 7200:
                injection = table[r][4] + 7200
                begin = injection + MENU[next_study_input]["waiting_time"]
                end = begin + MENU[next_study_input]["duration"]
                stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
                perv_osm = stressSyringe - PERV_OSM
                prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_perf_2(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_perf_2_dop(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    for r in range(1, len(table)):
        if "сер_2" in table[r]:
            if injection - table[r][4] < 7200:
                injection = table[r][4] + 7200
                begin = injection + MENU[next_study_input]["waiting_time"]
                end = begin + MENU[next_study_input]["duration"]
                stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
                perv_osm = stressSyringe - PERV_OSM
                prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_perf_3(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_perf_3_dop(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    for r in range(1, len(table)):
        if "сер_3" in table[r]:
            if injection - table[r][4] < 7200:
                injection = table[r][4] + 7200
                begin = injection + MENU[next_study_input]["waiting_time"]
                end = begin + MENU[next_study_input]["duration"]
                stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
                perv_osm = stressSyringe - PERV_OSM
                prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def calculate_2(next_study_input):
    begin = table[n - 1][6] + 600
    end = begin + MENU[next_study_input]["duration"]
    injection = begin - MENU[next_study_input]["waiting_time"]
    stressSyringe = injection - MENU[next_study_input]["stress/syringe"]
    perv_osm = stressSyringe - PERV_OSM
    prihod = perv_osm - PRIHOD
    drug = MENU[next_study_input]["drug"]
    list.extend([next_study_input, prihod, perv_osm, stressSyringe, injection, begin, end, drug])
    table.append(list)
    list_of_names_for_typer.append(next_study_input)
    print(fontstyle.apply('\n'.join(str(item) for item in list_of_names_for_typer), 'bold/Italic/red'))


def seconds_to_hours_and_mins():
    for n in range(1, len(table)):
        for m in range(1, len(table[n]) - 1):
            table[n][m] = get_time_hh_mm_ss(table[n][m])


def check_for_syringe_equal_to_injection():
    for n in range(1, len(table)):
        if table[n][3] == table[n][4]:
            if "почки" not in table[n]:
                table[n][3] = "-"


def assemble_begin_and_end():
    for t in range(1, len(table)):
        list1 = [f"{table[t][5]}-{table[t][6]}"]
        result = ', '.join(str(item) for item in list1)
        table[t][5] = result


def delete_last_column():
    for n in range(1, len(table)):
        del table[n][6]


def from_parathyroid_dop_to_parathyroid_1():
    for o in range(1, len(table) - 1):
        if "п_1" in table[o][0]:
            for r in range(1, len(table)):
                if "п_1_доп" in table[r][0]:
                    list2 = [f"{table[o][5]},\n{table[r][5]}"]
                    result = ', '.join(str(item) for item in list2)
                    table[o][5] = result

        if "п_1" in table[o]:
            natr_pert = time_to_sec(table[o][4])
            mibi = natr_pert + 1200
            natr_pert = get_time_hh_mm_ss(natr_pert)
            mibi = get_time_hh_mm_ss(mibi)
            sp_list = [f"{natr_pert}н.п.\n{mibi}mibi"]
            result = ', '.join(str(item) for item in sp_list)
            table[o][4] = result


def from_parathyroid_dop_to_parathyroid_2():
    for n in range(1, len(table) - 1):
        if "п_2" in table[n]:
            for r in range(1, len(table)):
                if "п_2_доп" in table[r]:
                    list2 = [f"{table[n][5]},\n{table[r][5]}"]
                    result = ', '.join(str(item) for item in list2)
                    table[n][5] = result

        if "п_2" in table[n]:
            natr_pert = time_to_sec(table[n][4])
            mibi = natr_pert + 1200
            natr_pert = get_time_hh_mm_ss(natr_pert)
            mibi = get_time_hh_mm_ss(mibi)
            sp_list = [f"{natr_pert}н.п.\n{mibi}mibi"]
            result = ', '.join(str(item) for item in sp_list)
            table[n][4] = result


def from_parathyroid_dop_to_parathyroid_3():
    for k in range(1, len(table) - 1):
        if "п_3" in table[k]:
            for r in range(1, len(table)):
                if "п_3_доп" in table[r]:
                    list2 = [f"{table[k][5]},\n{table[r][5]}"]
                    result = ', '.join(str(item) for item in list2)
                    table[k][5] = result

        if "п_3" in table[k]:
            natr_pert = time_to_sec(table[k][4])
            mibi = natr_pert + 1200
            natr_pert = get_time_hh_mm_ss(natr_pert)
            mibi = get_time_hh_mm_ss(mibi)
            sp_list = [f"{natr_pert}н.п.\n{mibi}mibi"]
            result = ', '.join(str(item) for item in sp_list)
            table[k][4] = result


def delete_unneccesary_parathyroid_info():
    try:
        for o in range(1, len(table)):
            if "п_1_доп" in table[o]:
                del table[o]
    except IndexError:
        for o in range(1, len(table) - 1):
            if "п_1_доп" in table[o]:
                del table[o]

    try:
        for o in range(1, len(table)):
            if "п_2_доп" in table[o]:
                del table[o]
    except IndexError:
        for o in range(1, len(table) - 1):
            if "п_2_доп" in table[o]:
                del table[o]

    try:
        for o in range(1, len(table)):
            if "п_3_доп" in table[o]:
                del table[o]
    except IndexError:
        for o in range(1, len(table) - 1):
            if "п_3_доп" in table[o]:
                del table[o]


def from_perfusion_dop_to_perfusion_1():
    for k in range(1, len(table) - 1):
        if "сер_1" in table[k]:
            for r in range(1, len(table)):
                if "сер_1_доп" in table[r]:
                    list2 = [f"{table[k][5]},\n{table[r][5]}"]
                    result = ', '.join(str(item) for item in list2)
                    table[k][5] = result

    for k in range(1, len(table) - 1):
        if "сер_1" in table[k]:
            for r in range(1, len(table)):
                if "сер_1_доп" in table[r]:
                    list2 = [f"{table[k][4]},\n{table[r][4]}"]
                    result = ',\n'.join(str(item) for item in list2)
                    table[k][4] = result


def from_perfusion_dop_to_perfusion_2():
    for k in range(1, len(table) - 1):
        if "сер_2" in table[k]:
            for r in range(1, len(table)):
                if "сер_2_доп" in table[r]:
                    list2 = [f"{table[k][5]},\n{table[r][5]}"]
                    result = ', '.join(str(item) for item in list2)
                    table[k][5] = result

    for k in range(1, len(table) - 1):
        if "сер_2" in table[k]:
            for r in range(1, len(table)):
                if "сер_2_доп" in table[r]:
                    list2 = [f"{table[k][4]},\n{table[r][4]}"]
                    result = ', '.join(str(item) for item in list2)
                    table[k][4] = result


def from_perfusion_dop_to_perfusion_3():
    for k in range(1, len(table) - 1):
        if "сер_3" in table[k]:
            for r in range(1, len(table)):
                if "сер_3_доп" in table[r]:
                    list2 = [f"{table[k][5]},\n{table[r][5]}"]
                    result = ', '.join(str(item) for item in list2)
                    table[k][5] = result

    for k in range(1, len(table) - 1):
        if "сер_3" in table[k]:
            for r in range(1, len(table)):
                if "сер_3_доп" in table[r]:
                    list2 = [f"{table[k][4]},\n{table[r][4]}"]
                    result = ','.join(str(item) for item in list2)
                    table[k][4] = result


def delete_unneccesary_perfusion_info():
    try:
        for o in range(1, len(table)):
            if "сер_1_доп" in table[o]:
                del table[o]
    except IndexError:
        for o in range(1, len(table) - 1):
            if "сер_1_доп" in table[o]:
                del table[o]

    try:
        for o in range(1, len(table)):
            if "сер_2_доп" in table[o]:
                del table[o]
    except IndexError:
        for o in range(1, len(table) - 1):
            if "сер_2_доп" in table[o]:
                del table[o]

    try:
        for o in range(1, len(table)):
            if "сер_3_доп" in table[o]:
                del table[o]
    except IndexError:
        for o in range(1, len(table) - 1):
            if "сер_3_доп" in table[o]:
                del table[o]


def rename_studies():
    for n in range(1, len(table)):
        if "п_1" in table[n]:
            table[n][0] = "паращитавидка"
        elif "п_2" in table[n]:
            table[n][0] = "паращитавидка"
        elif "п_3" in table[n]:
            table[n][0] = "паращитавидка"
        elif "сер_1" in table[n]:
            table[n][0] = "сердце"
        elif "сер_2" in table[n]:
            table[n][0] = "сердце"
        elif "сер_3" in table[n]:
            table[n][0] = "сердце"
        elif "скелет_1ч" in table[n]:
            table[n][0] = "скелет"
        elif "скелет_3ч" in table[n]:
            table[n][0] = "скелет"



# calculations
table = [['', 'Приход', 'Перв_осм', 'Замер/стресс', 'Введение', 'Исследование', '', '']]
studies = []

for keys, value in MENU.items():
    studies.append(keys)
studies = ', '.join(str(item) for item in studies)
print("\n")
print("Виды исследовании ОФЭКТ/КТ:")
print(studies)
study = (input("Напишите название исследования из списка: ")).lower()

while study not in MENU:
    print("Пишите только то, что в списке!")
    study = (input("Напишите название исследования из списка: ")).lower()

injection = input("Напишите время введения препарата первому пациенту в формате (чч:мм:сс): ")

injection_in_s = time_to_sec(injection)

if study in MENU:
    list = []
    calculate(study)

n = 1
is_on = True
while is_on:
    print("\n")
    next_study_input = (input("Добавите еще исследование? Если да, то какое? ")).lower()
    if next_study_input == "нет":
        is_on = False
        break
    additional_is_on = True
    while next_study_input not in MENU and additional_is_on:
        print("Пишите только то, что в списке!")
        next_study_input = (input("Напишите название исследования из списка: ")).lower()
        if next_study_input == "нет":
            additional_is_on = False
            is_on = False
    n += 1
    list = []
    if next_study_input == "почки" or next_study_input == "щитавидка":
        calculate_renal_thyroid(next_study_input)
    elif next_study_input == "п_1":
        calculate_parathyroid_1(next_study_input)
    elif next_study_input == "п_1_доп":
        calculate_parathyroid_1_dop(next_study_input)
    elif next_study_input == "п_2":
        calculate_parathyroid_2(next_study_input)
    elif next_study_input == "п_2_доп":
        calculate_parathyroid_2_dop(next_study_input)
    elif next_study_input == "п_3":
        calculate_parathyroid_3(next_study_input)
    elif next_study_input == "п_3_доп":
        calculate_parathyroid_3_dop(next_study_input)
    elif next_study_input == "сер_1":
        calculate_perf_1(next_study_input)
    elif next_study_input == "сер_1_доп":
        calculate_perf_1_dop(next_study_input)
    elif next_study_input == "сер_2":
        calculate_perf_2(next_study_input)
    elif next_study_input == "сер_2_доп":
        calculate_perf_2_dop(next_study_input)
    elif next_study_input == "сер_3":
        calculate_perf_3(next_study_input)
    elif next_study_input == "сер_3_доп":
        calculate_perf_3_dop(next_study_input)
    else:
        calculate_2(next_study_input)

#some works with tables, so any med employee (be it physician, physicist, chemist, etc.) can easily understand the table
seconds_to_hours_and_mins()
check_for_syringe_equal_to_injection()
assemble_begin_and_end()
from_parathyroid_dop_to_parathyroid_1()
from_parathyroid_dop_to_parathyroid_2()
from_parathyroid_dop_to_parathyroid_3()
from_perfusion_dop_to_perfusion_1()
from_perfusion_dop_to_perfusion_2()
from_perfusion_dop_to_perfusion_3()
delete_last_column()
delete_unneccesary_parathyroid_info()
delete_unneccesary_perfusion_info()
rename_studies()

#transferring to excel
print("Проверьте excel файл под названием 'spect-ct_scheduling.xlsx'")
df = pandas.DataFrame(table)
writer = pandas.ExcelWriter('spect-ct_scheduling.xlsx')
df.to_excel(writer, sheet_name='my_analysis', index=False)

for column in df:
    column_width = max(df[column].astype(str).map(len).max(), column)
    col_idx = df.columns.get_loc(column)
    writer.sheets['my_analysis'].set_column(col_idx, col_idx, column_width)

writer.save()
