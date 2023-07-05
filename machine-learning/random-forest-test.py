from sklearn.ensemble import RandomForestClassifier;
from sklearn.metrics import accuracy_score, classification_report;
#from yellowbrick.classfies import ConfusionMatrix;
import pickle;

with open("./credit.pkl", "rb") as f:
    xTreino, yTreino, xTeste, yTeste = pickle.load(f);
    
print(xTreino.shape);

#n_estimators = numero de arvores e decissao que serao criadas
randomForest = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0);
randomForest.fit(xTreino, yTreino);


previsoes = randomForest.predict(xTeste);

print(accuracy_score(yTeste, previsoes));
print(classification_report(yTeste, previsoes));
