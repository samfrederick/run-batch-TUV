"""
TUV default inputs:
==================================================================
inpfil =      usrinp   outfil =      usrout   nstr =            -2
lat =          0.000   lon =          0.000   tmzone =         0.0
iyear =         2002   imonth =           3   iday =            21
zstart =       0.000   zstop =       80.000   nz =              81
wstart =     280.000   wstop =      420.000   nwint =          140
tstart =      12.000   tstop =       20.000   nt =              10
lzenit =           F   alsurf =       0.100   psurf =       -999.0
o3col =      300.000   so2col =       0.000   no2col =       0.000
taucld =       0.000   zbase =        4.000   ztop =         5.000
tauaer =       0.235   ssaaer =       0.990   alpha =        1.000
dirsun =       1.000   difdn =        1.000   difup =        0.000
zout =         0.000   zaird =   -9.990E+02   ztemp =     -999.000
lirrad =           T   laflux =           F   lmmech =           F
lrates =           T   isfix =            0   nms =              7
ljvals =           F   ijfix =            0   nmj =              0
iwfix =            0   itfix =            0   izfix =            0
==================================================================

************* Can overwrite basic inputs here manually:
* Input and output files:
*   inpfil = input file name
*   outfil = output file name
* Radiative transfer scheme:
*   nstr = number of streams
*          If nstr < 2, will use 2-stream Delta Eddington
*          If nstr > 1, will use nstr-stream discrete ordinates
* Location (geographic):
*   lat = LATITUDE (degrees, North = positive)
*   lon = LONGITUDE (degrees, East = positive)
*   tmzone = Local time zone difference (hrs) from Universal Time (ut):  
*            ut = timloc - tmzone
* Date:
*   iyear = year (1950 to 2050)
*   imonth = month (1 to 12)
*   iday = day of month
* Time of day grid:
*   tstart = starting time, local hours
*   tstop = stopping time, local hours
*   nt = number of time steps
*   lzenit = switch for solar zenith angle (sza) grid rather than time 
*             grid. If lzenit = .TRUE. then 
*                tstart = first sza in deg., 
*                tstop = last sza in deg., 
*                nt = number of sza steps. 
*                esfact = 1. (Earth-sun distance = 1.000 AU)
* Vertical grid:
*   zstart = surface elevation above sea level, km
*   zstop = top of the atmosphere (exospheric), km
*   nz = number of vertical levels, equally spaced
*        (nz will increase by +1 if zout does not match altitude grid)
* Wavlength grid:
*   wstart = starting wavelength, nm
*   wstop  = final wavelength, nm
*   nwint = number of wavelength intervals, equally spaced
*           if nwint < 0, the standard atmospheric wavelength grid, not
*           equally spaced, from 120 to 735 nm, will be used. In this
*           case, wstart and wstop values are ignored.
* Surface condition:
*   alsurf = surface albedo, wavelength independent
*   psurf = surface pressure, mbar.  Set to negative value to use
*           US Standard Atmosphere, 1976 (USSA76)
* Column amounts of absorbers (in Dobson Units, from surface to space):
*          Vertical profile for O3 from USSA76.  For SO2 and NO2, vertical
*          concentration profile is 2.69e10 molec cm-3 between 0 and 
*          1 km above sea level, very small residual (10/largest) above 1 km.
*   o3_tc = ozone (O3)
*   so2_tc = sulfur dioxide (SO2)
*   no2_tc = nitrogen dioxide (NO2)
* Cloud, assumed horizontally uniform, total coverage, single scattering
*         albedo = 0.9999, asymmetry factor = 0.85, indep. of wavelength,
*         and also uniform vertically between zbase and ztop:
*   taucld = vertical optical depth, independent of wavelength
*   zbase = altitude of base, km above sea level
*   ztop = altitude of top, km above sea level
* Aerosols, assumed vertical provile typical of continental regions from
*         Elterman (1968):
*   tauaer = aerosol vertical optical depth at 550 nm, from surface to space. 
*           If negative, will default to Elterman's values (ca. 0.235 
*           at 550 nm).
*   ssaaer = single scattering albedo of aerosols, wavelength-independent.
*   alpha = Angstrom coefficient = exponent for wavelength dependence of 
*           tauaer, so that  tauaer1/tauaer2  = (w2/w1)**alpha.
* Directional components of radiation, weighting factors:
*   dirsun = direct sun
*   difdn = down-welling diffuse
*   difup = up-welling diffuse
*        e.g. use:
*        dirsun = difdn = 1.0, difup = 0 for total down-welling irradiance
*        dirsun = difdn = difup = 1.0 for actinic flux from all directions
*        dirsun = difdn = 1.0, difup = -1 for net irradiance
* Output altitude:
*   zout = altitude, km, for desired output.
*        If not within 1 m of altitude grid, an additional
*        level will be inserted and nz will be increased by +1.
*   zaird = air density (molec. cm-3) at zout.  Set to negative value for
*        default USSA76 value interpolated to zout.
*   ztemp = air temperature (K) at zout.  Set to negative value for
*        default USSA76 value interpolated to zout.
* Output options, logical switches:
*   lirrad = output spectral irradiance
*   laflux = output spectral actinic flux
*   lmmech = output for NCAR Master Mechanism use
*   lrates = output dose rates (UVB, UVA, CIE/erythema, etc.)
* Output options, integer selections:
*   isfix:  if > 0, output dose rate for action spectrum is=isfix, tabulated
*           for different times and altitudes.
*   ijfix:  if > 0, output j-values for reaction ij=ijfix, tabulated
*           for different times and altitudes.
*   iwfix:  if > 0, output spectral irradiance and/or spectral actinic
*           flux at wavelength iw=iwfix, tabulated for different times
*           and altitudes.
*   itfix:  if > 0, output spectral irradiance and/or spectral actinic
*           flux at time it=itfix, tabulated for different altitudes
*           and wavelengths.
*   izfix:  if > 0, output spectral irradiance and/or spectral actinic
*           flux at altitude iz=izfix, tabulated for different times
*           and wavelengths.
*   nms:    number of dose rates that will be reported. Selections must be 
*           made interactively, or by editing input file.
*   nmj:    number of j-values that will be reported. Selections must be 
*           made interactively, or by editing input file.
* The following default settings are also found in the input file 'defin1':

inpfil = defin1
outfil = usrout
nstr = -2
lat = 0.
lon = 0.
tmzone = 0.
iyear = 2002
imonth = 3
iday = 21
zstart = 0.
zstop = 80.
nz = 80
wstart = 280.
wstop = 420.
nwint = 140
tstart = 12.
tstop = 20.
nt = 5
lzenit = False
alsurf = 0.1
psurf = -999.
o3col = 300.
so2col = 0.
no2col = 0.
taucloud = 0.
zbase = 4.
ztop = 5.
tauaer = 0.235
ssaaer = 0.99
alpha = 1.
dirsun = 1.
difdn = 1.
difup = 0.
zout = 0.
zaird = -999.
ztemp = -999.
lirrad = True
laflux = False
lmmech = False
lrates = True
isfix = 0
ljvals = False
ijfix = 0
iwfix = 0
itfix = 0
izfix = 0
nms = 7
nmj = 0

UVA: 315-400 nm
UVB: 280-315 nm
UVC: 100-280 nm

"""
import subprocess
import os
import numpy as np
import pandas as pd
from modify_usrinp import modifyInput

