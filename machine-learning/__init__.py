import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

baseCredit = pd.read_csv("../../../Documents/estudos/credit_risk_dataset.csv");

# print(baseCredit["loan_amnt"].describe());

print(np.unique(baseCredit["loan_status"], return_counts=True));

# sns.countplot(x = "person_age", data = baseCredit);
graph = px.scatter_matrix(baseCredit, dimensions=['person_age', 'loan_amnt']);
graph.show();

