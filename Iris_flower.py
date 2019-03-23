import numpy as np

#importing data from the csv file
data = np.genfromtxt("iris_data.csv", delimiter=',')

# getting first column data (sepal length)
firstcol = data[:,0]
# getting first column data (sepal width)
secondcol = data[:,1]
# getting third column data (petal length)
thirdcol = data[:,2]
# getting fourth column data (petal width)
fourthcol = data[:,3]

# calculating average value of the first column
avgsepall = np.mean(firstcol)
avgsepalw = np.mean(secondcol)
avgpetall = np.mean(thirdcol)
avgpetalw = np.mean(fourthcol)

# printing each column as array
print(firstcol)
print(secondcol)
print(thirdcol)
print(fourthcol)

# printing average of each column
print(avgsepall)
print(avgsepalw)
print(avgpetall)
print(avgpetalw)