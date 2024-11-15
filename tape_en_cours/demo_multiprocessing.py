from multiprocessing import Pool
import time
import random


def f(x):
    time.sleep(random.random())
    print(x)
    return x * x


if __name__ == "__main__":
    tic = time.time()
    with Pool(3_000_000) as p:
        print(p.map(f, range(600)))
    print(f"total time: {time.time()-tic}")
