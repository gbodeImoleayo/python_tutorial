#--python is very sensitive to whitespace
#--therefore it is important to be consistent with spaces

#--Column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2}

#--Data types for each column  (only if non-string)
types = {'tempout': float}

#--initialize my data variable
data = {}#{'date':[], 'time':[], 'tempout':[]} # --as dictionary

for column in columns:
    data[column] = []

#--Read the data file
filename='../data/wxobs20170821.txt'

with open(filename, 'r') as datafile:
    
    #-- read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    #-- Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

exit()

#--initialize my data variable
#data = [] # --as list
data = {'date':[], 'time':[], 'tempout':[]} # --as dictionary


#--Read the data file
filename='../data/wxobs20170821.txt'

with open(filename, 'r') as datafile:
    
    #-- read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    #-- Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        data['tempout'].append(float(split_line[2]))

exit()

#--initialize my data variable
#data = [] # --as list
data = {'date':[], 'time':[], 'tempout':[]} # --as dictionary


#--Read the data file
filename='../data/wxobs20170821.txt'

with open(filename, 'r') as datafile:
    
    #-- read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    #-- Read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)

exit()


#--initialize my data variable
data = []

#--Read the data file
filename='../data/wxobs20170821.txt'

with open(filename, 'r') as datafile:
    
    #-- read the first three lines (header)
    for _ in range(3):
        datafile.readline()

    #-- Read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)

#DEBUG
for datum in data:
    print(datum)


exit()

#--initialize my data variable
data = []

#--Read the data file
filename='../data/wxobs20170821.txt'

with open(filename, 'r') as datafile:
    data = datafile.read()


exit()
#--DEBUG
print(type(data))


exit()
#--open the file
datafile=open(filename, 'r')

data = datafile.read()

#--DEBUG
print(data)
print('data')

#--close the file
datafile.close() 
exit()
#--print out the first few lines of the data
print(datafile.readline()) #--read first line 
print(datafile.readline()) #--read second line and so on
print(datafile.readline()) 
print(datafile.readline())

#--close the file
datafile.close() 
