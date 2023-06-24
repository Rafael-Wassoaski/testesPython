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


data = pd.read_csv("../panic_disorder_dataset_testing.csv");

print(np.unique(data['Age'], return_counts=True));

#sbn.barplot(y = "Substance_Use", x = "Age", data = data);

print(data["Symptoms"]);
labelEncoder = LabelEncoder();

data["Symptoms"] = labelEncoder.fit_transform(data["Symptoms"]);


print(data["Symptoms"]);
print("aqui", data.iloc[0, 1:16]);

xData = data.iloc[:, 1:16].values;
yData = data.iloc[:, 16].values;

print("xData " , xData[0]);


hotEncoder = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])], remainder='passthrough');


hotEncodedData = hotEncoder.fit_transform(xData).toarray();

print("encoded 1 " , hotEncodedData.shape);
print("encoded 2 " , yData.shape);


xTraining, xTest, yTraining, yTest = train_test_split(hotEncodedData, yData, test_size= 0.25, random_state=0);

with open('dadosProcessadosDistubios.pkl', 'wb') as f:
    pickle.dump([xTraining, xTest, yTraining, yTest], f);
    
    
    
print("x trainig" , hotEncodedData[len(yData) - 1]);
print("y trainig " , yData[len(yData) - 1]);


naiveBayes = GaussianNB();

naiveBayes.fit(xTraining, yTraining);

previsao = naiveBayes.predict([hotEncodedData[len(yData) - 1]]);
print("previsao " , previsao );
previsao = naiveBayes.predict(xTest);
print("metricas " , accuracy_score(yTest, previsao));







