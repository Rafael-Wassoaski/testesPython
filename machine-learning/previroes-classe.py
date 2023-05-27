from builtins import int
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

import pickle
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

baseCredit = pd.read_csv("../../credit_risk_dataset.csv");  
# : (dois pontos) indica todas as linhas    
xCredit = baseCredit.iloc[:, [0,1,6]].values;

yCredit = baseCredit.iloc[:, 8].values;

#menor valor de income
print(xCredit[:, 1].min());

#maior valor income
print(xCredit[:, 1].max());

#menor valor idade
print(xCredit[:, 0].min());

#maior valor idade
print(xCredit[:, 0].max());

#aplicando padronização nos dados de xCredit
scalerCredit = StandardScaler();
print(xCredit);
xCredit = scalerCredit.fit_transform(xCredit)
print(xCredit);

adultData = pd.read_csv("../../adult.csv");
print(adultData.describe());
print(np.unique(adultData["income"], return_counts=True));
#sns.countplot(x=adultData["income"]);
#plt.hist(x= adultData["age"]);
#plt.hist(x=adultData["education-num"])
#plt.hist(x=adultData["hours-per-week"]);

graph = px.treemap(adultData, path=['workclass']);
graph.update_traces(root_color="lightgrey")
graph.update_layout(margin = dict(t=50, l=25, r=25, b=25))
graph.show();   


graph = px.parallel_categories(adultData, dimensions=['occupation', 'relationship']);

graph.show();

xAdult = adultData.iloc[:, 0:14].values;
yAdult = adultData.iloc[:, 14].values;

print(xAdult);
print(yAdult); 

labelEncoderTest = LabelEncoder()
teste = labelEncoderTest.fit_transform(xAdult[:, 1  ]);
print(teste);

labelEncoderWorkClass = LabelEncoder();
labelEncoderEducation = LabelEncoder();
labelEncoderMarital = LabelEncoder();
labelEncoderOccupation = LabelEncoder();

xAdult[:, 1] = labelEncoderWorkClass.fit_transform(xAdult[:, 1]);
xAdult[:, 3] = labelEncoderEducation.fit_transform(xAdult[:, 3]);
xAdult[:, 5] = labelEncoderMarital.fit_transform(xAdult[:, 5]);
xAdult[:, 6] = labelEncoderOccupation.fit_transform(xAdult[:, 6]);
xAdult[:, 7] = labelEncoderOccupation.fit_transform(xAdult[:, 7]);
xAdult[:, 8] = labelEncoderOccupation.fit_transform(xAdult[:, 8]);
xAdult[:, 9] = labelEncoderOccupation.fit_transform(xAdult[:, 9]);
xAdult[:, 13] = labelEncoderOccupation.fit_transform(xAdult[:, 13]);

print(xAdult[0]);

hotEncoder = ColumnTransformer(transformers=[('OneHot',
                               OneHotEncoder(),
                               [1,3,5,6,7,8,9,13])],
                               remainder='passthrough');
hotEncodedData = hotEncoder.fit_transform(xAdult).toarray();
print(hotEncodedData[0]);
hotEncodedData = scalerCredit.fit_transform(hotEncodedData);
print(hotEncodedData[0]);

xAdultTraining, xAdultTest, yAdultTraining, yAdultTest = train_test_split(xAdult, yAdult, test_size= 0.25, random_state=0);
print(xAdultTraining.shape);
print(yAdultTraining.shape);
print(xAdultTest.shape)
print(yAdultTest.shape);  

with open("credit.pkl", mode="wb") as f:
    pickle.dump([xAdultTraining, yAdultTraining, xAdultTest, yAdultTraining], f)



