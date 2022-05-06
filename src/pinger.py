import requests
from time import sleep, time


DATA_OUTFILE = 'data.csv'


def timer_func(func):
    # This function shows the execution time of the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        ms = (t2 - t1) * 1000
        print(f'Function{func.__name__!r} executed in {ms:.2f}ms')
        f = open(DATA_OUTFILE, 'a')
        f.write(f'{ms:.2f}\n')
        f.close()

    return wrap_func


@timer_func
def ping():
    r = requests.get('http://52.53.207.225/')


def pings():
    for _ in range(10):
        ping()
        sleep(1)


if __name__ == '__main__':
    pings()
