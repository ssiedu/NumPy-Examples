import numpy as np;
list=[1,2,3,4,5];
npa1=np.array(list);
npa2=np.array([10,20,30]);
npa3=np.array([[5,6,7],[8,9,10]]);
npa4=np.arange(1,11);   #create an array from 1 to 10
npa5=np.zeros((4,4));   #create an array of size 4x4 with zeros as each element
npa6=np.zeros(4);       #create an array of size 4 with zero as each element
npa7=np.zeros((2,3,3)); #create an array of zeros of size 2x3x3 

print(npa1);
print(npa2);
print(npa3);
print(npa3);
print(npa4);
print(npa5);
print(npa6);
print(npa7);