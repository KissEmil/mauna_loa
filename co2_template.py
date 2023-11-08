""" Demo-exercise, using CO2-data from Mauna Loa
- Read in the data from 'co2_mm_mlo.txt'.
- Write a function that takes those data, as well as a threshold (in 'ppm'), and returns
    the first month when that threshold was crossed.
- Apply this function to the threshold of 420, and display the result like (for 360):
    'The first time we crossed 360 ppm was 1993-May.'
- Plot the rising CO2-data, as well as the threshold.

Tips:
    - np.where can be used to find events
    - The package datetime can be used to display the date in any desired format:

        import datetime
        # date = datetime.datetime(year, month, date)
        date = datetime.datetime(2023, 10, 1)
        print(date.str2time("%Y-%B"))
        >>> 2023-October

"""
# [xxx ------- Needs to be finished -------- xxx]


# author: 	Thomas Haslwanter
# date: 	19-Oct-2023

# Import the main packages
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd


def crossings(data: pd.DataFrame, threshold: float) -> str:
    """ When is the threshold crossed for the first time """

    # [xxx ------ This has to be done ------------ xxx]

    return_string = 'dummy text'
    return return_string


if __name__ == '__main__':
    """ Here comes the main part """

    # Read in the data
    in_file = 'co2_mm_mlo.txt'
    threshold = 360

    data = pd.read_csv(in_file, skiprows=42, header=None,
                       delim_whitespace=True)
    data.columns = ['year', 'month', 'date', 'co2',
                    'co2_avg', 'days', 'std', 'uncertainty']

    # First time above threshold
    date = crossings(data, threshold)
    print(
        f'The first time we crossed {threshold} ppm was {date}.')

    # Last time below threshold
    index = np.where(data.co2 < 360)[0][-1]
    x = datetime.datetime(data.year[index], data.month[index], 1)
    print(
        f'The last time we were below {threshold} ppm was {x.strftime("%Y-%B")}.')

    # And finally, plot the data
    data.plot('date', 'co2')
    plt.axhline(threshold, ls='dashed')
    plt.show()
