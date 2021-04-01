import time
import random

#This is the function that find the minimum operations needed to find the equal
def minOps(arr, k):
    #we sort the array
    arr = sorted(arr)
    #we define the the variable of opertions needed as 0 to start empty
    opsNeeded = 0
    #The for loop will append values to the array which is then appended to the opsneeded
    for i in range(k):
        opsNeeded += arr[k - 1] - arr[i]
    x = opsNeeded

    for i in range(k, len(arr)):
        opsNeeded = opsNeeded - (arr[i - 1] - arr[i - k])
        opsNeeded += (k - 1) * (arr[i] - arr[i - 1])
        x = min(x, opsNeeded)
    # we return the result of the for loops
    return x

#These are the arrays we are going to be using to test if the function works.

#First array
arr = [2, 7, 10, 19, 100]
n = len(arr)
k1 = 3
#second array
arr2 = [3, 8, 14, 1]
j = len(arr2)
k2 = 2
#Third array and so on
arr3 = [12, 57, 41, 8 , 2]
l = len(arr3)
k3 = 1

arr4 = [7, 22, 13, 3 , 110]
f = len(arr4)
k4 = 3

arr5 = [6, 11, 12, 31 , 73]
m = len(arr5)
k5 = 2

#We define the start of our time before the printing process
st = time.time()
#This prints out the outputs for the functions using the arrays and ks' we provided
print("Output: ",minOps(arr, k1))
print("output: ",minOps(arr2, k2))
print("output: ",minOps(arr3, k3))
print("output: ",minOps(arr4, k4))
print("output: ",minOps(arr5, k5))
'''
This prints out the running time of the system, the time it prints out is based on your system, a faster system will show
a 0.00~ because the recursion function is dependant on the system's memory. It is advised to use an online compiler to get
a more accurate time.
'''
print('Running time: {0:.8f}'.format(time.time() - st))


#This portion of the code will generate random arrays of varying sizes

#we request a k input from the user as well as the length of the array.
st1 = time.time()
k = 1  #You can select the value of K you want
arr_l = 1 #As well as

#This is the random list generator
rand_arr = sorted(random.sample(range(0, 100000), arr_l))
print("array of : ", arr_l, "created: ", rand_arr)


def opsNeeded(rand_arr, k):
    #Basically the same for loops used in minOps, only difference is the array we used is random.
    opsneeded = 0
    for i in range(k):
        opsneeded += rand_arr[k-1] - rand_arr[i]
    x = opsneeded
    for i in range(k, len(rand_arr)):
        opsneeded = opsneeded - (rand_arr[i - 1] - rand_arr[i - k])
        opsneeded += (k - 1) * (rand_arr[i] - rand_arr[i - 1])
        x = min(x, opsneeded)
    return x
    # This returns the result

print('Operations needed:', opsNeeded(rand_arr,k))
print('Running time: {0:.24f}'.format(time.time() - st1))