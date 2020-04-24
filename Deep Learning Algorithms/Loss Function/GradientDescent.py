import numpy as np
class GradientDescent:
    '''
    Gradient Descent Algorithm Implementation
    '''
    def __init__(self,w,x,b,y):
        self.w = w
        self.b = b 
        self.x = x
        self.y = y
        
    def sigmoid(self,w,b,x):
        return 1.0/(1.0 + np.exp(-w*x + b))

    def grad_w(self,w,b,x,y):
        fx = sigmoid(w,x,b)
        return (fx - y) * fx *(1-fx) * x
    def grad_b(self,w,b,x,y):
        fx = sigmoid(w,b,x)
        return (fx - y) * fx *(1-fx)

    def Compute(self):
        w,b,eta = -2,-2,1.0
        epochs = 1000
        for i in range(epochs):
            dw = db = 0
            for x,y in zip(X,Y):
                dw = dw + grad_w(w,b,x,y)
                db = db + grad_b(w,b,x,y)
            w = w - eta * dw
            b = b - eta * db