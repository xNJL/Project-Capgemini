import numpy as np 

def cosine_similarity(v_w1, v_w2):
    theta_num = np.dot(v_w1, v_w2)
    theta_den = np.linalg.norm(v_w1) * np.linalg.norm(v_w2)
    theta = theta_num / theta_den    
    return theta 

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