def batch_test():
    # NOTE test: change the number of time increments
    nt_range = np.arange(1, 11, 1)
    for i, nt_val in enumerate(nt_range):
        print(f'TUV Run: {i+1}'.center(20))
        print(20*'-')
        modified_variables = {'nt': nt_val
                                }
        modifyInput(modified_variables)
        
        subprocess.run(['./tuv'], stdout=subprocess.PIPE)
        os.rename('/data/keeling/a/sf20/d/usrout.txt', f'/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/DATA/usrout-{i}.txt')
        os.rename('/data/keeling/a/sf20/d/tuvlog.txt', f'/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/LOG/tuvlog-{i}.txt')
        print('\n')

def setInputs(**kwargs):
    inputs = {
        'inpfil' : 'defin1',
        'outfil' : 'usrout',
        'nstr' : -2,
        'lat' : 0.,
        'lon' : 0.,
        'tmzone' : 0.,
        'iyear' : 2002,
        'imonth' : 3,
        'iday' : 21,
        'zstart' : 0.,
        'zstop' : 80.,
        'nz' : 80,
        'wstart' : 280.,
        'wstop' : 420.,
        'nwint' : 140,
        'tstart' : 12.,
        'tstop' : 20.,
        'nt' : 5,
        'lzenit' : False,
        'alsurf' : 0.1,
        'psurf' : -999.,
        'o3col' : 300.,
        'so2col' : 0.,
        'no2col' : 0.,
        'taucld' : 0.,
        'zbase' : 4.,
        'ztop' : 5.,
        'tauaer' : 0.235,
        'ssaaer' : 0.99,
        'alpha' : 1.,
        'dirsun' : 1.,
        'difdn' : 1.,
        'difup' : 0.,
        'zout' : 0.,
        'zaird' : -999.,
        'ztemp' : -999.,
        'lirrad' : True,
        'laflux' : False,
        'lmmech' : False,
        'lrates' : True,
        'isfix' : 0,
        'ljvals' : False,
        'ijfix' : 0,
        'iwfix' : 0,
        'itfix' : 0,
        'izfix' : 0,
        'nms' : 7,
        'nmj' : 0,
    }
    iterable_vars = []
    for item in kwargs:
        if item not in inputs.keys():
            if item in ('iterable_i', 'iterable_j', 'iterable_k'):
                iterable_vars.append(kwargs[item])
                continue
            else:
                raise AttributeError(f'Invalid parameter name: "{item}"')
        inputs[item] = kwargs[item]
            
    return inputs, iterable_vars

