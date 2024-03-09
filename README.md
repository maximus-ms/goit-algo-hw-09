# GoITNeo Algo HW-9

## Task
We have a set of coins ```[50, 25, 10, 5, 2, 1]```. Imagine you are developing a system for a cash register that needs to determine the optimal way to give change to the customer.
You need to write two functions for the cash system that gives change to the customer:
 - *Greedy algorithm function* ```find_coins_greedy```. This function should take the amount to be given to the customer and return a dictionary with the quantity of coins of each denomination used to make up this amount. For example, for the amount 113, it would be a dictionary ```{50: 2, 10: 1, 2: 1, 1: 1}```. The algorithm should be greedy, meaning it selects the highest available coin denominations first.
 - *Dynamic programming function* ```find_min_coins```. This function should also take the amount for change but use dynamic programming to find the minimum number of coins needed to make up this amount. The function should return a dictionary with coin denominations and their quantities to achieve the desired amount most efficiently. For example, for the amount 113, it would be a dictionary ```{1: 1, 2: 1, 10: 1, 50: 2}```.

Compare the efficiency of the greedy algorithm and dynamic programming algorithm based on their execution time or Big O notation, focusing on their performance with large sums. Highlight how they handle large sums and why one algorithm may be more efficient than the other in certain situations. Include your conclusions in the readme.md file of the homework assignment.