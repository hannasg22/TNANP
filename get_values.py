"""This module defines all variables described in deuteron_values.jsonl
to later use them in the rest of the code.
We will have functions getting the values for:
    - Potentials' depth and range
    - Initial conditions
    - Boundary conditions
    - Range of radius r
    - Energy guess value
"""

import jsonlines

def central_V():
    file_name = "deuteron_values.jsonl"
    depth_and_range_c = [] # Form of the list will be [V0_c, r0_c]

    # Open values_deuteron.jsonl file and read the potential data
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Potential" in line:
                if "Depth_c" in line:
                    depth_and_range_c.append(line["Depth_c"])
                if "Range_c" in line:
                    depth_and_range_c.append(line["Range_c"])
    return depth_and_range_c

def tensorial_V():
    file_name = "deuteron_values.jsonl"
    depth_and_range_t = [] # Form of the list will be [V0_t, r0_t]

    # Open values_deuteron.jsonl file and read the potential data
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Potential" in line:
                if "Depth_t" in line:
                    depth_and_range_t.append(line["Depth_t"])
                if "Range_t" in line:
                    depth_and_range_t.append(line["Range_t"])
    return depth_and_range_t

def initial_conditions_A():
    file_name = "deuteron_values.jsonl"
    init_cond = [] # Form of the vector: [us_0A, vs_0A, ud_0A, vd_0A]

    # Open file and read initial conditions A
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Initial conditions A" in line:
                if "us_0" in line:
                    init_cond.append(line["us_0"])
                if "vs_0" in line:
                    init_cond.append(line["vs_0"])
                if "ud_0" in line:
                    init_cond.append(line["ud_0"])
                if "vd_0" in line:
                    init_cond.append(line["vd_0"])
    return init_cond

def initial_conditions_B():
    file_name = "deuteron_values.jsonl"
    init_cond = [] # Form of the vector: [us_0B, vs_0B, ud_0B, vd_0B]

    # Open file and read initial conditions B
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Initial conditions B" in line:
                if "us_0" in line:
                    init_cond.append(line["us_0"])
                if "vs_0" in line:
                    init_cond.append(line["vs_0"])
                if "ud_0" in line:
                    init_cond.append(line["ud_0"])
                if "vd_0" in line:
                    init_cond.append(line["vd_0"])
    return init_cond
  
def boundary_conditions_C():
    file_name = "deuteron_values.jsonl"
    bound_cond = []

    # Open file and read boundary conditions C
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Boundary conditions C" in line:
                if "us_fin" in line:
                    bound_cond.append(line["us_fin"])
                if "vs_fin" in line:
                    bound_cond.append(line["vs_fin"])
                if "ud_fin" in line:
                    bound_cond.append(line["ud_fin"])
                if "vd_fin" in line:
                    bound_cond.append(line["vd_fin"])
    return bound_cond

def boundary_conditions_D():
    file_name = "deuteron_values.jsonl"
    bound_cond = []

    # Open file and read boundary conditions D
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Boundary conditions D" in line:
                if "us_fin" in line:
                    bound_cond.append(line["us_fin"])
                if "vs_fin" in line:
                    bound_cond.append(line["vs_fin"])
                if "ud_fin" in line:
                    bound_cond.append(line["ud_fin"])
                if "vd_fin" in line:
                    bound_cond.append(line["vd_fin"])
    return bound_cond

def range_of_radius():
    file_name = "deuteron_values.jsonl"
    r_range = []

    # Open file and read values for minimum and maximum r
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Range of radius" in line:
                if "r_initial" in line:
                    r_range.append(line["r_initial"])
                if "r_final" in line:
                    r_range.append(line["r_final"])
    return r_range

def energy_guess():
    file_name = "deuteron_values.jsonl"

    # Open file and read first guess of E value
    with jsonlines.open(file_name, mode='r') as reader:
        for line in reader:
            if "Energy guess" in line:
                E_guess = line["Energy guess"]
    return E_guess
