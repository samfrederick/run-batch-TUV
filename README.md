# User Guide for run_tuv_batch

‘run_tuv_batch.py’ is a python module for running TUV in batch mode, whereby multiple simulations are run and corresponding outputs are saved based on parameters that the user specifies should be iterated over.

# Installation

You’ll need to modify the TUV source code to change the execution mode from interactive to non-interactive. To do so, navigate to TUV.f in the main TUV-V5.4 directory. Scroll down to line 237 where you should see the following 

```
      intrct = .TRUE.
c      intrct = .FALSE.
      IF ( .NOT. intrct) inpfil = 'usrinp'
```

Comment out line 237 by typing ‘c’ before the ‘intrct…’ statement. Then uncomment line 238. This switches TUV to non-interactive mode and will load the simulation based on the input parameters in the ‘usrinp’ text file.
Since the source code has been modified, open up a terminal, make sure you are in the TUV-V5.4 directory, and type ‘make’ to recompile the source code. 
Place the two python files fo rrun_tuv_batch, ‘run_tuv_batch.py’ and ‘modify_usrinp.py’, in the main TUV-V5.4 directory. That’s it!


# Using run_tuv_batch
 
The module allows easy customization based on the parameter or parameters that you wish to iterate over. You can vary up to three parameters at a time, where each can be understood as iterating over an x-dimension, a y-dimension, and a z-dimension

Here are a few examples to get you started:

example1_run_tuv_batch.py
Run a batch of 12 simulations where the month starts at January, ends in December, and steps by 1 month for each simulation.
Since we just iterate over 1 dimension corresponding to months in the year, the argument ‘iterable_i’ is set to the ‘imonth’ parameter. 
example2_run_tub_batch.py
Run a batch of 228 simulations where, similar to the first example, the month is varied from January to December over the first dimension. Along the second dimension, the latitude is varied from -90 to 90 degrees in steps of 10 degrees. 


# Output

Each time you run a batch execution with run_tuv_batch, you have to specify the subdirectory location where the output data are saved. This is located at ‘TUV-V5.4/OUTPUT/[name-of-your-subdirectory]’. 

Within this subdirectory you’ll find a ‘data’ and a ‘log’ folder. The ‘data’ folder contains all of the results from TUV for spectral irradiances, reaction rates, weighting functions, etc. The filenames for data depend on the number of parameters that you iterate over. If you just iterate over one dimension, the filename will appear like ‘usrout-{i}.txt’ where ‘i’ varies from 0 to the number of iterations along that dimension minus 1. Similarly, if you vary two parameters, the filename output will appear like ‘usrout-{i}-{j}.txt’.
 
The ‘log’ folder contains text files with a description of each simulation in case you need to review what the parameter settings were in one of the simulations you ran. 
