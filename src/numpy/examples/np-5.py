# ways to create array

# by using python list or tuple

import numpy as np;

list=[10,20,30,40];
tuple=(11,12,13,14);

ar1=np.array(list);
print(ar1);

ar2=np.array(tuple);
print(ar2);

#sometimes the size of array is known but elements are unknown.
#we can create array using some initial place holders like 0 or ones etc

ar3=np.zeros((3,4));    #creating array of size 3x4 with all elements 0
print(ar3);

ar4=np.full((3,3),10);  #creating an array of size 3x3 with each element 10
print(ar4);

ar5=np.ones((2,2));     #creating an array of size 2x2 with 1 as each element
print(ar5);

ar6=np.random.random((3,3));
print(ar6);

ar7=np.arange(0,50,10);#creating a sequence of integers from 0 to 50 step 10
print(ar7);

ar8=np.linspace(0,50,5);
print(ar8);         #creating a sequential array with 5 values between 0,50 (including 0,50)

ar9=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]);
print(ar9.shape);
ar10=ar9.reshape([2,6]);    #reshaping an array of size 3x4 to 2x6
print(ar10);    

ar11=ar9.flatten();         #flattenning a multi dim array to one dim
print(ar11);
