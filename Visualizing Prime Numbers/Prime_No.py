'''
Given an integer n,determine if it's prime or not.
The algorithm should run in sqrt(n) time. Take it as 'Long Integer
Draw a table and a graph to show the values for n varying from 2^32 to 2^128 in steps of 100.
'''

import math
import time
import matplotlib.pyplot as plt
import numpy as np
import random


def prime_no_prime(no):
    if no <= 1:
        return False
    if no == 2:
        return True

    if no > 2 and no % 2 == 0:
        print('ok')
        return False
    else:
        print('okkkk')
        square_root = math.floor(math.sqrt(no))
        for multiplier in range(3,square_root+1,2):
            if no % multiplier ==0:
                return False
        return True


def get_last_five_numbers(no):
    return no % 10000000000


def get_array():
    array = list()
    final_no = int(input('Enter a number till which all total no of prime number will be calculated'))
    for iterator in range(final_no):
        temp_no = int(iterator)
        array.append(temp_no)
    return array
'''
starting_time = time.time()
flag = prime_no_prime(numbers)
ending_time = time.time()
total_time = ending_time - starting_time
if flag == 1:
    print('No is prime')
if flag == 0:
    print('No is not prime')
print('Total time taken by the algorithm :' + str(total_time))
'''
#array = get_array()
#power = int(input('Mention the power for 2'))
#number = pow(2,power)
#last_five_numbers = get_last_five_numbers(number)

#total = 0
#for iterator in array:
#    flag = prime_no_prime(iterator)
#    total += flag
numbers = list()
time_taken = list()
for i in range(10000):
    get_number = np.float64(random.randint(pow(2,32),pow(2,40)))
    starting_time = time.time()
    flag = prime_no_prime(get_number)
    ending_time = time.time()
    total_time = ending_time - starting_time
    print('Total time taken by the algorithm :' + str(total_time))
    if total_time is not 0.0:
        numbers.append(get_number)
        time_taken.append(total_time)
    else:
        continue
print(time_taken)
plt.plot(numbers,time_taken,'ro')
plt.show()
