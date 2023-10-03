import pandas as pd
import csv

reference_filepath = '/data/keeling/a/sf20/d/TUV-V5.4/INPUTS/usrinp_backup'
outfile = '/data/keeling/a/sf20/d/TUV-V5.4/INPUTS/usrinp'

def createInputsDataset():
    
    inputs = pd.read_csv(reference_filepath, header=None, skiprows=2, nrows=16, delim_whitespace=True).drop(columns=[1,4,7])
    #inputs = pd.read_csv(filepath, header=None, skiprows=2, nrows=16,)# delimiter=' ')
    inputs1 = inputs[[0, 2]].rename(columns={0:"varname", 2:"value"})
    inputs2 = inputs[[3, 5]].rename(columns={3:"varname", 5:"value"})
    inputs3 = inputs[[6, 8]].rename(columns={6:"varname", 8:"value"})

    inputs_formatted = pd.concat([inputs1, inputs2])
    inputs_formatted = pd.concat([inputs_formatted, inputs3]).reset_index(drop=True)

    return inputs_formatted

def modifyInput(modified_variables):

    inputs_formatted = createInputsDataset()

    for var_name, var_value in modified_variables.items():
        var_value = formatVarType(var_name, var_value)
        var_idx = inputs_formatted[inputs_formatted['varname']== var_name].index[0]
        inputs_formatted.loc[var_idx, 'value'] = var_value
        #print(f'..setting {var_name}: {var_value:>10}')

    inputs1_formatted = pd.DataFrame(inputs_formatted.loc[0:15, :])
    inputs2_formatted = pd.DataFrame(inputs_formatted.loc[16:31, :])
    inputs3_formatted = pd.DataFrame(inputs_formatted.loc[32:, :])

    # Create a temporary csv file to store the modified variable info
    with open('modified-vars', 'w') as csvfile:
        for row1, row2, row3 in zip(inputs1_formatted.iterrows(), 
                                    inputs2_formatted.iterrows(), 
                                    inputs3_formatted.iterrows()):
            #idx1 = row1[0]
            attributes1 = row1[1]
            var1 = attributes1.varname
            val1 = str(attributes1.value)
            var1_str = f'{var1} = '
            len_var1_str = len(var1_str)
            len_val1 = 20 - len_var1_str
            val1_str = val1.rjust(len_val1, ' ')
            output1_str = f'{var1_str}{val1_str}'

            #idx2 = row2[0]
            attributes2 = row2[1]
            var2 = attributes2.varname
            val2 = str(attributes2.value)
            var2_str = f'{var2} = '
            len_var2_str = len(var2_str)
            len_val2 = 20 - len_var2_str
            val2_str = val2.rjust(len_val2, ' ')
            output2_str = f'{var2_str}{val2_str}'

            #idx3 = row3[0]
            attributes3 = row3[1]
            var3 = attributes3.varname
            val3 = str(attributes3.value)
            var3_str = f'{var3} = '
            len_var3_str = len(var3_str)
            len_val3 = 20 - len_var3_str
            val3_str = val3.rjust(len_val3, ' ')
            output3_str = f'{var3_str}{val3_str}'

            row_output = f'{output1_str}   {output2_str}   {output3_str}'
            
            csvfile.write(row_output)
            csvfile.write('\n')

    # update usrinpt with modified variable info
    # use backup usrinpt to copy over lines that wont change
    with open(reference_filepath) as refcsv:
        with open('modified-vars') as modcsv:
            with open(outfile, 'w') as outcsv:
                refreader = csv.reader(refcsv, delimiter='\t')
                modreader = csv.reader(modcsv)
                outwriter = csv.writer(outcsv)
                mod_line = 0
                modlines = [line for line in modreader]
                for i, row in enumerate(refreader):
                    if (i>1) and (i<18):
                        # copy over lines with updated variable values
                        outcsv.write(f'{modlines[mod_line][0]}\n')
                        mod_line += 1
                    else:
                        # copy over lines that dont change 
                        outcsv.write(f'{row[0]}\n')
    
    return

def varTypeDict():
    inputs_formatted = createInputsDataset()
    typedict = {}
    for row in inputs_formatted.iterrows():
        attribs = row[1]
        value = attribs.value

        if value == 'T' or value == 'F':
            typedict[attribs.varname] = 'bool'
        else:
            try: 
                inferred_type = pd.to_numeric(value).dtype
                if inferred_type == float:
                    typedict[attribs.varname] = 'float'
                if inferred_type == int:
                    typedict[attribs.varname] = 'int'
            except ValueError:
                typedict[attribs.varname] = 'str'
    return typedict

def formatVarType(var_name, var_value):
    typedict = {'inpfil': 'str',
                'lat': 'float',
                'iyear': 'int',
                'zstart': 'float',
                'wstart': 'float',
                'tstart': 'float',
                'lzenit': 'bool',
                'o3col': 'float',
                'taucld': 'float',
                'tauaer': 'float',
                'dirsun': 'float',
                'zout': 'float',
                'lirrad': 'bool',
                'lrates': 'bool',
                'ljvals': 'bool',
                'iwfix': 'int',
                'outfil': 'str',
                'lon': 'float',
                'imonth': 'int',
                'zstop': 'float',
                'wstop': 'float',
                'tstop': 'float',
                'alsurf': 'float',
                'so2col': 'float',
                'zbase': 'float',
                'ssaaer': 'float',
                'difdn': 'float',
                'zaird': 'float', # NOTE this is actually scientific expon
                'laflux': 'bool',
                'isfix': 'int',
                'ijfix': 'int',
                'itfix': 'int',
                'nstr': 'int',
                'tmzone': 'float',
                'iday': 'int',
                'nz': 'int',
                'nwint': 'int',
                'nt': 'int',
                'psurf': 'float',
                'no2col': 'float',
                'ztop': 'float',
                'alpha': 'float',
                'difup': 'float',
                'ztemp': 'float',
                'lmmech': 'bool',
                'nms': 'int',
                'nmj': 'int',
                'izfix': 'int'}
    
    var_type = typedict[var_name]

    if var_type == 'int':
        var_value = str(int(var_value))
    if var_type == 'float':
        var_value = f'{float(var_value):8.3f}'
    if var_type == 'bool':
        var_value = str(var_value)[0] # T or F

    return var_value

if __name__ == '__main__':

    # Test case
    modified_variables = {'tmzone': 2,
                          'nt': 10
                          }

    modifyInput(modified_variables)