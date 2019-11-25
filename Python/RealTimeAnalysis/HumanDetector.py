# Import needed libraries

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import numpy as np
import re
import pandas as pd

# DataFrame to contain the sensor data
data = pd.DataFrame()

# Filepath of the data file
filepath = 'modelData.txt'


with open(filepath) as fp:
    line = fp.readline()
    counter = 0

    while line:

        # Regex pattern to recognize needed data
        match = re.findall(pattern=('(\d+.\d+)'), string=line)
        if len(match) == 16:
            dataSeries = pd.Series(match, dtype='float', name=counter)
            counter += 1
            data = data.append(dataSeries, sort=None)

        line = fp.readline()


# Let's filter out all the row's containing erroneous data.
#
# 1. Set values over 40 and below 10 to NA
# 2. Drop lines with NA values

data = data[data < 40]
data = data[data > 10]
data = data.dropna()

# Create classification data
classification = pd.Series()

# Boolean mask for data >= 27
data1mask = data.iloc[::] >= 25

# Iterate through Boolean mask and if row contains value True, add 1 to classification. Else add 0.
for i in range(len(data1mask)):
    humanDetected = False
    for j in range(16):
        maskValue = data1mask.iloc[i, j]
        if (maskValue == True):
            humanDetected = True

    if (humanDetected == True):
        classification = classification.append(
            pd.Series([1]), ignore_index=True)
    else:
        classification = classification.append(
            pd.Series([0]), ignore_index=True)


X = np.array(data)
y = np.array(classification)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=12)


# Fit the Gaussian Naive Bayes model
clf = GaussianNB()
clf.fit(X_train, y_train)

import time
import os
while True:
    with open("data.txt") as fp:
        lines = fp.readlines()
        line = lines[-1]
        match = re.findall(pattern=('(\d+.\d+)'), string=line)
        if len(match) != 16:
            line = lines[-2]
            match = re.findall(pattern=('(\d+.\d+)'), string=line)
        array = np.array(match, dtype='float')
        array = array.reshape(1, -1)
        prediction = clf.predict(array)
    
    f = open("detection.txt", "a")
    f.write(str(prediction))
    f.write("\n")
    f.close()
    print(str(prediction))
    time.sleep(0.4)
    os.system("sed -i '1d' detection.txt")



    # f = open("data.txt", "a")
    # prediction = 

    # f.write(data)
    # f.write("\n")
    # f.close()

    # os.system("sed -i '1d' modelData.txt")

    # print(ser_bytes)
