#https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set(color_codes=True)

# reads the data from the file
df = pd.read_csv("iris_data.csv")


# from the dataset getting the Iris species values
species = df["Species"].unique()
nr_species = len(species)

# getting the names of columns that have numeric values
list_of_col = df.columns
col_name = []

for column in list_of_col:
    if df[column].dtype == float:
        col_name.append(column)

# calculating average value of each numeric column
avgsepall = np.mean(df["Sepal length"])
avgsepalw = np.mean(df["Sepal width"])
avgpetall = np.mean(df["Petal length"])
avgpetalw = np.mean(df["Petal Width"])


# printing average value of each numeric column rounded by 2 digits after comma
print("Average sepal length:", round(avgsepall, 2))
print("Average sepal width:", round(avgsepalw, 2))
print("Average petal length:", round(avgpetall, 2))
print("Average petal width:", round(avgpetalw, 2))

# Adopted from https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
fig, axs = plt.subplots(len(col_name), len(species), figsize=(20,20))

# creates a boxplot set for every species providing data on petal length&width and sepal length&width
for x in range(len(col_name)):
    for y in range(len(species)):  
        #print(col_name[x]," : ",species[y])
        axs[x,y].boxplot(df[col_name[x]][df['Species'] == species[y]])
        axs[x,y].set_title(col_name[x]+" - "+species[y], color="b")

# saves the graph as png file
plt.savefig("Boxplot.png")


# creates a violin plot per each species using following parametres: petal length and petal width
plt.figure(figsize=(15,15)) # size of the window
sns.violinplot( x="Petal Width", y="Petal length", hue="Species", data=df)

# saves the graph as png file
plt.savefig("Violinplot_petal.png")


# creates a violin plot per each species using following parametres: sepal length and sepal width
plt.figure(figsize=(15,15)) #size of the window
sns.violinplot( x="Sepal width", y="Sepal length", hue="Species", data=df)

# saves the graph as png file
plt.savefig("Violinplot_sepal.png")


# creates a scatterplot for all species using following parametres: sepal length&width vs petal lenth&width
sns.pairplot(df,hue="Species")

# saves the graph as png file
plt.savefig("Scatterplot.png")


#  show results in the graphs
plt.show()
