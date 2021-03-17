import _thread
import logging
from time import ctime, sleep


# 设置日记记录器等级
logging.basicConfig(level=logging.INFO)

loops = [2, 4]

# def loop1():
#     logging.info("start loop1 at" + ctime())
#     sleep(2)
#     logging.info("end loop1 at" + ctime())
#
#
# def loop2():
#     logging.info("start loop2 at" + ctime())
#     sleep(4)
#     logging.info("end loop2 at" + ctime())


def loop(nloop, nsec, lock):
    logging.info("start loop" + str(nloop) + " at" + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at" + ctime())
    # 释放锁
    lock.release()


def main():
    logging.info("start all loop at" + ctime())
    # loop1()
    # loop2()
    # 存储锁
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        # 创建锁
        lock = _thread.allocate_lock()
        # 锁住
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        # 创建线程
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    logging.info("end all loop at" + ctime())


if __name__ == "__main__":
    main()
