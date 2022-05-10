import requests
from time import sleep, time


#URL = 'http://verity-edge.lax.k8s.sx.ggops.com/xandr/page/classify?url=https://trilltrill.jp/articles/2247759'
#URL = 'http://localhost'
#URL = 'http://15.253.6.74'
#URL = 'http://70.224.227.122'
#URL = 'http://13.52.219.80'
#URL = 'http://54.188.245.97'
URL = 'http://34.227.14.247'
#DATA_OUTFILE = 'data_one_sec.csv'
#DATA_OUTFILE = 'data_one_min.csv'
#DATA_OUTFILE = 'data.csv'
#DATA_OUTFILE = 'data_localhost.csv'
#DATA_OUTFILE = 'data_same_localzone.csv'
#DATA_OUTFILE = 'data_other_localzone.csv'
#DATA_OUTFILE = 'data_us_west1.csv'
#DATA_OUTFILE = 'data_us_west2.csv'
DATA_OUTFILE = 'data_us_east1.csv'
#SLEEP_TIME = .1  # ten pings per second
SLEEP_TIME = 1  # one ping per second
#SLEEP_TIME = 10  # one ping every 10 seconds
#SLEEP_TIME = 60  # one ping per minute
PING_CUTOFF = 100000  # so we don't run forever and great a ginormous file

def timer_func(func):
    # This function shows the execution time of the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        ms = (t2 - t1) * 1000
        print(f'{int(t2)}: {ms:.2f}ms')
        f = open(DATA_OUTFILE, 'a')
        f.write(f'{int(t2)},{ms:.2f}\n')
        f.close()

    return wrap_func


@timer_func
def ping():
    r = requests.get(URL)


def pings():
    for _ in range(PING_CUTOFF):
        ping()
        sleep(SLEEP_TIME)


if __name__ == '__main__':
    pings()
