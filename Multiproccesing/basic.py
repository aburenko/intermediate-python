import multiprocessing
from time import sleep


def wait_and_print(n):
    sleep(n)
    print("spawned!")


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=wait_and_print, args=(1,))
        p.start()
