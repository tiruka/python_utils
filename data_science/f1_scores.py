from sklearn.metrics import f1_score

# F1 score is a measure of a test's accuray for binary classification problems.
# mean-f1, macro-f1 and micro-f1 are extended for multi label classification problems.
'''
y_val(multi label data)
a   b   c   d
0	1	0	0
1	0	0	0
0	0	0	0
1	1	0	0
0	1	0	0	
'''

# In mean-f1, caluculate mean of F1-score by record (row)
mean_f1 = np.mean([f1_score(y_val[i, :], preds[i, :]) for i in range(len(y_val))])

# In macro_f1, caluculate mean of F1-score by class (column)
n_class = len(y_val[0, :])
macro_f1 = np.mean([f1_score(y_val[:, c], preds[:, c]) for c in range(n_class)])

# In micro-f1, caluculate mean of F1-score by pair of record and class
micro_f1 = f1_score(y_val.reshape(-1), preds.reshape(-1))
print(mean_f1, macro_f1, micro_f1)

# sklearn version
sk_mean_f1 = f1_score(y_val, preds, average='samples')
sk_macro_f1 = f1_score(y_val, preds, average='macro')
sk_micro_f1 = f1_score(y_val, preds, average='micro')
print(sk_mean_f1, sk_macro_f1, sk_micro_f1)