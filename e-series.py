import numpy as np
E3 = np.array([1.0, 2.2, 4.7])
E6 = np.array([1.0, 1.5, 2.2, 3.3, 4.7, 6.8])
E12 = np.array([1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2])
E24 = np.array([1.00, 1.05, 1.10, 1.15, 1.21, 1.27,
        1.33, 1.40, 1.47, 1.54, 1.62, 1.69,
        1.78, 1.87, 1.96, 2.05, 2.15, 2.26,
        2.37, 2.49, 2.61, 2.74, 2.87, 3.01,
        3.16, 3.32, 3.48, 3.65, 3.83, 4.02,
        4.22, 4.42, 4.64, 4.87, 5.11, 5.36,
        5.62, 5.90, 6.19, 6.49, 6.81, 7.15,
        7.50, 7.87, 8.25, 8.66, 9.09, 9.53])
        
E_SERIES = [E3, E6, E12, E24]

def query_interpretter(number):
    """
    Returns the index in E_SERIES that corresponds with the number given.
    """
    if number == 3:
        return 0
    elif number == 6:
        return 1
    elif number == 12:
        return 2;
    elif number == 24:
        return 3