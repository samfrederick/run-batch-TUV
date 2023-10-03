import numpy as np
from run_tuv_batch import batch_run # since this is a relative import, make sure you're in the TUV-V5.4 home directory!

"""
In example 1, we're just letting the month vary from Jan. to Dec. Everything
else is the same across simulation runs.
"""

# Here you should create arrays for parameters you wish to iterate over. I create
# an array 'imonth_range' that contains [1, 2, ..., 12]. this is then passed to 
# the 'imonth' argument in batch_run() below.
month_start = 1 # January
month_end = 12 # December 
month_spacing = 1
imonth_range = np.arange(month_start, month_end + 1, month_spacing)

batch_run(data_subdir='example-1-output',
        # CONSTANT PARAMETERS (these will be the same across simulation runs)
        iday = 1, 
        tstart = 12.0,
        tstop = 12.01,
        nt = 1,
        wstart = 205.0, # Shortest wavelength I can go without getting runtime error
        wstop = 420.0,
        nwint = -156, #215, # for wavelengths lower than 205
        tauaer = 0,
        ssaaer = 0,
        alpha = 0,
        # ITERABLE PARAMETERS (loop over values in iterable arrays for parameters you'd like to vary)
        iterable_i = 'imonth', # specify the name of the parameter that will be iterated over
        imonth = imonth_range, # pass the array of months to the imonth parameter
        )