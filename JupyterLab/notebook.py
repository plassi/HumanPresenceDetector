# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'JupyterLab'))
	print(os.getcwd())
except:
	pass
# %% [markdown]
# <h1>HumanPresenceDetector data analysis</h1>
# 
# %% [markdown]
# <h3>1 Load data from file</h3>

# %%
# Import needed libraries

import re
import pandas as pd

# DataFrame to contain the sensor data
data = pd.DataFrame()

# Filepath of the data file
filepath = 'data.txt'


with open(filepath) as fp:
    line = fp.readline()
    counter = 0

    while line:
        
        # Regex pattern to recognize needed data
        match = re.findall(pattern=('(\d+.\d+)'), string=line)
        if len(match) == 16:
            dataSeries = pd.Series(match ,dtype='float', name=counter)
            counter += 1
            data = data.append(dataSeries, sort=None)

        line = fp.readline()
print(data.describe())

# %% [markdown]
# <h3>2 Filter data</h3>
# 
# %% [markdown]
# From data descriptions we can see that measurements include some erroneous data.
# 
# Let's filter out all the row's containing erroneous data.
# 
# 1. Set values over 40 and below 10 to NA
# 2. Drop lines with NA values

# %%
data = data[data < 40]
data = data[data > 10]
data = data.dropna()

# Drop first 10 rows
# data = data.iloc[10:]

# print(data.describe())


# %%
from matplotlib import pyplot as plt

plt.figure(figsize=(10, 4), dpi= 80, facecolor='w', edgecolor='k')
plt.plot(data)
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (celsius)")
plt.show()

# %% [markdown]
# <h3>3 Classification data</h3>
# %% [markdown]
# From the chart above we can see that human is present when at least one of the values is above 27 celsius.
# We can use this information to classify the data.
# 
# Add class column to data dataframe and use this classification:
# 
# 0 No human detected
# 1 Human is present
# 
# 

# %%
# Create classification data
classification = pd.Series()

# Boolean mask for data >= 27
data1mask = data.iloc[::] >= 27

# Iterate through Boolean mask and if row contains value True, add 1 to classification. Else add 0. 
for i in range(len(data1mask)):
    humanDetected = False
    for j in range(16):
        maskValue = data1mask.iloc[i, j]
        if (maskValue == True):
            humanDetected = True

    if (humanDetected == True):
        classification = classification.append(pd.Series([1]), ignore_index=True)
    else:       
        classification = classification.append(pd.Series([0]), ignore_index=True)


# %%
# Visualization of the training & classification data

plt.figure(figsize=(12, 8), dpi= 80, facecolor='w', edgecolor='k')


plt.subplot(2, 1, 1)
plt.plot(data)
plt.title('Training & Classification data')
plt.xlabel('time (s)')
plt.ylabel('Temperature (degrees Celsius)')

plt.subplot(2, 1, 2)
plt.plot(classification)
plt.xticks([])
plt.ylabel('Classification')

plt.show()

# %% [markdown]
# <h3>4 Machine Learning model</h3>
# 

# %%
# Create and split the data for classifier

import numpy as np
from sklearn.model_selection import train_test_split

X = np.array(data)
y = np.array(classification)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=12)


# Fit the Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train )

# Print models accuracy score
print("Accuracy score:")
print(clf.score(X_test, y_test))


# %%

# import emlearn

# cmodel = emlearn.convert(clf)
# cmodel.save(file='testi.h')


