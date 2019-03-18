with open("Iris_flower_data.csv", "r") as f:
    #print(f.read())
    print(f.head()) #to check the first 10 rows of the data set
    print(f.tail()) #to check out last 10 row of the data set)


# closing text file
f.close()

