#--python is very sensitive to whitespace
#--therefore it is important to be consistent with spaces

#--Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

#--Data types for each column  (only if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill':float}

#--initialize my data variable
data = {}#{'date':[], 'time':[], 'tempout':[]} # --as dictionary

for column in columns:
    data[column] = []

#--Read the data file
filename='../data/wxobs20170821.txt'

with open(filename, 'r') as datafile:
    
    #-- read the first three lines (header)
    for _ in range(3):
        headerline = datafile.readline()
        datafile.readline()
        #print(headerline)
    #-- Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

#-- Compute the wind chill temperature
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v**16
    wci = a + (b * t) - (c * v16) + (d * t * v16)

    return wci


#--Running the function to compute wci
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp,windspeed))




#--DEBUG
for wc_data, wc_comp in zip(data['windchill'], windchill):
    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}') #--format the printout to 5 decimal points

#for i, j in zip([1, 2], [3, 4, 5]):
#    print(i,j)



exit()


