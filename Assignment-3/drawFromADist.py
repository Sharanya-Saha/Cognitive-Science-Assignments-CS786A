import numpy as np

def find(a) :
    return np.array([i for i,val in enumerate(a) if val > 0])


def drawFromADist(p) :
    if np.sum(p)==0 :
        p = 0.05*np.ones(len(p))
    
    p=p/np.sum(p)
    rand = np.random.uniform()
    idx=find((rand-np.cumsum(p))<0)
    sample=min(idx)
    out = np.zeros(len(p))
    out[sample] = 1.0

    return out