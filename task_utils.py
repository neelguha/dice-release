# An assortment of utility functions for evaluating task performance
import numpy as np


def evaluate_entity_matching(predictions, X, Y):
    """ Evaluates performance for entity matching task 

    Args:
        predictions (dict): key corresponds to OFF entity, and value is predicted corresponding USDA entity or "None"
        X (list): list of OFF entities 
        Y (list): list of corresponding UDSA entities (or "None") 
    
    Returns:
        precision (float): precision 
        recall (float): recall
        f1 (float): F1 score
    """

    pairs = zip(X, Y)

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for off, usda_true in pairs:
        usda_pred = predictions[off]
        if usda_true == "None":
            if usda_true == usda_pred:
                tn += 1
            else:
                fp += 1
        else:
            if usda_true == usda_pred:
                tp += 1
            elif usda_pred == "None":
                fn += 1 
            else:
                fp += 1
    
    if tp + fp == 0:
        precision = 0
    else:
        precision = tp / (tp + fp)
    if tp + fn == 0:
        recall = 0
    else:
        recall = tp / (tp + fn)
    if precision + recall == 0:
        f1 = 0
    else:
        f1 = 2 *(precision*recall) / (precision + recall)
    return precision, recall, f1


def evaluate_arc_matching(predictions, X, Y):
    """ Evaluates performance for arc matching task 

    Args:
        predictions (dict): key corresponds to OFF arc, and value is predicted corresponding USDA arc or "None"
        X (list): list of OFF arcs 
        Y (list): list of corresponding UDSA arcs (or "None") 
    
    Returns:
        precision (float): precision 
        recall (float): recall
        f1 (float): F1 score
    """

    pairs = zip(X, Y)

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for off, usda_true in pairs:
        usda_pred = predictions[off]
        if usda_true == "None":
            if usda_true == usda_pred:
                tn += 1
            else:
                fp += 1
        else:
            if usda_true == usda_pred:
                tp += 1
            elif usda_pred == "None":
                fn += 1 
            else:
                fp += 1
    
    if tp + fp == 0:
        precision = 0
    else:
        precision = tp / (tp + fp)
    if tp + fn == 0:
        recall = 0
    else:
        recall = tp / (tp + fn)
    f1 = 2 *(precision*recall) / (precision + recall)
    return precision, recall, f1


def evaluate_multilabel_classification(y_true, predictions):
    """ Evaluates performance for multi-label classification tasks. 

    Args:
        y_true (NxC array): y_true[n, c] = 1 if the nth test sample belongs to class c and 0 otherwise.
        predictions (NxC array): predicted class membership array, follows same structure as y_true
    
    Returns:
        precision (float): precision 
        recall (float): recall
        f1 (float): F1 score

    """
    tp = np.sum(predictions*y_true) # samples where both prediction and y_true = 1
    fp = np.sum(predictions*(1-y_true)) # samples where prediction = 1 and y_true = 0
    fn = np.sum((1-predictions)*y_true) # samples where prediction = 0 and y_true = 1
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 *(precision*recall) / (precision + recall)
    return precision, recall, f1

def evaluate_regression(y_true, predictions):
    """ Returns mean-squared error 

    Args:
        y_true (array): true target values 
        predictions (array): predicted target values
    
    Returns:
        mse: mean squared error of predictions
    """
    return np.mean(np.square(y_true - predictions))


def evaluate_multi_classification(y_true, prediction):
    """ Returns accuracy for multi-class classification 

    Args:
        y_true (array): true classese
        predictions (array): predicted classes
    
    Returns:
        accuracy: accuracy of predictions
    """
    return np.mean(y_true == prediction)