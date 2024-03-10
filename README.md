# GoITNeo Algo HW-9

## Task
We have a set of coins ```[50, 25, 10, 5, 2, 1]```. Imagine you are developing a system for a cash register that needs to determine the optimal way to give change to the customer.
You need to write two functions for the cash system that gives change to the customer:
 - *Greedy algorithm function* ```find_coins_greedy```. This function should take the amount to be given to the customer and return a dictionary with the quantity of coins of each denomination used to make up this amount. For example, for the amount 113, it would be a dictionary ```{50: 2, 10: 1, 2: 1, 1: 1}```. The algorithm should be greedy, meaning it selects the highest available coin denominations first.
 - *Dynamic programming function* ```find_min_coins```. This function should also take the amount for change but use dynamic programming to find the minimum number of coins needed to make up this amount. The function should return a dictionary with coin denominations and their quantities to achieve the desired amount most efficiently. For example, for the amount 113, it would be a dictionary ```{1: 1, 2: 1, 10: 1, 50: 2}```.

Compare the efficiency of the greedy algorithm and dynamic programming algorithm based on their execution time or Big O notation, focusing on their performance with large sums. Highlight how they handle large sums and why one algorithm may be more efficient than the other in certain situations. Include your conclusions in the readme.md file of the homework assignment.

### Solution
#### Prepared three functions:
 - ```find_coins_greedy``` - performs calculations on each call, no cache
 - ```find_min_coins``` - returns cached result or calls and caches ```find_coins_greedy```
 - ```find_min_coins_lru``` - uses LRU decorator for caching

#### Test flow:
 - run all functions 100 times and take total time for each method
 - run all functions 50_000 times ("training" or caching data)
 - run all functions 100 times again and take total time for each method but with cached data.

#### Results
```
Execution time before caching results:
        greedy : 0.07720000576227903
        min    : 0.07619999814778566
        min_lru: 0.07979999645613134
Execution time after caching results:
        greedy : 0.07340009324252605
        min    : 0.029900023946538568
        min_lru: 0.058500212617218494
```
### Conclusions
As we can see regular (greedy) function has constant time to of execution and it is good for cases when we have rarely called functions or when we are very limited in memory space but not in time.

On another hand the functions which uses caching (or dynamic programming principles) at the beginning has the same execution time as a regular function. But with more and more calls we will have more cached data and time will be reduced. And we will have dramatically increased performance in case of complicated calculations in the function. We have to remember about addition memory consumption for caching approach.

We can see one additional test result of comparison "hand-made" caching and LRU decorator. Out manual caching gave us better results. So, in decorator we add one extra function-wrapper which adds same overhead to time of calling a function. But this method will be more efficient when function execution time is much bigger than call-return-time.