def batch_run(data_subdir, **kwargs):
    output_path = '/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/'
    dirExist = os.path.exists(output_path)
    if not dirExist:
        os.mkdir(output_path)

    os.mkdir(f'/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/{data_subdir}')
    os.mkdir(f'/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/{data_subdir}/data')
    os.mkdir(f'/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/{data_subdir}/log')

    input_dict, iterable_vars = setInputs(**kwargs)

    # create mesh for i and j parameters
    iter_ivar_name = kwargs.get('iterable_i', None) # month
    iter_jvar_name =kwargs.get('iterable_j', None) # lat
    iter_kvar_name =kwargs.get('iterable_k', None) # ozone column

    iterate_i = False
    iterate_j = False
    if (iter_ivar_name is not None):
        iterate_i = True
        idim = input_dict[iter_ivar_name].size
        if (iter_jvar_name is not None):
            iterate_j = True
            iterable_i_mesh, iterable_j_mesh = np.meshgrid(input_dict[iter_ivar_name], 
                                                           input_dict[iter_jvar_name])
            jdim = input_dict[iter_jvar_name].size
            i_index_mesh, j_index_mesh = np.meshgrid(np.arange(idim), np.arange(jdim))

            flat_iterable_i_mesh = iterable_i_mesh.flatten()
            flat_iterable_j_mesh = iterable_j_mesh.flatten()
            flat_i_index_mesh = i_index_mesh.flatten()
            flat_j_index_mesh = j_index_mesh.flatten()
            iterable_vars_dict = {iter_ivar_name: flat_iterable_i_mesh,
                                  iter_jvar_name: flat_iterable_j_mesh}
        else:
            iterable_i_mesh = input_dict[iter_ivar_name]
            i_index_mesh = np.arange(idim)
            flat_iterable_i_mesh = iterable_i_mesh.flatten()
            flat_i_index_mesh = i_index_mesh
            iterable_vars_dict = {iter_ivar_name: flat_iterable_i_mesh}
    else:
        raise AttributeError('No iterable parameters specified')
    
    if iter_kvar_name:
        iterable_k_mesh = input_dict[iter_kvar_name]
        #kdim = input_dict[iter_kvar_name].size
        flat_iterable_k_mesh = iterable_k_mesh.flatten()
        iterable_vars_dict[iter_kvar_name] = flat_iterable_k_mesh

    total_iterations = flat_i_index_mesh.size
    for iteration in range(total_iterations):

        i = flat_i_index_mesh[iteration]
        file_iter_label = f'{i}'
        if iterate_j:
            j = flat_j_index_mesh[iteration]
            file_iter_label = f'{i}-{j}'

        output_filename = f'/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/{data_subdir}/data/usrout-{file_iter_label}.txt'
        log_filename = f'/data/keeling/a/sf20/d/TUV-V5.4/OUTPUT/{data_subdir}/log/tuvlog-{file_iter_label}.txt'

        for var in iterable_vars:
            input_dict[var] = iterable_vars_dict[var][iteration]
            #print(input_dict[var])
        if any(np.isnan(input_dict[var]) for var in iterable_vars):
            print(f'..{var}={input_dict[var]}, skipping iteration {iteration+1}')
            continue

        print(f'TUV Run: {iteration+1}/{total_iterations}'.center(20))
        
        modifyInput(input_dict)
        
        subprocess.run(['./tuv'], stdout=subprocess.PIPE)
        os.rename('/data/keeling/a/sf20/d/usrout.txt', output_filename)
        os.rename('/data/keeling/a/sf20/d/tuvlog.txt', log_filename)

if __name__ == '__main__':

    # ITERABLE PARAMETERS
    # -------------------
    lat_spacing = 1#5
    lat_min = -89.5 #-90
    lat_max = 89.5 #90
    month_start = 1
    month_end = 12
    month_spacing = 1
    lat_range = np.arange(lat_min, lat_max + 1, lat_spacing)
    imonth_range = np.arange(month_start, month_end + 1, month_spacing)

    # Get seasonal TOC trend
    data_path = '/data/keeling/a/sf20/d/TUV-V5.4/omi-data/processed-seasonal-cycle/2005/'
    filename = 'omi_TOC_monthly-longavg_2005.csv'
    seasonal_TOC_trend = np.array(pd.read_csv(data_path + filename, index_col=0))

    # lower the latitude resolution of TOC to be 5 degrees instead of 1 for comp. effic.
    lat_range = lat_range[5::5] # sets the range to -84.5 to 85.5
    seasonal_TOC_trend = seasonal_TOC_trend[5::5]

    batch_run(data_subdir='general-iter-test-2',
        #data_subdir='seasonal-toc-2005-latres5deg',
        # CONSTANT PARAMETERS 
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
        # ITERABLE PARAMETERS (assigned subsequently looping over values)
        iterable_i = 'imonth',
        #iterable_j = 'lat',
        #iterable_k = 'o3col',
        imonth = imonth_range,
        #lat = lat_range, 
        #o3col = seasonal_TOC_trend, 
        )


    