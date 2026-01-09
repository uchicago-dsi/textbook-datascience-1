## Tree-based Methods
It is a broad umbrella term which includes decision trees, models built using many decision trees or decision tree variations. 

## Decision Tree
A single flow chart like tree structure that makes predictions by asking a series of questions about the features.

## Ensemble Methods
The technique of combining predictions from many simple models to give the final prediction.

## Root Node
The topmost node in a decision tree. 

## Internal Nodes
The nodes that are not root nodes or leaves in a decision tree. They represent the splits made of the feature space.

## Branches
The connections between nodes of a decision tree.

## Leaf Nodes or Leaves
The terminal nodes of a decision tree that provide the final prediction. 

## Recursive Binary Splitting
A technique to split the feature space of the data successively moving down the tree. At each step the split is binary i.e. into two parts and the split is chosen such that it gives the best results at that particular step without looking ahead (using RSS for regression or Gini impurity for classification). 

## Gini impurity
It measures how mixed the classes are in a node.
$$\text{Gini} = 1 - \sum_{i=1}^{K} p_i^2$$
where $K$ is the number of classes and $p_i$ is the proportion of training observations in the node that belong to class $i$.

## Residual Sum of Squares 
It measures the total squared deviation of the responses from the node's predicted value (the mean) and is used as the splitting criterion for regression trees:
$$\text{RSS} = \sum_{i \in R} (y_i - \bar{y}_R)^2$$
where $R$ represents a region (node), $y_i$ are the target values of observations in that region, and $\bar{y}_R$ is the mean of those target values. Lower RSS means observations have similar target values. We choose the split that results in the largest reduction in RSS.

## Pure Leaf
A leaf node i.e. terminal node in which all the training data points have the same value for the response or target variable. 

## Tree Pruning
It is a technique to limit the growth of decision trees by either preventing weak branches to grow (pre-pruning) or by removing branches that contribute little to predictive accuracy after the tree has fully grown (post-pruning).

## Pre-pruning
Technique to limit the growth of decision trees by setting stricter stopping criteria.

## Post-pruning
Technique to limit the growth of decision trees by removing branches that contribute little to predictive accuracy after the tree has fully grown.

## Weak Learners
Each of the building blocks i.e. simpler models that make an ensemble method are called Weak Learners. 

## Bagging
An ensemble technique in which several training datasets are created by bootstrapping from the original training dataset and then each of the weak learner models are trained on one of the bootstrapped datasets. To make the final prediction, all the predictions are aggregated. In case of regression the final prediction is the average of the predictions, in case of classification, the final prediction is the mode of all the predictions. 

## Random Forest
An ensemble technique of building several decision trees on bootstrapped training datasets, just like bagging, with a tweak that at every single node a random set of $m$ features (where $m < p$) are selected out of $p$ features and the split at that node can only be made using a feature from that set. 

## Boosting
An ensemble technique in which the weak learner models are trained sequentially. Each model is created to improve on the errors of the previous model. At the end, all the weak learners contribute to the final prediction with certain weights depending on the performance of each weak learner during the training. 

## AdaBoost
AdaBoost is an ensemble learning technique based on the idea of boosting. In this, each tree is created to correct the errors of the previous tree by increasing the weights of misclassified training samples so the next tree focuses on harder cases. 

## Stump
A decision tree with one node and two leaves. 

## Gradient Boosting
Gradient Boosting is an ensemble learning technique based on the idea of boosting. It repeatedly fits new trees to the residuals (errors) of the current model.