import pickle as pkl;
from sklearn import tree;
from sklearn.tree import DecisionTreeClassifier;
import matplotlib.pyplot as plt;
from sklearn.metrics import accuracy_score, classification_report;
from yellowbrick.classifier import ConfusionMatrix;

with open("dadosProcessadosDistubios.pkl", "rb") as f:
    xTraining, xTest, yTraining, yTest = pkl.load(f);
    
print(xTraining[0][0]);

decisionTree = DecisionTreeClassifier(criterion="entropy");
decisionTree.fit(xTraining, yTraining);

previsores = ["Participant ID",	"Age",	"Gender",	"Family History",	"Personal History",	
              "Current Stressors",	"Symptoms",	"Severity",	"Impact on Life",	"Demographics",
             "Medical History",	"Psychiatric History",	"Substance_Use",	"Coping Mechanisms",
              "Medical Support"]
print(decisionTree.feature_importances_);
print(decisionTree.classes_);
#fig, axes = plt.subplots(nrows=1, ncols=1, figsize = (150, 150));
#arvore = tree.plot_tree(decisionTree, feature_names=previsores, class_names=['Doido', 'Normal'], filled=True);

print(xTraining[0]);

previsoes = decisionTree.predict(xTest);
print(accuracy_score(yTest, previsoes));
print(classification_report(yTest, previsoes));

cm = ConfusionMatrix(decisionTree);
cm.fit(xTraining, yTraining);
cm.score(xTest, yTest);