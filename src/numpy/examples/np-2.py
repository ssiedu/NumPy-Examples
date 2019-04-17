import numpy as np;
vector = np.linspace(10,20,5);#no of points  5 between 10 and 20
print(vector);


npa1=np.array([[10,20,30],[40,50,60]]);
print(npa1);
print(npa1.shape);
npa2=npa1.reshape(3,2); #converting array of 2x3 into 3x2
print(npa2);

npa3=np.arange(1,24,dtype=np.int16);
print(npa3);
print(npa3.ndim);   #returns 1 for 1dim 2 for 2dim and n for ndim
print(npa3.itemsize); # returns size of 1 item;
print(npa3.flags);

#creating an empty array
print("Empty Array");
npa4=np.empty([4,2],np.int32);
print(npa4);

#creating an array with all values 1
print("Ones Array");
npa5=np.ones([3,3]);
print(npa5);
