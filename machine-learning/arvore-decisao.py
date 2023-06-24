from sklearn.tree import DecisionTreeClassifier;
from sklearn import tree;
import pandas as pd;
import matplotlib.pyplot as plt;
import pickle;


with open("risco_processado.pkl","rb") as f:
    xRisco, yRisco = pickle.load(f);
    
print(xRisco);
print(yRisco);

arvoreDecission = DecisionTreeClassifier(criterion="entropy");
arvoreDecission.fit(xRisco, yRisco);

print(arvoreDecission.feature_importances_);

#isso eh uma lista
previsores = ['nome1', 'nome2'];
fig, axes = plt.subplots(nrows=1, ncols=1, figsize = (20, 20));
#arvore = tree.plot_tree(arvoreDecission, feature_names=previsores, class_names=str(arvoreDecission.classes_), filled=True);
arvore = tree.plot_tree(arvoreDecission, filled=True);

print(arvore);

previsoes = arvoreDecission.predict([[0,0,1,2], [2,0,0,0]]);
print(previsoes);

fig.savefig("test.png");
