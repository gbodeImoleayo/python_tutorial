#--python is very sensitive to whitespace
#--therefore it is important to be consistent with spaces

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
