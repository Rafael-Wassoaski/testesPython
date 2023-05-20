from builtins import int
from sklearn.preprocessing import StandardScaler

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