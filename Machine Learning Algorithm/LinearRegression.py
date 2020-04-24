import numpy as np

class LinearRegression:

    def __init__(self,x,y,m_curr,b_curr):
        self.x = x
        self.y = y
        self.learning_rate = learning_rate
        self.iteration = iteration 
        self.m_curr = 0
        self.b_curr = 0

    def gradient_descent(self,x,y,iteration,m_curr=0,b_curr=0,learning_rate = 0.01):
        n = len(x)
        for i in range(iteration):
            y_predicted = m_curr * x + b_curr
            cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
            md = -(2/n) * sum(x*(y-y_predicted))
            bd = -(2/n) * sum(y-y_predicted)
            m_curr = m_curr - learning_rate * md
            b_curr = b_curr - learning_rate * bd
        return m_curr,b_curr
    
    def fit(self,x,y):
        pass

    def predict(self):
        pass


    
            

