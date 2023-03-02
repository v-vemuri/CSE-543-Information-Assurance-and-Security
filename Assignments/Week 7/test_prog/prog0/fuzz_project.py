import random
from random import seed
from random import randint
import sys
file = '/Users/bujjicutie/Downloads/CSE543 Information Assurance and Security/ISA/Assignments/Week 7/test_prog/prog0/seed'

File_object = open(file, "r")
starter_seed = File_object.read()

prng_seed = int(sys.argv[1])
iterations = int(sys. argv[2])


def fuzzer(starter_seed, prng_seed, iterations):
    starter_seed  += "" 
    Startseed = list(starter_seed)
    iteration_counter = 0
    for i in range(0, iterations):
        seed(prng_seed)
        iteration_counter += 1
        if iteration_counter == 500:
            for j in range(0, 10):
                rand_int = randint(0,255)
                add_char = chr(rand_int)
                Startseed.append(add_char)
                iteration_counter = 0
        for i in range (0, len(Startseed)):
            prob = randint(0, 100)
            if prob <= 13:
                int = randint(0, 255)
                character = chr(int)
                Startseed[i] = character
        prng_seed += 1
        output = "".join(Startseed)
    print(output)

fuzzer(starter_seed, prng_seed, iterations)
