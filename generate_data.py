"""This module takes the values we want to apply in the model and saves
them in a file deuteron_values.jsonl to later use them in our functions.
"""

import jsonlines

# DATA FOR DEUTERON MODEL
data_deuteron = [
    {"Potential": "Central", "Depth_c": 13.888, "Range_c": 2.8},
    {"Potential": "Tensor", "Depth_t": 10.7632, "Range_t": 2.8},
    {"Initial conditions": "us wavefunction", "us_0": 0.5, "vs_0": 1.0},
    {"Initial conditions": "ud wavefunction", "ud_0": 0.125, "vd_0": 0.5},
    {"Boundary conditions": "us wavefunction", "us_fin": 0.038, "vs_fin": -0.012},
    {"Boundary conditions": "Derivatives", "ud_fin": 0.00038, "vd_fin": -0.0001},
    {"Range of radius": "Range r", "r_initial": 0.5, "r_final": 10.0},
    {"Energy guess": -2.225}
]

file_name = "deuteron_values.jsonl"

# WRITE VALUES IN THE FILE
with jsonlines.open(file_name, mode='w') as writer:
    writer.write_all(data_deuteron)

print(f"'{file_name}' file has been created with the deuteron data in JSON lines format.")
