# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i)
# for i in mygenerator:
#     print(i)

import time


def ft_progress(listy):
    for i in listy:
        yield i


def main():
    listy = range(3333)
    ret = 0
    old = time.time()
    current = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
        current = current + (time.time() - old)
        print("Elapsed time : %.2fs" % current, end="\r")
        old = time.time()
    print()
    print(ret)


if __name__ == "__main__":
    main()
