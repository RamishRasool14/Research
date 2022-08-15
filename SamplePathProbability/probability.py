# write code to calculate probability of the following problem. 
# There is a straight line marked between -1,000,000 to +1,000,000. Kate initially stands at position O. She
# repeatedly tosses a fair coin that generates heads with probability 0.5, tails with probability 0.5. If she
# obtains heads, she goes forward one step (current position + 1) and if she obtains tails she goes
# backward one step (current position -1). She does this a million times. We wish to localize Kate to as narrow a range as possible. Choose the best description of where she is
# likely to be after the end of the process.

import random

def calculate_probability(n=1000000):
    """
    Calculate the probability of Kate being in a given position after n tosses.
    """
    heads = 0
    for i in range(n):
        if random.random() < 0.5:
            heads -= 1
        else:
            heads += 1
    return heads

def run_test(n = 1000):
    """
    Calculate probability of absolute value of function calculate_probability being less than 2000 and print every 10th iteration.
    """
    count = 0
    for i in range(n):
        if abs(calculate_probability()) < 2000:
            count += 1
        if i % 100 == 0:
            print(count)
    return count / n

print (run_test())