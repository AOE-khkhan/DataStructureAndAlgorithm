import numpy as np

class LogisticRegression:
    def __init__(self,X,weight):
        self.weight = weight
        self.X = X

    def sigmoid(self,X, weight):
        z = np.dot(X, weight)
        return 1/(1 + np.exp(-z))
        
    def loss(h, y):
        return (-y*np.log(h) - (1-y)*np.log(1-h)).mean()
        
    def gradient_descent(self,X, h , y):
        return np.dot(X.T, (h-y))/y.shape[0]
        
    def update_weight_loss(self,weight, learning_rate, gradient):
        return weight - learning_rate * gradient

    def log_likelihood(self,x, y, weights):
        z = np.dot(x, weights)
        ll = np.sum(y*z - np.log(1 + np.exp(z)))
        return ll

    def gradient_ascent(self,X, h, y):
        return np.dot(X.T, y-h)

    def update_weight_mle(self,weight, learning_rate, gradient):
        return weight + learning_rate * gradient

    