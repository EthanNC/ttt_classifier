import random
import math
from collections import Counter
from DecisionTree import DecisionTree

class RandomForest(object):
    def __init__(self, tree_num):
        self.tree_num = tree_num
        self.forest = []

    def bootstrap(self, records):
        """
        This function bootstrap will return a set of records, which has the same
        size with the original records but with replacement.
        """
        # You code here


    def train(self, records, attributes):
        """
        This function will train the random forest, the basic idea of training a
        Random Forest is as follows:
        1. Draw n bootstrap samples using bootstrap() function
        2. For each of the bootstrap samples, grow a tree, with the following
            modification: at each node, randomly sample m of the predictors and
            choose the best split from among those variables
        """
        # Your code here

    def predict(self, sample):
        """
        The predict function predicts the label for new data by aggregating the
        predictions of each tree

        This function should return the predicted label
        """
        # Your code here
