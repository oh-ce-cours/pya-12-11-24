from threading import Thread
import time


# Define a function for the thread
def print_time(thread_name, delay):
    count = 0

    while count < 5:
        time.sleep(delay)
        count += 1
        print("{}, {}".format(thread_name, time.ctime(time.time())))


# Create two threads as follows
t1 = Thread(
    target=print_time,
    args=(
        "Thread-1",
        1,
    ),
)
t2 = Thread(
    target=print_time,
    args=(
        "Thread-2",
        2,
    ),
)
t1.start()
t2.start()
print("Pas bloqué")
t1.join()
t2.join()
print("Fini")
