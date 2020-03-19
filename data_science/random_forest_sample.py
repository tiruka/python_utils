from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

'''
Numpy array of Y and X are just sample for understanding.
Replace it with data you want to search.
Random Forest is an ensemble learning method for classification,
regression and other tasks that operate by constructing a multitude of decision trees.
Less tuning parameters and robust model even with multiple input variables.
You can get importace of each input variables.
Random Forest can be applied for regression, binary classificaiton, multi classificaiton,
and multi label classificaiton as well.
'''

# Sample Data
Y = np.array([
        [0],
        [0],
        [1],
        [1],
        [0],
        [1],
])
X = np.array([
  [13, 4, 2],
   [2, 2, 4],
   [7, 17, 1],
   [5, 2, 0],
   [4, 1, 12],
   [2, 3, 3]])

# Learning
rfc = RandomForestClassifier(bootstrap=True,
                             n_estimators=10,
                             max_depth=10,
                             max_features='sqrt',
                             random_state=1)
rfc.fit(X, Y)

# Test and Prediction
test_x = np.array([
    [13, 4, 2],
    [2, 2, 4],
    [2, 3, 0]
])

test_y = np.array([
    [0],
    [1],
    [1],
])
preds = rfc.predict_proba(test_x)
fpr, tpr, thr = roc_curve(test_y, preds[:, 1])
auc = roc_auc_score(test_y, preds[:, 1])

# Visualization
plt.plot(fpr, tpr)
plt.plot(fpr, fpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

# Showing each importance of input variables to predict.
# Whether you adapt this model, it is a good indicator to search data more deeply.
# fi = list(zip(X.columns, rfc.feature_importances_))
# fi.sort(key=lambda x: -x[1])
# pd.DataFrame(fi, columns=['Features', 'Importance'])