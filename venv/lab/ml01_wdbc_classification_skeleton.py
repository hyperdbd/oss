import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, svm) # Mission #2 and #3) You need to import some modules if necessary
from matplotlib.lines import Line2D # For the custom legend

def load_wdbc_data(filename):
    class WDBCData:
        data = []
        target = []
        target_names = ['malignant', 'benign']
        feature_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
                         'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
                         'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
    wdbc = WDBCData()
    # TODO
    with open(filename) as f:
        data = [line.split(', ') for line in f.readlines()]

    wdbc.data = np.array(data)
    wdbc.target = wdbc.data[,:1]

    return wdbc

if __name__ == '__main__':
    # Load a dataset
    #wdbc = datasets.load_breast_cancer()
    wdbc = load_wdbc_data('../data/wdbc.data')
    #wdbc = load_wdbc_data('data/wdbc.data') # Mission #1) Implement 'load_wdbc_data()'

    # Train a model
    model = svm.SVC()                       # Mission #2) Try at least two different classifiers
    model.fit(wdbc.data, wdbc.target)

    # Test the model
    predict = model.predict(wdbc.data)
    n_correct = sum(predict == wdbc.target)
    accuracy = n_correct / len(wdbc.data)   # Mission #3) Calculate balanced accuracy

    # Visualize testing results
    cmap = np.array([(1, 0, 0), (0, 1, 0)])
    clabel = [Line2D([0], [0], marker='o', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    for (x, y) in [(0, 1)]: # Not mandatory, but try [(i, i+1) for i in range(0, 30, 2)]
        plt.title(f'svm.SVC ({n_correct}/{len(wdbc.data)}={accuracy:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y], c=cmap[wdbc.target], edgecolors=cmap[predict])
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
        plt.show()
