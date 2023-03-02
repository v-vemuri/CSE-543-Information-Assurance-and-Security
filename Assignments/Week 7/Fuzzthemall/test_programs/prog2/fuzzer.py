import random
from random import seed, randint
import sys

initial_seed = open('seed', "r").read()

prng_seed = int(sys.argv[1])
num_of_iterations = int(sys. argv[2])


def mutative_fuzzer(initial_seed, prng_seed, num_of_iterations):
    initial_seed = initial_seed + "" 
    initial_seed_list = list(initial_seed)

    for iter_num in range(0, num_of_iterations):
        seed(prng_seed)
        if (iter_num+1)%500 == 0:
            for i in range(0, 10):
                rand_char = chr(randint(0,255))
                initial_seed_list.append(rand_char)
    
        for itm in range (0, len(initial_seed_list)):
            prob = randint(0, 100)
            if prob <= 13:
                rand_char = chr(randint(0, 255))
                initial_seed_list[itm] = rand_char
        prng_seed += 1
        result = "".join(initial_seed_list)
    print('result', result)
    
 
mutative_fuzzer(initial_seed, prng_seed, num_of_iterations)

