**Class_structures**

This script implements the following logic:
1. Take all multiples of a provided number.
2. Extend the list of divisors when an odd length is given. For example, the divisors of 9 are [1, 3, 9], however the length of the array is 3, we only want even arrays, so we add the middle value in again, so we get [1, 3, 3, 9]. Therefore, the outer values are always a multiplication of 9 i.e. [1,9], [3,3].
3. Create a 2-dimensional array with n >= 1 rows.

Additional implementations:
1. Load the class into another python file. 
2. Build on logarithmic transformations for log(2).
3. Develop multiprocessing, queuing, scheduler, concurrency and multithreading options to improve speed for large numbers.

Current speed for 10 million:
1. 18/05/2021 - 14.2 seconds

Future aims:
1. Get into higher column dimensions.


Final objective:
1. Integrate with stocks from `Financial-Statistics` to develop ML models on the data.
