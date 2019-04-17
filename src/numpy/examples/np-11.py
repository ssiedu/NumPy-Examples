#appyling a function on nparray

import numpy as np;

def area(radius):
    return 3.14*radius*radius;

sd = np.array([1,2,3,4]);
res = np.fromfunction(area,sd[:1]);
print(sd);
print(res);


#################################WRONG CODE##############################################
