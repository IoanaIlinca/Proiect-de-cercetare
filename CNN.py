import os
from sklearn import tree
import numpy
from sklearn import metrics
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import classification_report


def load_file(filepath):
    f = open(filepath, 'r')
    paths = []
    content = f.readlines()
    for line in content:
        text = line
        text = text.strip("[]\n ")
        text = text.split("], [")
        path = []
        for pair in text:
            x = float(pair.split(", ")[0])
            y = float(pair.split(", ")[1])
            paths.append(x * 20 + y)
        # paths.append(path)

    return paths


# load a list of files into a 3D array of [samples, timesteps, features]


def load_group(directory):
    loaded = []
    for filename in os.listdir(directory):
        result = load_file(os.path.join(directory, filename))
        loaded.append(result)

    return loaded


# load the dataset, returns train and test X and y elements


def load_dataset():
    # load all train
    trainX = load_group("drive/MyDrive/train_input")
    trainY = load_group("drive/MyDrive/train_result")
    testX = load_group("drive/MyDrive/test_input")
    testY = load_group("drive/MyDrive/test_result")

    return trainX, trainY, testX, testY


if __name__ == "__main__":
    trainX, trainY, testX, testY = load_dataset()
    # trainX = [1, 1, 2, 1, 2, 3]

    '''
    clf = tree.DecisionTreeClassifier()
    lst1 = []
    for value in trainX:
       for val in value:
          lst1.append(val)
    lst2 = []
    for value in trainY:
       for val in value:
          lst2.append(val)

    lst1 = numpy.array(lst1)
    lst2 = numpy.array(lst2)
    lst1 = lst1.reshape(1, -1)
    lst2 = lst2.reshape(1, -1)
    clf = clf.fit(lst1, lst2)

    lst3 = []
    for value in testX:
       for val in value:
          lst3.append(val)
    lst3 = numpy.array(lst3)
    lst3 = lst3.reshape(1, -1)
    y_pred = clf.predict(lst1)
    print("Accuracy:", metrics.accuracy_score(lst2, y_pred))
    '''
    knn = tree.DecisionTreeClassifier()
    classifier = MultiOutputClassifier(knn, n_jobs=-1)
    classifier.fit(MultiLabelBinarizer().fit_transform(trainX), MultiLabelBinarizer().fit_transform(trainY))
    y_pred = classifier.predict(MultiLabelBinarizer().fit_transform(testX))
    cr_y1 = classification_report(MultiLabelBinarizer().fit_transform(testY)[:, 0], y_pred[:, 0])
    cr_y2 = classification_report(MultiLabelBinarizer().fit_transform(testY)[:, 1], y_pred[:, 1])

    print(cr_y1)
    print(cr_y2)
