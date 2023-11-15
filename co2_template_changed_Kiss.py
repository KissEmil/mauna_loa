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

# author: 	Thomas Haslwanter
# date: 	19-Oct-2023

# changed on: 14-Nov-2023
# changed by: Kiss Emil

# Import the main packages
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd


def crossings(data: pd.DataFrame, threshold: float) -> str:
    """
    Function crossings:
    Input: pandas dataframe, containing the data of 'co2_mm_mlo.txt', here called data
           threshold, border value, here called threshold
    
    Processing: Function looks, where the the co2 values of each month of the year (data.co2) crossed the threshold
                Then crossings are calculated ba looking, where the argument: over the threshold, changes from 0 to 1 or False to True (Positions: Where was the co2 value below threshold)
                1 is added to every crossing position to get the Postitions, where the co2 values were over threshold
                With the Element 0 (First crossing of threshold) year and month of the crossing are selected
                
    Output: Returns a string for when (year-month) the co2 value reached the threshold for the first time
    """
    
    # Overshoot: Where is data.co2 equal or bigger as threshold
    overshoot = data.co2 > threshold
    
    # When do the crossings of the threshold happen?
    # And when is the first time we are at or over threshold
    crossing = np.where(np.diff(overshoot*1)==1)[0] + 1

    # Get the date of the position, where threshold was reached
    x = datetime.datetime(data.year[crossing[0]], data.month[crossing[0]], 1)
    
    # Return string in specific format
    return_string = f'The first time we crossed {threshold} ppm was {x.strftime("%Y-%B")}.'
    return return_string


if __name__ == '__main__':
    """
    Main
    Reads in txt file 'co2_mm_mlo.txt' and creates a pandas dataframe
    Calls function crossings with pd.dataframe (data) and threshold (threshold)
    Gets string back from function crossings and prints string
    Calculates, where the values of data.co2 were below threshold
    Plots data.co2
    """

    # Read in the data
    in_file = 'co2_mm_mlo.txt'
    threshold = 420

    data = pd.read_csv(in_file, skiprows=42, header=None,
                       delim_whitespace=True)
    data.columns = ['year', 'month', 'date', 'co2',
                    'co2_avg', 'days', 'std', 'uncertainty']

    # First time above threshold
    overshoot_date = crossings(data, threshold)
    print(f'{overshoot_date}')

    # Last time below threshold
    index = np.where(data.co2 < threshold)[0][-1]
    x = datetime.datetime(data.year[index], data.month[index], 1)
    print(f'The last time we were below {threshold} ppm was {x.strftime("%Y-%B")}.')

    # And finally, plot the data
    data.plot('date', 'co2', color='green', label='co2 ppm-level of every month')
    plt.axhline(threshold, ls='dashed', color='red', label='threshold')
    
    plt.ylabel('Co2-Level in ppm')
    plt.xlabel('Year')
    plt.legend()
    plt.show()
