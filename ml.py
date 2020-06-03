from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

class MLModels(object):
    x_train = None
    x_test = None
    y_train = None
    y_test = None
    model = None
    parameters = None

    def __init__(self, x_train, x_test, y_train, y_test):
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def grid_search(self):
        clf_ = GridSearchCV(
            self.model, param_grid=self.parameters, n_jobs=-1, scoring='recall'
        )
        clf_.fit(self.x_train, self.y_train)
        best_estimator = clf_.best_estimator_
        print(f"Best estimator recall: {clf_.best_score_}")
        y_pred_ = best_estimator.predict(self.x_test)
        print('Precision Score : ' + str(precision_score(self.y_test, y_pred_)))
        print(f'Recall Score : {recall_score(self.y_test, y_pred_)}')
        print(confusion_matrix(self.y_test, y_pred_))

    def logistic_regression(self):
        self.model = LogisticRegression()
        self.parameters = [
            {
                'solver': ['saga'], 'penalty': ['l1', 'l2'], 'C': [0.001, 0.01, 1, 10, 25],
                'max_iter': [10, 20, 50, 100]
            },
            {
                'solver': ['sag', 'lbfgs'], 'penalty': ['l2'], 'C': [0.001, 0.01, 1, 10, 25],
                'max_iter': [10, 20, 50, 100]
            }
        ]
