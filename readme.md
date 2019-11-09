1 Introduction

    This project's goals are to connect Omron D6T-44L-06 sensor to Arduino and to train 
    a classification algorithm on Arduino to detect human and possibly specific animals.

    Omron D6T datasheet https://omronfs.omron.com/en_US/ecb/products/pdf/en-d6t.pdf


2 Record data of the sensor output

    Record data with and without human presence
    Sample recording https://github.com/labazor/HumanPresenceDetector/blob/master/Python/SerialLogger/data/data.txt

3 Visualize raw data

4 Preprocess data

4.1 Filtering data limit low/high

4.2 Data normalization

5 Select and classify the training data

6 Create classification model

6.1 Split to train & test

6.2 Naive Bayes Gaussian classification

7 Testing model accuracy

8 C++ software for Arduino
