from multiprocessing import Pool
import time


def f(x):
    time.sleep(1)
    return x * x


if __name__ == "__main__":
    tic = time.time()
    with Pool(30) as p:
        print(p.map(f, range(60)))
    print(f"total time: {time.time()-tic}")
