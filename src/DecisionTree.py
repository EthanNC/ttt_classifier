from collections import Counter
import unittest
import math

def class_counts(rows):
        counts = {}  # a dictionary of label -> count.
        for row in rows:
            # in our dataset format, the label is always the last column
            #print(row)
            label = row["attributes"]
            if label not in counts:
                counts[label] = 0
            counts[label] += 1
        return counts

class TreeNode(object):
    def __init__(self, question, true_branch, false_branch, isLeaf=False):
        # Your code here
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.isLeaf = isLeaf

    def predict(self, sample):
        """
        This function predicts the label of given sample
        """
        # Your code here

class Question:
    """A Question is used to partition a dataset.

    This class just records a 'column number' (e.g., 0 for Color) and a
    'column value' (e.g., Green). The 'match' method is used to compare
    the feature value in an example to the feature value stored in the
    question. See the demo below.
    """

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        # if val != self.value:
        #     return val >= self.value
        # else:
        return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
    
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))


class Leaf():
    def __init__(self, records):
        self.predictions = class_counts(records)
       

class DecisionTree(object):
    """
        Class of the Decision Tree
    """
    
    def __init__(self):
        self.root = None
        my_tree = None

    def stopping_cond(self, records, attributes):
        """
        The stopping_cond() function is used to terminate the tree-growing
        process by testing whether all the records have either the same class
        label or the same attribute values.

        This function should return True/False to indicate whether the stopping
        criterion is met.
        """
        # Your code here


    def classify(self, row, node):
        """
        This function determines the class label to be assigned to a leaf node.
        For each node t, let p(i|t) denote the fraction of training records from
        class i associated with the node t. In most cases, the leaf node is
        assigned to the class that has the majority number of training records

        This function should return a label that is assigned to the node
        """

        #if leaf return class assgined
        if isinstance(node, Leaf):
            for key in node.predictions.keys():
                return key
        #compare the attributes to the questions down the tree
        if node.question.match(row["label"]):
            return self.classify(row, node.true_branch)
        else:
            return self.classify(row, node.false_branch)

    def gini(self, records):
        """Replaced this method with entropy. Just think of entropy as impurity"""
        counts = class_counts(records)
        impurity = 1
        for lbl in counts:
            prob_of_lbl = counts[lbl] / float(len(records))
            impurity -= prob_of_lbl**2
        return impurity

    def info_gain(self, left, right, current_uncertainty):
        """Information Gain.
        The uncertainty of the starting node, minus the weighted impurity of
        two child nodes.
        """
        p = float(len(left)) / (len(left) + len(right))
        return current_uncertainty - p * self.gini(left) - (1 - p) * self.gini(right)

    def find_best_split(self, records, attributes):
        # Your code here
        # Hint-1: loop through all available attributes
        # Hint-2: for each attribute, loop through all possible values
        # Hint-3: calculate gain ratio and pick the best attribute

            # Split the records into two parts based on the value of the select
            # attribute

                # calculate the information gain based on the new split

                # calculate the gain ratio

                # if the gain_ratio is better the best split we have tested
                # set this split as the best split

        """Find the best question to ask by iterating over every feature / value
        and calculating the information gain."""
        best_gain = 0  # keep track of the best information gain
        best_question = None  # keep train of the feature / value that produced it
        length = len(records)
        current_uncertainty = self.gini(records)
        n_features = 9 # number of columns


        for col in range(n_features):  # for each feature

            #values = set([records[col] for row in records])  # unique values in the column 
            values = set()
            for row in records:
                values.add(row['label'][col])  # unique values in the column
            for val in values:  # for each value

                question = Question(col, val)

                # try splitting the dataset
                true_rows, false_rows = self.partition(records, question)

                # Skip this split if it doesn't divide the
                # dataset.
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue

                # Calculate the information gain from this split
                gain = self.info_gain(true_rows, false_rows, current_uncertainty)

                # You actually can use '>' instead of '>=' here
                # but I wanted the tree to look a certain way for our
                # toy dataset.
                if gain >= best_gain:
                    best_gain, best_question = gain, question

        return best_gain, best_question

    def partition(self, rows, question):
        """Partitions a dataset.

        For each row in the dataset, check if it matches the question. If
        so, add it to 'true rows', otherwise, add it to 'false rows'.
        """
        true_rows, false_rows = [], []
        for row in rows:
            if question.match(row['label']):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows

    def train(self, records, attributes):
        """
            This function trains the model with training records "records" and
            attribute set "attributes", the format of the data is as follows:
                records: training records, each record contains following fields:
                    label - the lable of this record
                    attributes - a list of attribute values
                attributes: a list of attribute indices that you can use for
                            building the tree
            Typical data will look like:
                records: [
                            {
                                "label":"p",
                                "attributes":['p','x','y',...]
                            },
                            {
                                "label":"e",
                                "attributes":['b','y','y',...]
                            },
                            ...]
                attributes: [0, 2, 5, 7,...]
        """
        my_tree = self.tree_growth(records,attributes)
        self.my_tree = my_tree


    def tree_growth(self, records, attributes):
        """
        This function grows the Decision Tree recursively until the stopping
        criterion is met. Please see textbook p164 for more details

        This function should return a TreeNode
        """
        # Your code here
        # Hint-1: Test whether the stopping criterion has been met by calling function stopping_cond()
        # Hint-2: If the stopping criterion is met, you may need to create a leaf node
        # Hint-3: If the stopping criterion is not met, you may need to create a
        #         TreeNode, then split the records into two parts and build a
        #         child node for each part of the subset
        gain, question = self.find_best_split(records, attributes)

        # Base case: no further info gain
        # Since we can ask no further questions,
        # we'll return a leaf.
        if gain == 0:
            return Leaf(records)

        # If we reach here, we have found a useful feature / value
        # to partition on.
        true_rows, false_rows = self.partition(records, question)

        # Recursively build the true branch.
        true_branch = self.tree_growth(true_rows, attributes)

        # Recursively build the false branch.
        false_branch = self.tree_growth(false_rows, attributes)

        # Return a Question node.
        # This records the best feature / value to ask at this point,
        # as well as the branches to follow
        # dependingo on the answer.
        return TreeNode(question, true_branch, false_branch)



    def predict(self, sample):
        """
        This function predict the label for new sample by calling the predict
        function of the root node
        """
        #return self.root.predict(sample)
        return self.classify(sample, self.my_tree)


# if __name__ == "__main__":
#   main().unittest

