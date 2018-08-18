from django.shortcuts import render
from sklearn.metrics import roc_curve, auc
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from sklearn.datasets import make_classification



def main():

    print('start')
    features = np.load('features.npy')
    person_id = np.load('person_id.npy')


    #feature_similarity, true_labels = get_similarity(features, features[0], person_id[0], person_id)
    feature_similarity, true_labels = get_total_similarity(features, person_id)


    # actual code for roc + threshold charts start here
    # compute fpr, tpr, thresholds and roc_auc
    print(len(feature_similarity), len(true_labels))
    print(feature_similarity, true_labels)
    fpr, tpr, thresholds = roc_curve(true_labels, feature_similarity)
    print(len(tpr), tpr)
    print(len(fpr), fpr)
    print(len(thresholds), thresholds)
    roc_auc = auc(fpr, tpr)  # compute area under the curve

    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % (roc_auc))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")

    # create the axis of thresholds (scores)
    ax2 = plt.gca().twinx()
    ax2.plot(fpr, thresholds, markeredgecolor='r', linestyle='dashed', color='r')
    ax2.set_ylabel('Threshold', color='r')
    ax2.set_ylim([thresholds[-1], thresholds[0]])
    ax2.set_xlim([fpr[0], fpr[-1]])

    plt.savefig('roc_and_threshold_3.png')
    plt.close()


def get_similarity(features, current_vector, current_person, person_id):
    list_similarity = []
    list_classify = []
    confidence_values = []

    T = 0

    for index, vector in enumerate(features):
        similarity = np.dot(vector, current_vector)
        list_similarity.append(similarity)
        person = person_id[index]
        if similarity >= T:
            if not person == current_person:
                T = similarity

    for sim in list_similarity:
        confidence = sim/T
        #print('similarity: {0} | T: {1} | Probabilty: {2}'.format(sim, T, confidence))
        confidence_values.append(confidence)
        if sim >= T:
            list_classify.append(1)
        else:
            list_classify.append(0)

    feature_similarity = np.array(list_similarity)
    true_labels = np.array(list_classify)
    return feature_similarity, true_labels


def get_total_similarity(features, person_id):
    list_similarity = []
    list_classify = []
    confidence_values = []
    chunck = 0


    for index, vector_a in enumerate(features):
        T = 0
        person = person_id[index]
        for number, vector_b in enumerate(features):
            similarity = np.dot(vector_a, vector_b)
            list_similarity.append(similarity)
            current_person = person_id[number]
            if similarity >= T:
                if not person == current_person:
                    T = similarity

        for sim in list_similarity[chunck:]:
            confidence = sim/T
            #print('similarity: {0} | T: {1} | Probabilty: {2}'.format(sim, T, confidence))
            confidence_values.append(confidence)
            if sim >= T:
                list_classify.append(1)
            else:
                list_classify.append(0)
        chunck = chunck + len(features)

    feature_similarity = np.array(list_similarity)
    true_labels = np.array(list_classify)
    return feature_similarity, true_labels


main()