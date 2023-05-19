from builtins import int

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

baseCredit = pd.read_csv("../../credit_risk_dataset.csv");

# print(baseCredit["loan_amnt"].describe());

print(np.unique(baseCredit["loan_status"], return_counts=True));

#sns.countplot(x = "person_age", data = baseCredit);
# print(baseCredit.loc[baseCredit["person_age"] <= 0]);
# deletar coluna (0 é linha 1 é coluna)
baseCredit2 = baseCredit.drop('person_age', axis=1);

# deletar registros com base em condicao (valores incosistentes)
# o .index passa o indice da linha, nesse caso aqui filtramos todos que tem person age < 0 e com o .index retornamos sua posição no csv
baseCredit3 = baseCredit.drop(baseCredit[baseCredit["person_age"] < 0].index);

# preencher valores com média / acessar media
# para acessar a media de um csv usamos a função mean()
print(baseCredit.mean());
print(baseCredit['person_age'].mean());
print(baseCredit['person_age'][baseCredit['person_age'] > 0].mean());
# px.scatter_matrix(baseCredit, dimensions=['person_age', 'loan_amnt']).show();

# visulizar do inicio do csv até um valor especifico do csv (head)
# print(baseCredit.head(27))

print("dados do index 3");
print(baseCredit.loc[3]);


#retornar todos os registros e mostrar que o valor está vazio (faltando) quando o mesmo for "null"
#sum é uma função para somar os valores retornados como true
print(baseCredit.isnull().sum());

#mostrando média de de "loan_int_rate"
print(baseCredit["loan_int_rate"].mean());

# print(baseCredit[baseCredit["loan_int_rate"].isnull()]);
# print(baseCredit.loc[39]);
baseCredit.loc[pd.isnull(baseCredit['loan_int_rate']), "loan_int_rate"] = baseCredit["loan_int_rate"].mean();
# desse jeito tbm funciona
# baseCredit.loc[baseCredit['loan_int_rate'].isnull()] = baseCredit["loan_int_rate"].mean();
print(baseCredit.isnull().sum());
# essa funcao fillna tambem preenche automaticamente valores nulos
baseCredit['loan_int_rate'].fillna(baseCredit['loan_int_rate'].mean(), inplace= True);