import pandas as pd
Data = pd.read_csv('Market_Basket.csv', header = None)
print(Data)
print(Data.ndim)
transacts = []
for i in range(0, 7501):
    for j in range(0, 20):
        transacts.append(str(Data.values[i,j]))
from apyori import apriori
rule = apriori(transactions = transacts, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)
output = list(rule)
def inspect(output):
    lhs         = [tuple(result[2][0][0])[0] for result in output]
    rhs         = [tuple(result[2][0][1])[0] for result in output]
    support    = [result[1] for result in output]
    confidence = [result[2][0][2] for result in output]
    lift       = [result[2][0][3] for result in output]
    return list(zip(lhs, rhs, support, confidence, lift))
Final_Out_DF = pd.DataFrame(inspect(output), columns = ['Left_Hand_Side', 'Right_Hand_Side', 'Support', 'Confidence', 'Lift'])
print(Final_Out_DF)
print(Final_Out_DF.nlargest(n = 10, columns = 'Lift'))