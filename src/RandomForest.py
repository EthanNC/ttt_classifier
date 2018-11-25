import random
import math
from collections import Counter
from DecisionTree import DecisionTree

import numpy as numpy

class RandomForest(DecisionTree):
    def __init__(self, tree_num):
        self.tree_num = tree_num
        self.forest = []

    def bootstrap(self, records):
        """
        This function bootstrap will return a set of records, which has the same
        size with the original records but with replacement.
        """
        # You code here
        new_record = numpy.array(records)
        record_replacement = numpy.random.choice(new_record, size=new_record.shape, replace=True)
        return record_replacement


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
        for i in self.tree_num:
            sample = self.bootstrap(records)
            tree = DecisionTree.tree_growth(self ,sample, attributes)
            self.forest.append(tree)
        
            

    def predict(self, sample):
        """
        The predict function predicts the label for new data by aggregating the
        predictions of each tree

        This function should return the predicted label
        """
        # Your code here
        negative = []
        positive = []
        for tree in self.forest:
            label = DecisionTree.classify(self,sample, tree)
            if label == "negative":
                negative.append(label)
            else:
                positive.append(label)

        if len(positive) > len(negative):
            return "positive"
        else:
            return "negative"
