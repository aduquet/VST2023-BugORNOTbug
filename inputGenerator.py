from typing import List
import random

#A string of up to `max_length` characters'''
#in the range [`char_start`, `char_start` + `char_range`)'''

def fuzzer(max_length: int = 100, char_start: int = 32, char_range: int = 32) -> str:

    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

def hundred_inputs(trials) -> List[str]:
    population = []
    for i in range(trials):
        population.append(fuzzer())
    return population

def fuzzer_2():
    from random import randrange, uniform

    # randrange gives you an integral value
    # irand = randrange(0, 10)
    # print(irand)
    # # uniform gives you a floating-point value
    # frand = uniform(0, 10)
    # print(frand)

    import numpy as np
    X2 = np.random.uniform(low=0, high=10, size=(100,)).astype(int) 
    print(X2)
    return X2


if __name__ == '__main__':
    # print(fuzzer(9, ord('0'), 10))
    x = fuzzer_2()

    import numpy as np
    import matplotlib.pyplot as plt
    mu, sigma = 200, 25
    # x = mu + sigma*np.random.randn(10000)
    # n, bins, patches = plt.hist(x)
    
    plt.hist(x)
    plt.show()