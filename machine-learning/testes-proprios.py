# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:53:50 2023

@author: meire
"""

import pandas as pd;
import numpy as np;
import seaborn as sbn;
from sklearn.preprocessing import LabelEncoder, OneHotEncoder;
from sklearn.compose import ColumnTransformer;
import pickle;
from sklearn.model_selection import train_test_split;
from sklearn.naive_bayes import GaussianNB;
from sklearn.metrics import accuracy_score;                   


data = pd.read_csv("../panic_disorder_dataset_training.csv");
data2 = pd.read_csv("../panic_disorder_dataset_testing.csv");


print(np.unique(data['Age'], return_counts=True));

#sbn.barplot(y = "Substance_Use", x = "Age", data = data);

print(data["Symptoms"]);
labelEncoder = LabelEncoder();

data["Symptoms"] = labelEncoder.fit_transform(data["Symptoms"]);


print(data["Symptoms"]);
print("aqui", data.iloc[0, 1:16]);

xData = data.iloc[:, 1:16].values;
yData = data2.iloc[:, 16].values;

print("xData " , xData[0]);

labelEncoder = LabelEncoder();

xData[:, 1] = labelEncoder.fit_transform(xData[:, 1]);
xData[:, 2] = labelEncoder.fit_transform(xData[:, 2]);
xData[:, 3] = labelEncoder.fit_transform(xData[:, 3]);
xData[:, 4] = labelEncoder.fit_transform(xData[:, 4]);
xData[:, 6] = labelEncoder.fit_transform(xData[:, 6]);
xData[:, 7] = labelEncoder.fit_transform(xData[:, 7]);
xData[:, 8] = labelEncoder.fit_transform(xData[:, 8]);
xData[:, 9] = labelEncoder.fit_transform(xData[:, 9]);
xData[:, 10] = labelEncoder.fit_transform(xData[:, 10]);
xData[:, 11] = labelEncoder.fit_transform(xData[:, 11]);
xData[:, 12] = labelEncoder.fit_transform(xData[:, 12]);
xData[:, 13] = labelEncoder.fit_transform(xData[:, 13]);
xData[:, 14] = labelEncoder.fit_transform(xData[:, 14]);

print("xData depois " , xData[0]);


hotEncoder = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])], remainder='passthrough');



hotEncodedData = hotEncoder.fit_transform(xData).toarray();

print("encoded 1 " , hotEncodedData.shape);
print("encoded 1 0" , hotEncodedData[0][23]);

print("encoded 2 " , yData.shape);


xTraining, xTest, yTraining, yTest = train_test_split(xData, yData, test_size= 0.25, random_state=0);
with open("dadosProcessadosDistubios.pkl", mode="wb") as f:
    pickle.dump([xTraining, xTest, yTraining, yTest], f)







