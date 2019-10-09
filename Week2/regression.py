from sklearn.linear_model import Ridge
import numpy as np

if __name__=='__main__':
    
    rng = np.random.RandomState(0)
    
    clf = Ridge(alpha=1.0)
    clf.fit(X, y) 

    clf = SVR(gamma='scale', C=1.0, epsilon=0.2)
    clf.fit(X, y) 