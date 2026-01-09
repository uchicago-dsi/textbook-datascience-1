## pd.Categorical(values).codes

Converts categorical data into numeric codes. Each unique category gets assigned an integer starting from 0. This is useful when you need to convert string labels into numbers for machine learning models.
```python
import pandas as pd

colors = pd.Categorical(['red', 'blue', 'red', 'green', 'blue'])
print(colors.codes)
# Output: array([2, 0, 2, 1, 0])
# red=2, blue=0, green=1
```

## DecisionTreeClassifier 

A scikit-learn class that creates a decision tree for classification tasks. 
```python
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state=2)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
```

## plot_tree

A scikit-learn function that visualizes a trained decision tree. 
```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plot_tree(clf, feature_names=['feature1', 'feature2'], 
          class_names=['classA', 'classB'], filled=True)
plt.show()
```

## BaggingClassifier

A scikit-learn class that implements bagging for classification. 
```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bag_clf = BaggingClassifier(DecisionTreeClassifier(), 
                             n_estimators=100, random_state=42)
bag_clf.fit(X_train, y_train)
predictions = bag_clf.predict(X_test)
```

## model.feature_importances_

An attribute of trained tree-based models that returns an array showing the importance of each feature. Higher values indicate features that are more useful for making predictions. The values sum to 1.
```python
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

importances = clf.feature_importances_
print(importances)
# Output: array([0.05, 0.32, 0.63]) 
# Feature 2 is most important (0.63)
```

## model.estimators_

An attribute of ensemble models that returns a list of all the individual weak learner models (estimators) that were trained. 
```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=10)
rf.fit(X_train, y_train)

# Access the third tree in the forest
third_tree = rf.estimators_[2]
print(len(rf.estimators_))  # Output: 10
```

## RandomForestClassifier

A scikit-learn class that implements the Random Forest algorithm for classification. 
```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', 
                            random_state=42)
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)
```

## AdaBoostClassifier

A scikit-learn class that implements the AdaBoost algorithm for classification. 
```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

ada = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), 
                         n_estimators=50, random_state=42)
ada.fit(X_train, y_train)
predictions = ada.predict(X_test)
```

## GridSearchCV

A scikit-learn class that performs exhaustive search over specified parameter values for a model. It uses cross-validation to evaluate each combination of parameters and finds the best one.
```python
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

param_grid = {
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(grid_search.best_params_)  # {'max_depth': 5, 'min_samples_split': 2}
best_model = grid_search.best_estimator_
```