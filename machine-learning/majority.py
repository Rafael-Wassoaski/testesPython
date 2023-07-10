import Orange;
from collections import Counter;

basecredit = Orange.data.Table("../../credit_risk_dataset.csv");
print(basecredit.domain);
majority = Orange.classification.MajorityLearner();

previsoes = Orange.evaluation.testing.TestOnTestData(basecredit, basecredit, [majority]);
#print(previsoes);
print(Orange.evaluation.CA(previsoes));
Counter(str(registro.get_class() for registro in basecredit));