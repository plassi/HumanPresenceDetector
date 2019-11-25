1 Introduction

    This project's goals are to connect Omron D6T-44L-06 sensor to Arduino and to train 
    a classification algorithm on Arduino. Classificator classifies filtered sensor data 
    to detect human and smaller mammal in the field of view of the thermal sensor.

    Omron D6T datasheet https://omronfs.omron.com/en_US/ecb/products/pdf/en-d6t.pdf
    
2 Arduino schematics & sketches

    Arduino/Schematics/                     
    Arduino/Sketches/                      


2 Data record

    Python/SerialLogger/SerialLogger.py     Python3 source for logging serial data 
                                            of Arduino wirh Omron D6T-44l-06 sensor.
                                            
    raw_data/                               Recorded samples

3 Data analysis

    JupyterLab/notebook.ipynb               Data analysis results as a JupyterLab Notebook.

4 C++ software for Arduino
    emlearn
