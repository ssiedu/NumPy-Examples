#unary operations on array

import numpy as np;

sd=np.array([10,20,30,40,50]);
md=np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(sd);
print(md);

print(sd.max());    #maximum element
print(md.max());    #maximum element overall md

print(md.max(axis=1));  #row wise maximum element
print(md.max(axis=0));  #column wise maximum element

print(sd.sum());    #sum of all elements
print(md.sum());    #sum of all elements

print(md.sum(axis=1));  #sum row wise
print(md.sum(axis=0));  #sum col wise

print(md.cumsum(axis=1)); #cummulative sum row wise
print(md.cumsum(axis=0)); #cummulative sum col wise
print(md.cumprod(axis=1));#cummulative prod row wise
print(md.cumprod(axis=0));#cummulative prod col wise

