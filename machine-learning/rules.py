import Orange;
import pickle as pkl;



baseCredit = Orange.data.Table("../../credit_risk_dataset.csv");
print(baseCredit);
print(baseCredit.domain);


cn2 = Orange.classification.rules.CN2Learner();
baseDivided = Orange.evaluation.testing.sample(baseCredit, n=0.25);
print(baseDivided);

rules = cn2(baseDivided[1]);    



for rule in rules.rule_list:
    print(rule);

previsoes = rules([["boa", "alta", "ruim"], ["ruim", "desconhecida", "baixa"]]);    

print(previsoes);
print(baseCredit.domain.class_var);
print(baseCredit.domain.class_var.values);

for i in previsoes:
    print(i)
    print(baseCredit.domain.class_var.values[i]);
    
    
#Calculando a acuracia    
previsoes2 = Orange.evaluation.testing.TestOnTestData(baseDivided[1], baseDivided[0], [lambda testdata: rules]);
print(previsoes2);

accuracy = Orange.evaluation.CA(previsoes2);
print(accuracy);

