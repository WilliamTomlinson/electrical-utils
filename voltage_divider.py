"""
A prongram that calculates what valued components to use to fill certain tasks
while still conforming to the main e-series'.
"""

import e_series

def volt_div_approx(e_series, v_in, v_out):
    """ Takes an input voltage and an output voltage to determine
    a pairng of resistors from a selected e-series that best approximates 
    the output voltage.

    volt_div_approx() returns a tuple: (R1, R2, best approximation)
    """
    e_series = E_SERIES[e_series]
    v_best = v_in
    for R1 in e_series:
        for R2 in e_series:
            v_x = v_in * (R1 / (R1 + R2))
            if (v_best < v_x < v_out) or (v_out < v_x < v_best):
                v_best = v_x
                r_pair = (R1, R2, round(v_best, 4))
    return r_pair

def get_volt_div():
    series = input("What E-Series should be used? ")
    series_index = query_interpretter(series);
    v_in = input("What is the input voltage? ")
    v_out = input("What is the desired output voltage? ")
    print(volt_div_approx(series_index, v_in, v_out))