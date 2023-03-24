from __future__ import division
import numpy as np
import random, pdb
import operator

def roulette_selection(weights):
    sorted_indexed_weights = sorted(enumerate(weights), key=operator.itemgetter(1))
    indices, sorted_weights = zip(*sorted_indexed_weights)
    tot_sum=sum(sorted_weights)
    prob = [x/tot_sum for x in sorted_weights]
    cum_prob = np.cumsum(prob)
    random_num=random.random()

    for index_value, cum_prob_value in zip(indices, cum_prob):
        if random_num < cum_prob_value:
            return index_value

xanhdo = [47, 3, 50]
for i in range(10): 
    print (roulette_selection(xanhdo)) 

xanhdo1 = [17, 3, 50]
for i in range(10):
    print(roulette_selection(xanhdo1))

xanhdo2 = [77, 3, 50] 
for i in range(10):
    print(roulette_selection(xanhdo2))